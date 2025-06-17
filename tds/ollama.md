## Local LLM Runner: Ollama

[`ollama`](https://github.com/ollama/ollama) is a command-line tool for running open-source large language models entirely on your own machine—no API keys, no vendor lock-in, full control over models and performance.

[![Run AI Models Locally: Ollama Tutorial (Step-by-Step Guide + WebUI)](https://i.ytimg.com/vi_webp/Lb5D892-2HY/sddefault.webp)](https://youtu.be/Lb5D892-2HY
<youtube_summary>This guide covers everything you need to know about using Olama, from installation to advanced features, including setting up Open Web UI for a better interface and using Retrieval-Augmented Generation (RAG) to chat with your own documents.

**Installation and Setup:**
- Download Olama from olama.com by selecting your OS and running the installer.
- Start Olama via the desktop app (icon in system tray) or by running `olamaserve` in the terminal.
- Verify installation by running `olama` in the terminal to see available commands.

**Managing Models:**
- List available models with `olama list` (initially empty).
- Browse and select models on the Olama website by featured, popular, or newest.
- Models vary in size (e.g., 9 billion or 27 billion parameters) affecting hardware requirements.
- Download models with `olama pool <model-name>` without running them immediately.
- View downloaded models with `olama list` and get details using `olama show <model-name>`.
- Remove models using `olama rm <model-name>`.

**Running and Interacting with Models:**
- Run a model with `olama run <model-name>`.
- Models maintain conversation history during sessions.
- Use chat commands starting with `/set` to adjust session attributes:
  - `/set parameter temperature <value>` adjusts creativity (0 = factual, 1 = creative).
  - `/set system "<message>"` assigns personality or role to the model.
- View current settings with `/show parameters` or `/show system`.
- Save customized sessions as new models with `/save <model-name>`.
- Exit chat with `/bye`.

**Creating Custom Models via File:**
- Create a text file defining base model, parameters, and system message.
- Use `olama create <model-name> -f ./<filename>` in terminal within the folder containing the file.
- Confirm creation with `olama list` and view details with `olama show <model-name>`.
- Run the custom model like any other.

**Using Olama API:**
- Olama offers API endpoints to create messages and models.
- Example: Use Postman to POST to `http://localhost:11434` with JSON specifying model and prompt.
- Streaming responses can be toggled by setting `"stream": false` in the request body.

**Installing and Using Open Web UI:**
- Requires Docker installed from docker.com (Docker Desktop).
- Run the provided Docker command from the Open Web UI installation page.
- Access Open Web UI via browser, sign up, and log in.
- Select from available models and chat through a user-friendly interface.
- Upload documents to chat via RAG functionality (e.g., ask questions about uploaded files).

**Additional Resources:**
- A linked video demonstrates using Olama with Flow-wise for advanced AI applications.
- Viewers are encouraged to like, subscribe, and comment on favorite open source models.

This comprehensive overview enables users to install Olama, manage and customize models, interact via terminal or web UI, utilize APIs, and leverage document-based querying with RAG.</youtube_summary>
)

### Basic Usage

[Download Ollama for macOS, Linux, or Windows](https://ollama.com/) and add the binary to your `PATH`. See the full [Docs ↗](https://ollama.com/docs) for installation details and troubleshooting.

```bash
# List installed and available models
ollama list

# Download/pin a specific model version
ollama pull gemma3:1b-it-qat

# Run a one-off prompt
ollama run gemma3:1b-it-qat 'Write a haiku about data visualization'

# Launch a persistent HTTP API on port 11434
ollama serve

# Interact programmatically over HTTP
curl -X POST http://localhost:11434/api/chat \
     -H 'Content-Type: application/json' \
     -d '{"model":"gemma3:1b-it-qat","prompt":"Hello, world!"}'
```

### Key Features

- **Model management**: `list`/`pull` — Install and switch among Llama 3.3, DeepSeek-R1, Gemma 3, Mistral, Phi-4, and more.
- **Local inference**: `run` — Execute prompts entirely on-device for privacy and zero latency beyond hardware limits.
- **Persistent server**: `serve` — Expose a local REST API for multi-session chats and integration into scripts or apps.
- **Version pinning**: `pull model:tag` — Pin exact model versions for reproducible demos and experiments.
- **Resource control**: `--threads` / `--context` — Tune CPU/GPU usage and maximum context window for performance and memory management.

### Real-World Use Cases

- **Quick prototyping**. Brainstorm slide decks or blog outlines offline, without worrying about API quotas: `ollama run gemma-3 'Outline a slide deck on Agile best practices'`
- **Data privacy**. Summarize sensitive documents on-device, retaining full control of your data: `cat financial_report.pdf | ollama run phi-4 'Summarize the key findings'`
- **CI/CD integration**. Validate PR descriptions or test YAML configurations in your pipeline without incurring API costs: `git diff origin/main | ollama run llama2 'Check for style and clarity issues'`
- **Local app embedding**. Power a desktop or web app via the local REST API for instant LLM features: `curl -X POST http://localhost:11434/api/chat -d '{"model":"mistral","prompt":"Translate to German"}'`

Read the full [Ollama docs ↗](https://github.com/ollama/ollama/tree/main/docs) for advanced topics like custom model hosting, GPU tuning, and integrating with your development workflows.
