# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "fastapi",
#     "google-genai",
#     "numpy",
#     "openai",
#     "pydantic",
#     "typing",
#     "uvicorn",
# ]
# ///

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from openai import OpenAI
import httpx
import numpy as np
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import re
from google import genai
from google.genai import types
import base64
import certifi
import json

os.environ["SSL_CERT_FILE"] = certifi.where()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),http_client=httpx.Client(verify=False))
aipipe_client = OpenAI(api_key=os.environ.get("AIPIPE_API_KEY"),base_url="https://aipipe.org/openai/v1",http_client=httpx.Client(verify=False))
google_client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


class QuestionRequest(BaseModel):
    question: str
    image: str = None

def parse_base64_data_uri(b64_with_prefix: str):
    match = re.match(r"data:(image/\w+);base64,(.+)", b64_with_prefix)
    if not match:
        raise ValueError("Invalid base64 image format or missing data URI prefix.")
    
    mime_type = match.group(1)
    base64_data = match.group(2)
    return mime_type, base64.b64decode(base64_data)

def understand_image_base64(b64_input: str):
    try:
        if b64_input.startswith("data:"):
            mime_type, image_bytes = parse_base64_data_uri(b64_input)
        else:
            mime_type, image_bytes = parse_base64_data_uri(f"data:image/webp;base64,{b64_input}")

        image = types.Part.from_bytes(data=image_bytes, mime_type=mime_type)

        response = google_client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[image, "What is in this image?"]
        )

        return response.text
    
    except Exception as e:
        return None


def getchunks(text: str, max_chunk_chars: int = 1000, overlap_chars: int = 200):
    length = len(text)
    # Determine step size, ensure it's positive
    step = max_chunk_chars - overlap_chars if max_chunk_chars > overlap_chars else max_chunk_chars
    chunks = []
    # Slide window across the text
    for start in range(0, length, step):
        end = start + max_chunk_chars
        chunks.append(text[start:end])
        if end >= length:
            break
    return chunks

def semantic_split_text(text: str, max_chunk_chars: int = 1000):
    normalized = text.replace('\n', '<NL>')

    return getchunks(normalized)

def get_embedding(chunk: str, model: str = "text-embedding-3-small"):
    response = client.embeddings.create(
        input=chunk,
        model=model
    )

    return response.data[0].embedding

def load_embeddings():
    data = np.load("embeddings.npz", allow_pickle=True)
    return data["chunks"],data["embeddings"],data["source_urls"]

def get_llm_answer(question:str, context: str):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful and formal assistant trained to answer user questions using only the provided context.\n\n"
                    "Instructions:\n"
                    "1. Respond strictly based on the given context. If insufficient information is available, reply: 'I don't know based on the available context.'\n"
                    "2. The response must be a summary of the answer and supporting context in **under 100 tokens**.\n"
                    "3. Keep your tone formal and consistent across all text blocks.\n"
                    "4. Ensure all blocks are cleanly formatted, formally worded, and styled consistently.\n"
                    "5. The complete response must not exceed 300 tokens total.\n"
                )
            },
            {
                "role": "user",
                "content": f"Question: {question}\n\nContext:\n{context}"
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "tda-response",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "answer": {
                            "type": "string",
                            "description": "The assistant's response to the user's question based on the provided context."
                        },
                        "links": {
                            "type": "array",
                            "description": "List of URLs used to support the answer.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "url": { 
                                        "type": "string",
                                        "description": "Must be a valid URL. If from Discourse, format should be: https://discourse.onlinedegree.iitm.ac.in/t/<slug>/<topic_id>/<post_number>. Fallback URL is available as 'Source'. Include all possible urls that could be used to support the answer."
                                    },
                                    "text": { 
                                        "type": "string",
                                        "description": "A brief description of the snippet's content."
                                    }
                                },
                                "required": ["url", "text"],
                                "additionalProperties": False
                            }
                        }
                    },
                    "required": ["answer","links"],
                    "additionalProperties": False
                }
            }
        },
        temperature=0.7,
        max_tokens=400
    )

    return response.choices[0].message.content

def get_llm_formatter(text:str):
    response = client.chat.completions.create(
        model="gpt-4o",  # or "gpt-4"
        messages=[
            {"role": "developer", "content": "You are a helpful assistant. Formalize the following text."},
            {"role": "user", "content": text}
        ],
        temperature=0.3,
        max_tokens=1000
    )
    return response.choices[0].message.content

def rerank_with_llm(question, top_chunks):
    prompt = f"""
You are a helpful assistant. Rerank the following context snippets in order of how relevant they are to the user question.

User Question:
{question}

Snippets:
""" + "\n\n".join([f"{i+1}. {chunk}" for i, chunk in enumerate(top_chunks)])

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    ranking = re.findall(r"(?:\*\*|^|\n)?(?:\d+\.\s*)?Snippet\s+(\d+)", response.choices[0].message.content, flags=re.IGNORECASE)

    return [int(i) - 1 for i in ranking]


def get_answer(question:str, image: str = None):
    chunks = semantic_split_text(question)
    if len(chunks) >1:
        embeddings_list = [get_embedding(chunk) for chunk in chunks]
        embeddings = np.mean(embeddings_list, axis=0)
    else:
        embeddings = get_embedding(chunks[0])
    final_chunks, final_embeddings, final_source_urls = load_embeddings()
    similarity = np.dot(final_embeddings, embeddings) / (np.linalg.norm(final_embeddings) * np.linalg.norm(embeddings))
    top_indices = np.argsort(similarity)[-5:][::-1]
    top_chunks = [final_chunks[i] for i in top_indices]
    rerank = rerank_with_llm(question, top_chunks)
    top_3_rerank_indices = rerank[:3]
    top_3_indices = [top_indices[i] for i in top_3_rerank_indices]
    top_chunks = [final_chunks[i] for i in top_3_indices]
    top_source_urls = [final_source_urls[i] for i in top_3_indices]
    formatted_chunks = "\n\n".join(
        [f"Snippet {i+1}: {chunk}\nSource: {top_source_urls[i]}" for i, chunk in enumerate(top_chunks)]
    )

    return json.loads(get_llm_answer(question, formatted_chunks))

@app.post("/api")
def handle_question(request: QuestionRequest):
    question = request.question
    if request.image:
        image_text = understand_image_base64(request.image)
        question = f"{question}\n\nImage Description:\n{image_text}"

    return JSONResponse(content=get_answer(question), status_code=200)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
