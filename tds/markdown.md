## Documentation: Markdown

Markdown is a lightweight markup language for creating formatted text using a plain-text editor. It's the standard for documentation in software projects and data science notebooks.

Watch this introduction to Markdown (19 min):

[![Markdown Crash Course (19 min)](https://i.ytimg.com/vi_webp/HUBNt18RFbo/sddefault.webp)](https://youtu.be/HUBNt18RFbo
<youtube_summary>This video is a comprehensive crash course on Markdown, aimed at both beginners and those familiar with some syntax but wanting to learn more. Markdown is a lightweight markup language with plain text formatting that is easy to read and converts to HTML and other formats. It is widely used for README files, documentation on GitHub, forum posts, blog posts, and static site generators like Gatsby.

The tutorial covers:
- Basic Markdown syntax including headings (using #), emphasis (italic with single * or _, bold with double ** or __), strikethrough (double ~~), horizontal rules (--- or ___), block quotes (>), links ([text](URL "title")), unordered lists (using *), ordered lists (numbers), inline code (backticks `), and images (![alt](URL)).
- GitHub-flavored Markdown features such as fenced code blocks with syntax highlighting (using triple backticks ``` with language specified), tables, and task lists with checkboxes ([x]).
- Tips on escaping Markdown characters with a backslash (\) to display them literally.

The presenter recommends using Visual Studio Code with the "Auto Open Markdown Preview" extension for live previewing Markdown, but mentions other editors like Atom, Sublime Text, or dedicated Markdown editors such as Markpad and Harupad are also options.

The video demonstrates creating a README.md file with Markdown syntax, initializing a Git repository, committing the file, and pushing it to GitHub, showing how GitHub renders the Markdown including code blocks, tables, and task lists.

Finally, it mentions online converters to transform Markdown into HTML and provides a cheat sheet for reference. The overall message is that Markdown is simple, useful, and worth learning quickly for anyone involved in coding, documentation, or content creation.

The video is sponsored by Coding Dojo, a programming school that trains beginners into developers in 14 weeks, boasting over 90% job placement within three months, often with salaries over $70K. Links to Coding Dojo are provided in the description.</youtube_summary>
)

Common Markdown syntax:

````
# Heading 1
## Heading 2

**bold** and *italic*

- Bullet point
- Another point
  - Nested point

1. Numbered list
2. Second item

[Link text](https://url.com)
![Image alt](image.jpg)

```python
# Code block
def hello():
    print("Hello")
```

> Blockquote
````

There is also a [GitHub Flavored Markdown](https://github.github.com/gfm/) standard which is popular. This includes extensions like:

```
- [ ] Incomplete task
- [x] Completed task

~~Strikethrough~~

Tables:

| Column 1 | Column 2 |
|----------|----------|
| Cell 1   | Cell 2   |

```

Tools for working with Markdown:

- [markdown2](https://pypi.org/project/markdown2/): Python library to convert Markdown to HTML
- [markdownlint](https://github.com/DavidAnson/markdownlint): Linting
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one): VS Code extension
- [pandoc](https://pandoc.org/): Convert between formats
