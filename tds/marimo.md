## Interactive Notebooks: Marimo

[Marimo](https://marimo.app/) is a new take on notebooks that solves some headaches of Jupyter. It runs cells reactively - when you change one cell, all dependent cells update automatically, just like a spreadsheet.

Marimo's cells can't be run out of order. This makes Marimo more reproducible and easier to debug, but requires a mental shift from the Jupyter/Colab way of working.

It also runs Python directly in the browser and is quite interactive. [Browse the gallery of examples](https://marimo.io/gallery). With a wide variety of interactive widgets, It's growing popular as an alternative to Streamlit for building data science web apps.

Common Operations:

```python
# Create new notebook
uvx marimo new

# Run notebook server
uvx marimo edit notebook.py

# Export to HTML
uvx marimo export notebook.py
```

Best Practices:

1. **Cell Dependencies**
   - Keep cells focused and atomic
   - Use clear variable names
   - Document data flow between cells
2. **Interactive Elements**

   ```python
   # Add interactive widgets
   slider = mo.ui.slider(1, 100)
   # Create dynamic Markdown
   mo.md(f"{slider} {"🟢" * slider.value}")
   ```

3. **Version Control**
   - Keep notebooks are Python files
   - Use Git to track changes
   - Publish on [marimo.app](https://marimo.app/) for collaboration

[!["marimo: an open-source reactive notebook for Python" - Akshay Agrawal (Nbpy2024)](https://i.ytimg.com/vi_webp/9R2cQygaoxQ/sddefault.webp)](https://youtu.be/9R2cQygaoxQ
<youtube_summary>AE Agraval presented a project called Marimo, an open-source reactive Python notebook developed over two years with co-maintainer Miles. Marimo aims to address common issues with traditional Python notebooks, particularly hidden state and irreproducibility caused by arbitrary cell execution order. Traditional notebooks can have code-output mismatches and are often not reproducible, as over a third of the 10 million Jupyter notebooks on GitHub were found to be non-reproducible.

Marimo’s key design goals are reproducibility—ensuring code matches outputs via reactive execution modeled as a directed acyclic graph (DAG) of cells; maintainability—using a pure Python file format that is easy to version control, executable as scripts, and importable as modules; and reusability—supporting execution as scripts and sharing as interactive web apps without exposing code. The reactive model, inspired by spreadsheets and reactive notebooks like Pluto (Julia) and Observable (JavaScript), automatically recalculates dependent cells on code changes, eliminating hidden state and making notebooks intuitive and bug-resistant.

A live demo showcased Marimo's features: live-updating plots reacting to variable changes, markdown with embedded Python values, UI elements like sliders for interactivity, and a complex embedding visualizer enabling selection and live preview of data points. Marimo enforces constraints such as no variable reassignment, banning cycles, and discouraging mutable variables across cells to maintain the reactive model.

Marimo notebooks are stored as Python files where each cell is a function with annotations; execution follows the DAG order guarded by the standard if __name__ == "__main__" entry point. They can be run from the command line with variable overrides, useful for data engineering workflows. The notebooks can also be served as reactive web apps via a CLI command that supports multiple client sessions.

Marimo also supports running entirely in the browser using Pyodide, aiding educational use cases. The project is open source and available on GitHub with a gallery of examples.

The name "Marimo" refers to a moss ball algae from lakes in Japan and Europe, chosen as a cute mascot. The team emphasized sticking to their design principles over supporting a traditional "Jupyter mode" to preserve reproducibility and reactivity.

In summary, Marimo is a reactive Python notebook designed for reproducibility, maintainability, and interactivity, addressing major issues in traditional notebooks by enforcing a reactive DAG model, using pure Python file format, and enabling execution as scripts or web apps.</youtube_summary>
)
