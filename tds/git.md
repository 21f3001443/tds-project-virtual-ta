## Version Control: Git, GitHub

[Git](https://git-scm.com/) is the de facto standard for version control of software (and sometimes, data as well). It's a system that keeps track of changes you make to files and folders. It allows you to revert to a previous state, compare changes, etc. It's a central tool in any developer's workflow.

[GitHub](https://github.com/) is the most popular hosting service for Git repositories. It's a website that shows your code, allows you to collaborate with others, and provides many useful tools for developers.

Watch these introductory videos to learn the basics of Git and GitHub (98 min):

[![Git Tutorial for Beginners: Command-Line Fundamentals (30 min)](https://i.ytimg.com/vi_webp/HVsySz-h9r4/sddefault.webp)](https://youtu.be/HVsySz-h9r4
<youtube_summary>This video tutorial provides a comprehensive introduction to Git command line basics, covering what Git is, installation, and essential commands for managing local and remote repositories. It is useful for beginners new to version control, those familiar with other systems like SVN, and users accustomed to Git GUIs who want to learn command line operations.

Git is explained as a distributed version control system, unlike centralized systems such as SVN. In Git, every developer has a full copy of the repository locally, allowing offline access and acting as a backup if the central repository fails. Installation guidance directs users to the official Git website for downloads, followed by verifying installation with `git --version` and setting global configuration for username and email using `git config --global user.name` and `git config --global user.email`. Users are also shown how to check configurations with `git config --list` and access help manuals via `git help <command>` or `git <command> -h`.

Two common Git workflows are covered:

1. **Tracking an Existing Local Project**: Initialize a repository with `git init` inside the project directory, which creates a `.git` folder. Untracked files are managed using `.gitignore` to exclude files (e.g., personal preference files) from version control. The tutorial explains the three Git states—working directory, staging area, and committed files—and demonstrates adding files to staging with `git add`, removing them with `git reset`, committing with `git commit -m`, and viewing commit logs via `git log`.

2. **Cloning and Working with a Remote Repository**: Use `git clone <URL> <directory>` to copy a remote repository locally. Commands like `git remote -v` and `git branch -a` show remote info and all branches. After modifying files, users can view changes with `git diff`, stage and commit locally, then synchronize with the remote repository using `git pull` (to fetch updates) and `git push` (to upload commits).

Branching is introduced as a key workflow for feature development. Users create branches with `git branch <name>`, switch branches with `git checkout <name>`, and commit changes separately from the master branch. To share branches remotely, use `git push -u origin <branch>`. Once features are complete and tested, branches are merged back into master using `git checkout master`, `git pull`, and `git merge <branch>`, followed by pushing updates to the remote master branch. Branches can be deleted locally with `git branch -d <branch>` and remotely with `git push origin --delete <branch>`.

The video stresses the importance of detailed commit messages and explains common commands and workflows for efficient Git usage. It concludes by mentioning future tutorials on advanced Git topics like merge conflicts, undoing mistakes, tagging, rebasing, and cherry-picking, encouraging viewers to subscribe for updates and ask questions in the comments.</youtube_summary>
)

[![Git and GitHub for Beginners - Crash Course (68 min)](https://i.ytimg.com/vi_webp/RGOj5yH7evk/sddefault.webp)](https://youtu.be/RGOj5yH7evk
<youtube_summary>This video tutorial by Gwen from Faraday Academy provides a comprehensive introduction to Git and GitHub, covering their importance, key concepts, and practical usage.

**Introduction to Git and GitHub:**
- Git is a free, open-source version control system widely used by developers to track changes in code over time.
- Version control allows programmers to save multiple versions of their code, facilitating tracking changes, debugging, and reverting to previous versions.
- GitHub is a web-based platform for hosting Git repositories, enabling collaboration, project organization, and portfolio building.

**Key Terminology:**
- Directory (folder), terminal/command line (text interface for commands), CLI (command line interface).
- Code editor: specialized software for writing code, exemplified by Visual Studio Code.
- Repository (repo): a folder containing project files tracked by Git.
- Difference between Git (tool for tracking changes) and GitHub (online hosting service).

**Basic Git Commands Covered:**
- `git clone`: copies a remote repository to local machine.
- `git add`: stages changes to be tracked by Git.
- `git commit`: saves staged changes with a message.
- `git push`: uploads local commits to remote repository.
- `git pull`: downloads changes from remote repository.

**Using GitHub:**
- Sign up for GitHub and create a new repository (project).
- Create and edit files directly in GitHub’s online editor (e.g., README.md files written in Markdown).
- View commit history and changes visually.

**Setting Up Git Locally:**
- Git typically pre-installed on Mac/Linux; Windows users can install Git Bash recommended.
- Visual Studio Code is recommended as a free, cross-platform code editor with integrated terminal.
- Clone repositories from GitHub to local machine via terminal commands.

**Working Locally:**
- Use terminal commands (`git status`, `git add`, `git commit`) to track and save code changes.
- Use `git push` to upload changes to GitHub after authenticating with SSH keys.
- SSH keys allow secure authentication between local machine and GitHub by generating a public/private key pair; public key uploaded to GitHub.

**Initializing Local Repositories:**
- Use `git init` to create a new Git repository locally.
- Connect local repository to a remote GitHub repository via `git remote add origin <URL>`.
- Push local commits to the remote repository.

**Workflows:**
- GitHub interface workflow: editing files and committing changes directly on GitHub automatically stages and commits.
- Local workflow: editing code locally, staging with `git add`, committing, then pushing to GitHub.
- Pull requests (PRs) are used to request merging code from one branch to another, allowing code review and collaboration.

**Git Branching:**
- The master branch is the main branch by convention.
- Branching allows parallel development: new branches start identical to master but changes in branches are isolated.
- Feature branches help develop new features safely without affecting master.
- Hotfix branches address urgent bug fixes and merge back to master.
- Switch branches using `git checkout`; create new branches with `git checkout -b <branch-name>`.
- Use tab completion for branch names.
- Changes committed on one branch do not affect others until merged.
- Use `git diff` to view differences between branches or commits.
- Push branches to GitHub and create pull requests to merge them into master.

**Pull Requests and Code Review:**
- PRs enable team members to review, comment, and request changes before merging.
- Comments can be tied to specific lines of code.
- After approval, PRs are merged, and feature branches are typically deleted.

**Merge Conflicts:**
- Occur when different branches change the same lines.
- Must be resolved manually by editing conflicting files and removing conflict markers.
- After resolving conflicts, commit the changes to complete the merge.

**Undoing Changes:**
- `git reset` can unstage files or undo commits.
- `git reset HEAD~1` moves the HEAD pointer back one commit, undoing the last commit.
- `git reset --hard <commit-hash>` reverts files and commits to a previous state, discarding all changes after that commit.

**Forking Repositories:**
- Forking creates a personal copy of another user's repository.
- Forks allow users to freely make changes and experiment without affecting the original repo.
- Changes made in forks can be pushed to the forked repo and pull requests can be submitted to the original repository.
- Large projects may have multiple branches like dev, staging, and master for different environments.
- Feature branches merge into dev or master, which are long-lived branches, whereas feature branches are temporary.

**Summary:**
- The tutorial demonstrates creating repositories, cloning, committing, pushing, branching, merging, resolving conflicts, undoing changes, and forking repositories.
- It emphasizes best practices like descriptive commit messages, use of branches for features and fixes, and collaborative workflows using pull requests.
- Gwen encourages viewers to learn Git commands via the terminal for better understanding and proficiency.
- The tutorial concludes with an invitation to comment and follow Gwen’s additional coding content on her YouTube channel.

This comprehensive guide equips viewers with foundational knowledge and practical skills to effectively use Git and GitHub for version control and collaborative software development.</youtube_summary>
)

Essential Git Commands:

```bash
# Repository Setup
git init                   # Create new repo
git clone url              # Clone existing repo
git remote add origin url  # Connect to remote

# Basic Workflow
git status                 # Check status
git add .                  # Stage all changes
git commit -m "message"    # Commit changes
git push origin main       # Push to remote

# Branching
git branch                 # List branches
git checkout -b feature    # Create/switch branch
git merge feature          # Merge branch
git rebase main            # Rebase on main

# History
git log --oneline          # View history
git diff commit1 commit2   # Compare commits
git blame file             # Show who changed what
```

Best Practices:

1. **Commit Messages**

   ```bash
   # Good commit message format
   type(scope): summary

   Detailed description of changes.

   # Examples
   feat(api): add user authentication
   fix(db): handle null values in query
   ```

2. **Branching Strategy**

   - main: Production code
   - develop: Integration branch
   - feature/\*: New features
   - hotfix/\*: Emergency fixes

3. **Code Review**
   - Keep PRs small (<400 lines)
   - Use draft PRs for WIP
   - Review your own code first
   - Respond to all comments

Essential Tools

- [GitHub Desktop](https://desktop.github.com/): GUI client
- [GitLens](https://gitlens.amod.io/): VS Code extension
- [gh](https://cli.github.com/): GitHub CLI
- [pre-commit](https://pre-commit.com/): Git hooks
