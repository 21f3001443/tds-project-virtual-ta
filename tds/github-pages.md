## Static hosting: GitHub Pages

[GitHub Pages](https://pages.github.com/) is a free hosting service that turns your GitHub repository directly into a static website whenever you push it. This is useful for sharing analysis results, data science portfolios, project documentation, and more.

Common Operations:

```bash
# Create a new GitHub repo
mkdir my-site
cd my-site
git init

# Add your static content
echo "<h1>My Site</h1>" > index.html

# Push to GitHub
git add .
git commit -m "feat(pages): initial commit"
git push origin main

# Enable GitHub Pages from the main branch on the repo settings page
```

Best Practices:

1. **Keep it small**
   - [Optimize images](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Performance/Multimedia). Prefer SVG over WEBP over 8-bit PNG.
   - [Preload](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel/preload) critical assets like stylesheets
   - Avoid committing large files like datasets, videos, etc. directly. Explore [Git LFS](https://git-lfs.github.com/) instead.

Tools:

- [GitHub Desktop](https://desktop.github.com/): GUI for Git operations
- [GitHub CLI](https://cli.github.com/): Command line interface
- [GitHub Actions](https://github.com/features/actions): Automation

[![Host a website using GitHub Pages](https://i.ytimg.com/vi_webp/WqOXxoGSpbs/sddefault.webp)](https://youtube.com/shorts/WqOXxoGSpbs)

[![Deploy your first GitHub Pages Website](https://i.ytimg.com/vi_webp/sT_zXIX3ZA0/sddefault.webp)](https://youtu.be/sT_zXIX3ZA0
<youtube_summary>In this GitHub session, Rozelle Scarlett, a Developer Advocate at GitHub, demonstrates how beginners can efficiently use GitHub tools like CodeSpaces, Copilot, and GitHub Actions to develop, deploy, and automate projects. Rozelle explains her role focusing on introducing beginners to open source, and showcases a workflow starting from opening a Next.js template in GitHub CodeSpaces, which provides a ready-to-use development environment accessible via browser, beneficial especially for users with limited local resources.

She builds a simple to-do list web application using GitHub Copilot, an AI pair programmer that generates code based on comments (a technique called prompt engineering). Rozelle emphasizes writing clear comments to guide Copilot in creating desired functionality, such as adding and deleting to-do items. She demonstrates how Copilot assists in importing necessary packages, creating state, functions, and rendering UI components, significantly speeding up development.

After coding, Rozelle pushes the project to a GitHub repository and uses GitHub Actions to automate deployment to GitHub Pages. She highlights that GitHub Actions is a versatile automation tool extending beyond continuous integration/continuous deployment (CI/CD) to automate various tasks like running scripts, managing collaborators, and more. GitHub automatically detects the project type and generates the appropriate workflow YAML file, simplifying deployment especially for beginners unfamiliar with YAML syntax.

The session includes explanations about GitHub Actions features, such as cloud-hosted runners supporting multiple operating systems, and showcases real-world examples of custom actions—like automatically assigning issues or adding collaborators—to streamline project management and onboarding. Additionally, Rozelle introduces the GitHub Actions VS Code extension, which allows developers to view action logs directly in their editor for easier debugging.

Resources shared include links to GitHub CodeSpaces templates, the demo repository used, and encouragement to try creating projects from scratch using these tools. The session concludes with an invitation to join upcoming deeper dives into GitHub CodeSpaces and an open call for questions from the audience, emphasizing the accessibility and power of GitHub’s integrated development and automation ecosystem for developers of all levels.</youtube_summary>
)
