## LLM Sentiment Analysis

[OpenAI's API](https://platform.openai.com/) provides access to language models like GPT 4o, GPT 4o mini, etc.

For more details, read OpenAI's guide for:

- [Text Generation](https://platform.openai.com/docs/guides/text-generation)
- [Vision](https://platform.openai.com/docs/guides/vision)
- [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

Start with this quick tutorial:

[![OpenAI API Quickstart: Send your First API Request](https://i.ytimg.com/vi_webp/Xz4ORA0cOwQ/sddefault.webp)](https://youtu.be/Xz4ORA0cOwQ
<youtube_summary>The OpenAI API allows developers to make API calls using curl, Python, or Node.js. This video demonstrates how to use curl to make your first API call. First, you need to create an API key. Then, ensure curl is installed on your machine by running a command in the terminal. Next, set up the API key on a Mac by storing it in your bash profile or zshrc file, which are hidden files that can be revealed with Command + Shift + Period. In the zshrc file, export the API key by adding it in a text editor like VS Code. After this setup, you can make your first API request using the curl command. Running the curl command returns a response from the API. You can also monitor your API usage activity on the OpenAI dashboard. This process outlines how developers can make their first API call to the OpenAI API using curl.</youtube_summary>
)

Here's a minimal example using `curl` to generate text:

```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [{ "role": "user", "content": "Write a haiku about programming." }]
  }'
```

Let's break down the request:

- `curl https://api.openai.com/v1/chat/completions`: The API endpoint for text generation.
- `-H "Content-Type: application/json"`: The content type of the request.
- `-H "Authorization: Bearer $OPENAI_API_KEY"`: The API key for authentication.
- `-d`: The request body.
  - `"model": "gpt-4o-mini"`: The model to use for text generation.
  - `"messages":`: The messages to send to the model.
    - `"role": "user"`: The role of the message.
    - `"content": "Write a haiku about programming."`: The content of the message.

[![LLM Sentiment Analysis](https://i.ytimg.com/vi_webp/_D46QrX-2iU/sddefault.webp)](https://youtu.be/_D46QrX-2iU
<youtube_summary>The session explores using large language models (LLMs), specifically OpenAI's GPT models, for sentiment analysis and classification of movie reviews without any training. A small dataset of about 20 movie reviews labeled positive or negative is used. The speaker demonstrates using the OpenAI API via platform.openai.com playground, starting with GPT-3.5 Turbo (the least capable model at the time) and comparing results with GPT-4 and GPT-4 Turbo. They show that newer models provide more nuanced and accurate sentiment analysis.

Key points include:
- Initial zero-shot sentiment classification of movie reviews, with models sometimes giving conditional or ambiguous assessments.
- Improved accuracy by asking the model to explain its reasoning before giving sentiment.
- Discussion on token usage and cost: tokens roughly correspond to parts of words, with about 1 million tokens costing $5. The example review used 412 tokens.
- Explanation of how to access OpenAI’s API using Python requests, including creating and storing API keys securely in Colab.
- Step-by-step code walkthrough for loading movie reviews CSV, sending requests to the API for sentiment, and parsing JSON responses to extract sentiment.
- Demonstration of looping through the dataset and appending model-generated sentiment as a new column using pandas, employing a function with pandas apply method.
- Comparison of model-generated sentiments with original labels shows strong alignment with only minor disagreement.
- Discussion on potential use cases for training/fine-tuning models, especially for niche or company-specific needs, or for aspect-based sentiment analysis (e.g., sentiment about acting, storyline, direction).
- Demonstration of few-shot learning by providing example inputs and outputs in the prompt to teach the model how to identify sentiment for specific aspects within reviews.
- Clarification that this prompt-based "training" is done by including examples in the message array (system, user, assistant roles), which can be zero-shot, one-shot, or multi-shot prompting.
- Reminder that longer prompts and examples increase token usage and cost, so prompt engineering aims to balance accuracy with token efficiency.

Overall, the session illustrates how large language models can be effectively utilized for sentiment analysis and classification tasks out-of-the-box, with minimal setup and no traditional model training, and how prompt engineering and few-shot examples can further refine performance for specific tasks.</youtube_summary>
)

This video explains how to use large language models (LLMs) for sentiment analysis and classification, covering:

- **Sentiment Analysis**: Use OpenAI API to identify the sentiment of movie reviews as positive or negative.
- **Prompt Engineering**: Learn how to craft effective prompts to get desired results from LLMs.
- **LLM Training**: Understand how to train LLMs by providing examples and feedback.
- **OpenAI API Integration**: Integrate OpenAI API into Python code to perform sentiment analysis.
- **Tokenization**: Learn about tokenization and its impact on LLM input and cost.
- **Zero-Shot, One-Shot, and Multi-Shot Learning**: Understand different approaches to using LLMs for learning.

Here are the links used in the video:

- [Jupyter Notebook](https://colab.research.google.com/drive/1tVZBD9PKto1kPmVJFNUt0tdzT5EmLLWs)
- [Movie reviews dataset](https://drive.google.com/file/d/1X33ao8_PE17c3htkQ-1p2dmW2xKmOq8Q/view)
- [OpenAI Playground](https://platform.openai.com/playground/chat)
- [OpenAI Pricing](https://openai.com/api/pricing/)
- [OpenAI Tokenizer](https://platform.openai.com/tokenizer)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference/)
- [OpenAI Docs](https://platform.openai.com/docs/overview)
