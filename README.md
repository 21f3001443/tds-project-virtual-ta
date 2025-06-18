
# **Project Report: TDS Virtual TA**

## **Project Title**

**TDS Virtual TA — A Virtual Teaching Assistant for Discourse Q\&A**

## **Submitted By**

*21f3001443*
*B.Sc. in Programming and Data Science (Online)*
*IIT Madras*

---

## **1. Objective**

To develop a Virtual Teaching Assistant (TA) system that responds to student queries related to the *Tools in Data Science (TDS)* course using publicly available course content and Discourse discussions. This system leverages large language models (LLMs) and retrieval-augmented generation (RAG) techniques to return context-aware answers with links to references.

---

## **2. Key Features**

* **LLM-based Answering (GPT-4.0)**
* **RAG Pipeline with Reranker for Quality Enhancement**
* **Multi-source Ingestion: Markdown, Discourse, YouTube**
* **File Attachment Support (base64 images)**
* **Image-to-Text via Gemini Flash Model**
* **Answers with Citation Links**
* **<30s Response SLA**

---

## **3. Tech Stack Overview**

| Component            | Technology Used                                 |
| -------------------- | ----------------------------------------------- |
| Programming Language | Python 3.10                                     |
| API Framework        | FastAPI                                         |
| Embedding Model      | OpenAI `text-embedding-3-small`                 |
| LLM Model            | OpenAI `gpt-4.0`                                |
| Reranker             | LLM-based reranking pipeline                    |
| Vector Store         | NumPy `.npz` format (vectors + source metadata) |
| Hosting              | Hugging Face Spaces (Dockerized deployment)     |
| Discourse Scraper    | Discourse API                                   |
| Course Content       | TDS markdown content from GitHub                |
| Image OCR            | Gemini `gemini-2.0-flash`                       |
| Video Transcripts    | YouTube API for transcript extraction           |
| Version Control      | Git + GitHub                                    |

---

## **4. Data Ingestion Workflow**

1. **Discourse Posts**

   * Scraped using Discourse API (1 Jan 2025 – 14 Apr 2025)
   * Stored as structured `.txt` files (post, topic ID, date, link)

2. **TDS Course Content**

   * Markdown files downloaded directly from official GitHub repo
   * Used as-is in chunking and embedding

3. **Images in Posts**

   * Image URLs extracted from Discourse posts
   * Converted to text using Gemini 2.0 Flash model

4. **Video Resources**

   * Transcripts obtained via YouTube Data API
   * Text chunks added to document corpus

---

## **5. Embedding & Retrieval**

* Documents are normalized, chunked, and embedded using OpenAI `text-embedding-3-small`
* Stored using NumPy `.npz` archives with corresponding metadata
* Upon receiving a question, similarity search retrieves top-K relevant chunks

---

## **6. Answer Generation Pipeline**

1. Accepts `POST` request to the API:

   ```json
   {
     "question": "...",
     "image": "..."  // optional base64
   }
   ```

2. Embeds question and performs vector similarity search

3. Retrieves top results and re-ranks using LLM-based reranker

4. Sends top-ranked context + question to `gpt-4.0`

5. Responds with answer and relevant links

---

## **7. Deployment**

* **Hosting:** Hugging Face Spaces (Docker container)
* **Public API Endpoint:**
  👉 [https://21f3001443-tds-project-virtual-ta.hf.space/api](https://21f3001443-tds-project-virtual-ta.hf.space/api)

---

## **8. Sample Request**

```bash
curl "https://21f3001443-tds-project-virtual-ta.hf.space/api" \
  -H "Content-Type: application/json" \
  -d '{
        "question": "Should I use gpt-4o-mini which AI proxy supports, or gpt3.5 turbo?",
        "image": "<base64_encoded_image>"
      }'
```

### Sample JSON Response

```json
{
  "answer": "You must use `gpt-3.5-turbo-0125`, even if the AI Proxy only supports `gpt-4o-mini`. Use the OpenAI API directly for this question.",
  "links": [
    {
      "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939",
      "text": "Clarification on GPT model selection"
    },
    {
      "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939",
      "text": "Related discussion on tokenizer usage"
    }
  ]
}
```

---

## **9. Evaluation Checklist**

| Requirement                    | Status       |
| ------------------------------ | ------------ |
| Public GitHub Repository       | ✅ Yes        |
| MIT License File               | ✅ Yes        |
| POST API with JSON Support     | ✅ Yes        |
| Image Support (base64)         | ✅ Yes        |
| Discourse Scraper              | ✅ Included   |
| promptfoo Compatible           | ✅ Yes        |
| Response < 30 sec              | ✅ Achieved   |
| RAG with Reranker              | ✅ Included   |
| Gemini Image-to-Text Pipeline  | ✅ Integrated |
| YouTube Transcript Integration | ✅ Done       |

---

## **10. Submission Links**

* 🔗 **API Endpoint:** [https://21f3001443-tds-project-virtual-ta.hf.space/api](https://21f3001443-tds-project-virtual-ta.hf.space/api)
* 🔗 **GitHub Repository:** [https://github.com/username/tds-virtual-ta](https://github.com/username/tds-virtual-ta)
* 🔗 **Submit Here:** [https://exam.sanand.workers.dev/tds-project-virtual-ta](https://exam.sanand.workers.dev/tds-project-virtual-ta)

---

## **11. Learnings**

* Practical implementation of RAG (retrieval-augmented generation)
* End-to-end AI system deployment with containerization
* Integration of image-to-text and transcript data for improved coverage
* Evaluation via automated tools like `promptfoo`
