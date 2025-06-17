## CI/CD: GitHub Actions

[GitHub Actions](https://github.com/features/actions) is a powerful automation platform built into GitHub. It helps automate your development workflow - running tests, deploying applications, updating datasets, retraining models, etc.

- Understand the basics of [YAML configuration files](https://docs.github.com/en/actions/writing-workflows/quickstart)
- Explore the [pre-built actions from the marketplace](https://github.com/marketplace?type=actions)
- How to [handle secrets securely](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)
- [Triggering a workflow](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)
- Staying within the [free tier limits](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions)
- [Caching dependencies to speed up workflows](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/caching-dependencies-to-speed-up-workflows)

Here is a sample `.github/workflows/iss-location.yml` that runs daily, appends the International Space Station location data into `iss-location.json`, and commits it to the repository.

```yaml
name: Log ISS Location Data Daily

on:
  schedule:
    # Runs at 12:00 UTC (noon) every day
    - cron: "0 12 * * *"
  workflow_dispatch: # Allows manual triggering

jobs:
  collect-iss-data:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v5

      - name: Fetch ISS location data
        run: | # python
          uv run --with requests python << 'EOF'
          import requests

          data = requests.get('http://api.open-notify.org/iss-now.json').text
          with open('iss-location.jsonl', 'a') as f:
              f.write(data + '\n')
          'EOF'

      - name: Commit and push changes
        run: | # shell
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git add iss-location.jsonl
          git commit -m "Update ISS position data [skip ci]" || exit 0
          git push
```

Tools:

- [GitHub CLI](https://cli.github.com/): Manage workflows from terminal
- [Super-Linter](https://github.com/github/super-linter): Validate code style
- [Release Drafter](https://github.com/release-drafter/release-drafter): Automate releases
- [act](https://github.com/nektos/act): Run actions locally

[![Github Actions CI/CD - Everything you need to know to get started](https://i.ytimg.com/vi_webp/mFFXuXjVgkU/sddefault.webp)](https://youtu.be/mFFXuXjVgkU
<youtube_summary>This video explains how to use GitHub Actions, a built-in CI/CD tool on GitHub, to automate code testing and delivery. CI/CD stands for continuous integration and continuous delivery, enabling automated testing to ensure code meets standards before automated delivery, thus speeding up updates and allowing developers to focus on coding.

Key terminology for GitHub Actions workflows is introduced: 
- Workflow YAML files define events (triggers), jobs, runners (environments), steps, and actions.
- An event, such as pushing new code, triggers the workflow.
- Jobs run on specified runners (e.g., Ubuntu, Windows, macOS containers hosted by GitHub or self-hosted).
- Steps include actions like checking out the code and running tools such as linters.

The video demonstrates creating a GitHub repository, adding a workflow YAML file under the directory `.github/workflows/` named `superlinter.yaml`, which triggers on push events to run a job called "superlint". This job runs on an Ubuntu runner and performs two steps: checking out the code and running the Super Linter, a tool that checks code against language-specific standards.

After committing the workflow file, the action automatically runs, indicated by a status icon. The video shows how to monitor the workflow’s progress and view detailed logs, illustrating how the linter checks the code and reports results.

Next, the video adds a Python file with deliberate linting errors (inconsistent spacing and formatting). Upon committing, the linter detects errors, providing line-by-line feedback. The presenter edits the code to fix the formatting issues according to linter suggestions, commits the changes, and demonstrates that the linter then passes successfully.

Additional features include viewing the history of workflow runs, filtering workflows, and using GitHub’s guided workflow setup and marketplace for pre-made workflow templates that can be customized.

The video encourages viewers to like and subscribe for more content on DevOps, programming, and IT topics.</youtube_summary>
)

- [How to handle secrets in GitHub Actions](https://youtu.be/1tD7km5jK70
<youtube_summary>Any GitHub action or user with the right access to your repository effectively has read access to all configured secrets. To minimize exposure, grant secrets the least privilege necessary. Secrets include personal access tokens, API tokens, and other sensitive authentication or authorization data. For example, if a secret doesn't need to be at the organization level, place it at the repository or environment level instead. Review your secrets by going to the repository's settings tab and clicking on "Secrets."</youtube_summary>
)
