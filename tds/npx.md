## JavaScript tools: npx

[npx](https://docs.npmjs.com/cli/v8/commands/npx) is a command-line tool that comes with npm (Node Package Manager) and allows you to execute npm package binaries and run one-off commands without installing them globally. It's essential for modern JavaScript development and data science workflows.

For data scientists, npx is useful when:

- Running JavaScript-based data visualization tools
- Converting notebooks and documents
- Testing and formatting code
- Running development servers

Here are common npx commands:

```bash
# Run a package without installing
npx http-server .                # Start a local web server
npx prettier --write .           # Format code or docs
npx eslint .                     # Lint JavaScript
npx typescript-node script.ts    # Run TypeScript directly
npx esbuild app.js               # Bundle JavaScript
npx jsdoc .                      # Generate JavaScript docs

# Run specific versions
npx prettier@3.2 --write .        # Use prettier 3.2

# Execute remote scripts (use with caution!)
npx github:user/repo            # Run from GitHub
```

Watch this introduction to npx (6 min):

[![What you can do with npx (6 min)](https://i.ytimg.com/vi_webp/55WaAoZV_tQ/sddefault.webp)](https://youtu.be/55WaAoZV_tQ
<youtube_summary>Ryan H Lewis introduces NPX, a new CLI tool bundled with NPM version 5.0 and above, designed as a Node package executor to simplify running node packages in various ways. Key features include:

1. Running local binaries easily without manually specifying the node_modules/.bin path.
2. Executing binaries not yet installed by temporarily downloading and running them without permanent installation.
3. Running command strings using the -c argument.

Use cases highlighted:

- Running local dependencies as if they were global, avoiding tedious path specifications, especially helpful in NPM scripts.
- Running infrequently used global binaries (e.g., Yeoman, Webpack CLI, Create React App) on demand without permanent global installation.
- Trying out new package versions before upgrading projects by using NPX to run different versions temporarily.
- Testing local code or branches from git repositories directly via NPX without complex setup like npm link.
- Running packages from sources other than the NPM registry, such as GitHub gists, by providing URLs to NPX (with a caution to review such code before execution).

Ryan invites viewers to share their thoughts and experiences with NPX and encourages liking and subscribing for more content related to Node, Webpack, AWS, Serverless, and other developer tools and topics.</youtube_summary>
)
