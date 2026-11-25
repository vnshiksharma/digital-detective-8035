# Mission 6 — Git and GitHub

## 1. Task / objective

Practise core Git workflow commands, create a new branch called `update-about`, add a "My Learning" section to the root README, push the branch to GitHub, and open a Pull Request from `update-about` to `main`.

## 2. Work completed

All four tasks completed: Git workflow commands practised and explained, `update-about` branch created and pushed, root README updated on that branch, Pull Request opened on GitHub, and a Git command glossary written.

## 3. Commands / tools used

```bash
git status
git add README.md
git commit -m "Add My Learning section to root README"
git log --oneline
git branch update-about
git checkout update-about
git push origin update-about
```

## 4. My understanding

### Task 6.1 — Git Workflow

**`git status`** — shows which files have been changed, which are staged (ready to commit), and which are untracked (not yet added to Git). It is the first command to run before making a commit to understand what will be included.

**`git add <file>`** — moves a changed file into the **staging area**. Only staged files are included in the next commit. This lets you choose exactly which changes to group together.

**Staging vs committing:**
- **Staging** (`git add`) is like putting items into a box before sealing it. You can add, remove, or check the box before closing it.
- **Committing** (`git commit`) seals the box and labels it with a message. The changes are now permanently recorded in the repository's history.

**`git commit -m "message"`** — creates a snapshot of all staged files with a descriptive message. The message should explain *what* changed and *why*.

**`git log`** — shows the commit history. Each commit shows its hash, author, date, and message. `git log --oneline` shows one line per commit.

---

### Task 6.2 — The `update-about` Branch

Starting from `main`:

```bash
git checkout -b update-about
# (edit root README.md — added "My Learning" section)
git add README.md
git commit -m "Add My Learning section to root README"
git push origin update-about
```

The root README was updated on the `update-about` branch. The `main` branch was not changed.

**My Learning section added to root README** (genuine takeaways from earlier missions):

> - Using `>>` appends to a file without overwriting, while `>` replaces the entire contents — a small difference that can cause permanent data loss if confused.
> - The OS assigns a unique PID to every running process, which is how it manages hundreds of programs at the same time without them interfering with each other.
> - Git's staging area is what makes commits precise — you can change five files but commit only three of them, keeping the history clean and meaningful.

---

### Task 6.3 — Pull Request

A Pull Request was opened on GitHub:

| Field | Detail |
|-------|--------|
| From branch | `update-about` |
| To branch | `main` |
| Title | `Add My Learning section to root README` |
| Description | Adds a genuine three-point learning summary to the root README, documenting key takeaways from Missions 2, 3, and 6. |
| Status | **Open (not merged)** — left unmerged per assignment instructions |

> The PR is left open and unmerged. The changes in `update-about` are therefore **not** in `main`. The branch and PR remain visible on GitHub.

---

### Task 6.4 — Git Command Glossary

| Command | Purpose |
|---------|---------|
| `git init` | Initialise a new empty Git repository in the current folder |
| `git status` | Show which files are changed, staged, or untracked |
| `git add <file>` | Stage a file (add it to the next commit) |
| `git commit -m "..."` | Save staged changes as a permanent snapshot with a message |
| `git log` | View the commit history (messages, hashes, authors, dates) |
| `git branch <name>` | Create a new branch; `git branch` with no argument lists branches |
| `git checkout <name>` | Switch to a different branch |
| `git push origin <branch>` | Upload local commits on a branch to the remote repository on GitHub |
| `git fetch` | Download new data from the remote without merging it into the local branch |
| `git pull` | Download and immediately merge remote changes into the current local branch |

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

All findings are documented in this README.  
The `update-about` branch and its Pull Request are visible at:  
`https://github.com/vnshiksharma/digital-detective-8035`

## 8. Commit details

| Field | Value |
|-------|-------|
| Commit message | `Complete Git and GitHub collaboration mission` |
| Branch | `main` |
| Push status | Pushed successfully to GitHub |
| Branch `update-about` | Created and pushed to GitHub |
| PR status | Open (unmerged) |
