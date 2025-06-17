## LLM CLI: llm

[`llm`](https://pypi.org/project/llm) is a command-line utility for interacting with large language models—simplifying prompts, managing models and plugins, logging every conversation, and extracting structured data for pipelines.

[![Language models on the command-line w/ Simon Willison](https://i.ytimg.com/vi_webp/QUXQNi6jQ30/sddefault.webp)](https://youtu.be/QUXQNi6jQ30?t=100
<youtube_summary>The talk discusses the Unix command line as an ideal environment for experimenting with large language models (LLMs), highlighting the Unix philosophy of piping outputs between tools, which aligns well with how LLMs function by taking prompts and returning responses.

The speaker created a command line tool called "llm" (installable via pip or Homebrew) that initially interfaced with OpenAI’s API but has evolved to support numerous other models through a plugin system, including local models like Mistral and Claude 3 variants, enabling flexible use of both remote and local LLMs. The tool logs all interactions into a SQLite database, facilitating comprehensive tracking, analysis, and management of conversations and experiments via SQL queries or visualization tools like the speaker’s "data set" app.

Key features include:
- Easy installation and API key management.
- Support for multiple plugins adding access to various LLMs and additional functionalities.
- A command ("llm chat") to maintain local model sessions without reloading models each time.
- Ability to send images as part of prompts (feature forthcoming).
- A plugin ("llm-cmd") that generates shell commands from prompts, allowing users to review and execute them safely.
- Templates for system prompts to customize interactions.
- Tools to pipe and process input/output, facilitating workflows like summarizing Hacker News threads or running retrieval-augmented generation (RAG) pipelines by scraping web content with another tool ("shot scraper") and feeding results to LLMs.
- Embedding support with commands to generate, store, and query embeddings in SQLite, enabling semantic search over data collections such as blog posts or bookmarks.
- Plans to support structured output and function calling to enable agentic workflows and tool execution via plugins.
- Compatibility with a wide range of models including API-based and local ones, and the ability to switch between them easily.
- Discussion of local models running efficiently on modest hardware like recent Macs (M1/M2), with promising developments in Apple’s ML ecosystem and mobile devices (e.g., running Mistral 7B on iPhone).
- The tool’s scriptability allows users to build complex workflows, automate tasks, and explore language models deeply, including experimenting with smaller local models to learn LLM behaviors.
- The speaker emphasizes the importance of good project management practices such as writing unit tests and documentation to maintain productivity across multiple projects.
- Future goals include adding a web UI, better plugin ecosystem, integration with external vector databases, and improved evaluation tools.
- The speaker encourages community contributions, especially writing plugins for new models or APIs like Hugging Face.
- The Unix command line foundation allows the "llm" tool to be combined with existing tools like Ansible or Kubernetes for distributed workflows or parallel execution on multiple machines.

Overall, the talk showcases "llm" as a powerful, extensible, and scriptable command line interface for interacting with a wide array of LLMs and embedding models, supporting advanced workflows such as RAG, semantic search, and automated shell command generation, with strong tracking and analytical capabilities via SQLite logging. The speaker shares insights on local versus remote model use, hardware considerations, and ongoing development plans, inviting community involvement and highlighting the tool’s role in making LLM experimentation accessible and efficient on the command line.</youtube_summary>
)

### Basic Usage

[Install llm](https://github.com/simonw/llm#installation). Then set up your [`OPENAI_API_KEY`](https://platform.openai.com/api-keys) environment variable. See [Getting started](https://github.com/simonw/llm?tab=readme-ov-file#getting-started).

**TDS Students**: See [Large Language Models](large-language-models.md) for instructions on how to get and use `OPENAI_API_KEY`.

```bash
# Run a simple prompt
llm 'five great names for a pet pelican'

# Continue a conversation
llm -c 'now do walruses'

# Start a memory-aware chat session
llm chat

# Specify a model
llm -m gpt-4.1-nano 'Summarize tomorrow’s meeting agenda'

# Extract JSON output
llm 'List the top 5 Python viz libraries with descriptions' \
  --schema-multi 'name,description'
```

Or use llm without installation using [`uvx`](uv.md):

```bash
# Run llm via uvx without any prior installation
uvx llm 'Translate "Hello, world" into Japanese'

# Specify a model
uvx llm -m gpt-4.1-nano 'Draft a 200-word blog post on data ethics'

# Use structured JSON output
uvx llm 'List the top 5 programming languages in 2025 with their release years' \
  --schema-multi 'rank,language,release_year'
```

### Key Features

- **Interactive prompts**: `llm '…'` — Fast shell access to any LLM.
- **Conversational flow**: `-c '…'` — Continue context across prompts.
- **Model switching**: `-m MODEL` — Use OpenAI, Anthropic, local models, and more.
- **Structured output**: `llm json` — Produce JSON for automation.
- **Logging & history**: `llm logs path` — Persist every prompt/response in SQLite.
- **Web UI**: `datasette "$(llm logs path)"` — Browse your entire history with Datasette.
- **Persistent chat**: `llm chat` — Keep the model in memory across multiple interactions.
- **Plugin ecosystem**: `llm install PLUGIN` — Add support for new models, data sources, or workflows. ([Language models on the command-line - Simon Willison's Weblog](https://simonwillison.net/2024/Jun/17/cli-language-models/?utm_source=chatgpt.com))

### Practical Uses

- **Automated coding**. Generate code scaffolding, review helpers, or utilities on demand. For example, after running`llm install llm-cmd`, run `llm cmd 'Undo the last git commit'`. Inspired by [Simon’s post on using LLMs for rapid tool building](https://simonwillison.net/2025/Mar/11/using-llms-for-code/).
- **Transcript processing**. Summarize YouTube or podcast transcripts using Gemini. See [Putting Gemini 2.5 Pro through its paces](https://www.macstories.net/mac/llm-youtube-transcripts-with-claude-and-gemini-in-shortcuts/).
- **Commit messages**. Turn diffs into descriptive commit messages, e.g. `git diff | llm 'Write a concise git commit message explaining these changes'`. \
- **Data extraction**. Convert free-text into structured JSON for automation. [Structured data extraction from unstructured content using LLM schemas](https://simonwillison.net/2025/Feb/28/llm-schemas/).
