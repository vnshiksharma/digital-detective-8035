# Mission 0 — GitHub Workspace Setup

## 1. Task / objective

Set up the development environment: verify that Python 3 and Git are installed, create the local project folder with the required directory structure, write the root README, create a public GitHub repository, connect the local repository to it, make an initial commit, and push to the `main` branch.

## 2. Work completed

- Verified Python 3 and Git installations and recorded their versions.
- Created the local project folder `digital-detective-8035` inside the workspace.
- Created all nine mission sub-folders plus the `terminal-practice` sub-directory.
- Wrote the root `README.md` with project title, introduction, mission index with links, topics covered, instructions for running the number converter, and a learning summary.
- Created a `.gitignore` for macOS metadata and Python cache files.
- Created a new **public** GitHub repository named `digital-detective-8035` under the account `vnshiksharma`.
- Initialised a local Git repository (`git init -b main`).
- Added the GitHub remote and pushed the initial commit.

## 3. Commands / tools used

```bash
# Check Python and Git versions
python3 --version
git --version

# Create directory structure
mkdir -p digital-detective-8035/{mission-00-setup,...}

# Initialise Git and connect to GitHub
git init -b main
git remote add origin https://github.com/vnshiksharma/digital-detective-8035.git
git add .
git commit -m "Set up Digital Detective mission structure"
git push -u origin main
```

## 4. My understanding

A **Git repository** is a folder tracked by Git. Git records every change made to the files inside it, stores those changes as commits, and lets you share the full history with others through a remote host such as GitHub.

The work is organised by mission so that each commit matches exactly one topic. This makes the commit history easy to read — you can tell at a glance which commit introduced the terminal notes and which introduced the Python converter. It also makes it easier to review or correct one mission without touching the others.

## 5. Difficulties faced

The git global `user.email` was not configured, so the first commit attempt would have failed with an identity error.

## 6. How I resolved them

Ran `git config --global user.email` and `git config --global user.name` to set the correct values before making any commit.

## 7. Evidence / files

| Item | Detail |
|------|--------|
| Python version | Python 3.14.7 |
| Git version | git version 2.55.0 |
| Operating system | macOS 27.2.1 (Build 26B131) |
| Repository URL | https://github.com/vnshiksharma/digital-detective-8035 |
| Visibility | Public |
| Root README | [README.md](../README.md) |
| .gitignore | [.gitignore](../.gitignore) |

Folders created:

```
digital-detective-8035/
├── .gitignore
├── README.md
├── mission-00-setup/README.md
├── mission-01-computer-basics/README.md
├── mission-02-terminal/README.md
│   └── terminal-practice/notes.txt, notes-backup-renamed.txt
├── mission-03-operating-system/README.md
├── mission-04-programs/README.md, hello.py
├── mission-05-numbers-data/README.md, number_converter.py
├── mission-06-git-github/README.md
├── mission-07-networking/README.md
└── mission-08-final-report/README.md
```

## 8. Commit details

| Field | Value |
|-------|-------|
| Commit message | `Set up Digital Detective mission structure` |
| Branch | `main` |
| Push status | Pushed successfully to GitHub |
