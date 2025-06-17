## Python tools: uv

[Install uv](https://docs.astral.sh/uv/getting-started/installation/).

[`uv`](https://docs.astral.sh/uv/) is a fast Python package and project manager that's becoming the standard for running Python scripts. It replaces tools like pip, conda, pipx, poetry, pyenv, twine, and virtualenv into one, enabling:

- **Python Version Management**: uv installs and manages _multiple_ Python versions, allowing developers to specify and switch between versions seamlessly.
- **Virtual Environment Handling**: It automates the creation and management of virtual environments, ensuring isolated and consistent development spaces for different projects.
- **Dependency Management**: With support for the pyproject.toml format, uv enables precise specification of project dependencies. It maintains a universal lockfile, uv.lock, to ensure reproducible installations across different systems.
- **Project Execution**: The `uv run` command allows for the execution of scripts and applications within the managed environment, streamlining development workflows.

Here are some commonly used commands:

```bash
# Replace python with uv. This automatically installs Python and dependencies.
uv run script.py

# Run a Python script directly from the Internet
uv run https://example.com/script.py

# Run a Python script without installing
uvx ruff

# Use a specific Python version
uv run --python 3.11 script.py

# Add dependencies to your script
uv add httpx --script script.py

# Create a virtual environment at .venv
uv venv

# Install packages to your virtual environment
uv pip install httpx
```

Here are some useful tools you can run with `uvx` without installation:

```bash
uvx --from jupyterlab jupyter-lab   # Jupyter notebook
uvx marimo      # Interactive notebook
uvx llm         # Chat with LLMs from the command line
uvx openwebui   # Chat with LLMs via the browser
uvx httpie      # Make HTTP requests
uvx datasette   # Browse SQLite databases
uvx markitdown  # Convert PDF to Markdown
uvx yt-dlp      # Download YouTube videos
uvx asciinema   # Record your terminal and play it
```

uv uses [inline script metadata](https://packaging.python.org/en/latest/specifications/inline-script-metadata/#inline-script-metadata) for dependencies.
The eliminates the need for `requirements.txt` or virtual environments. For example:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "pandas",
# ]
# ///
```

[![uv - Python package and project management | Inline Script Metadata (28 min)](https://i.ytimg.com/vi_webp/igWlYl3asKw/sddefault.webp)](https://youtu.be/igWlYl3asKw?t=1240
<youtube_summary>This video provides an in-depth introduction to UV, a new, extremely fast Python package and project management tool written in Rust. Created by the same team behind the Ruff formatter and linter, UV aims to replace multiple tools like pip, pip-tools, and pep-ex, offering installation speeds 10 to 100 times faster than pip. UV is popular, with over 23,000 GitHub stars, and supports project initialization, dependency management, automatic virtual environment creation, Python version management, and command-line tool execution.

Key features demonstrated include:

- Installing UV via standalone installers for Mac, Linux, Windows, or pip.

- Initializing a new Python project with `uv init`, specifying Python versions (e.g., 3.13), which creates a project directory with files including `pyproject.toml` that contains project metadata and dependencies.

- Adding dependencies (e.g., FastAPI, SQLAlchemy, Alembic) using `uv add`, which automatically creates a virtual environment, updates `pyproject.toml`, generates a `uv.lock` file with locked dependency versions, and updates `.gitignore`.

- Running projects using `uv run`, which uses the created virtual environment without manual activation.

- Synchronizing an environment with `uv sync` to install all dependencies from the lock file, useful when cloning projects.

- Managing optional and development dependencies, with optional dependencies added via `uv add --optional <group> <package>` and development dependencies added with `uv add -D <package>`, placed appropriately in `pyproject.toml`.

- Removing dependencies easily with `uv remove`.

- Viewing the dependency tree with `uv tree`.

- Running standalone Python scripts with dependencies specified either via the command line using `uv run --with <package>` or embedded as inline script metadata in the script file, which UV automatically reads to install dependencies when running the script.

- Generating inline script metadata automatically with `uv add --script <script.py> <dependencies>`.

- Creating virtual environments manually with `uv ven` if needed.

Additionally, UV supports managing command-line tools provided by Python packages, workspaces (collections of packages sharing a lock file), and Python version management per project. The video plans a follow-up on containerizing a FastAPI app with Docker using UV, and mentions integration guides for Jupyter notebooks, GitHub Actions, and pre-commit hooks.

The presenter highlights UV's speed, convenience in dependency and environment management, and its potential as the future tool for Python project management. Viewers are invited to comment for further videos on UV’s tool management and workspaces features and to support the channel.</youtube_summary>
)

<!-- Assessment: Share output of `uv run --with httpie -- https https://httpbin.org/get?email={email}` -->
<!-- Assessment: Share output of `uvx markitdown {email}.pdf` -->
<!-- Assessment: Share output of `uv ruff format script.py` -->
