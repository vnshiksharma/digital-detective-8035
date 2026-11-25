# Mission 6 — Git and GitHub

## 1. Task / objective

Understand version control, practise staging and committing changes, create a branch called `update-about`, add a "My Learning" section to the root README, open a Pull Request from `update-about` into `main`, and explain the collaboration workflow.

## 2. Work completed

- Practised and documented the core Git workflow commands (`status`, `add`, `commit`, `log`).
- Created branch `update-about` from `main`.
- Added a genuine "My Learning" section to the root README on that branch.
- Staged, committed, and pushed the branch to GitHub.
- Created Pull Request #1 on GitHub (`update-about` → `main`).
- Reviewed the changed file in the PR diff.
- Documented the post-merge steps (what to run after a merge).
- Written a Git command glossary.

## 3. Commands / tools used

```bash
# Task 6.1 — workflow inspection
git status
git add mission-06-git-github/README.md
git commit -m "Complete Git and GitHub collaboration mission"
git log --oneline

# Task 6.2 — branching
git checkout -b update-about
# (edited README.md to add My Learning section)
git status
git add README.md
git commit -m "Add My Learning section to root README"
git push origin update-about

# Task 6.3 — after PR merge (steps to run if instructor requires merge)
git checkout main
git pull origin main

# Task 6.4 — reference commands
git init
git branch
git checkout <branch>
git push origin <branch>
git fetch
git pull
```

## 4. My understanding

---

### Task 6.1 — Basic Git Workflow

The table below explains each Git operation **in my own words**, matching the actual commands run during this mission.

| Git operation | What it does in my own words |
|---------------|------------------------------|
| **Check repository status** (`git status`) | Shows which files have been changed since the last commit, which of those are staged (ready to go into the next commit), and which are untracked (not yet known to Git). It is the first command I run before staging anything, so I know exactly what has changed. |
| **Stage selected changes** (`git add <file>`) | Moves a specific changed file into the **staging area** (also called the index). Only staged files are included in the next commit. This lets me choose exactly which changes belong together in one snapshot — I can change ten files but commit only three. |
| **Create a commit** (`git commit -m "..."`) | Seals the staging area into a permanent snapshot with a short description. The snapshot is stored in the repository history with a unique hash. After a commit the staging area is empty again. |
| **View commit history** (`git log --oneline`) | Lists every commit made so far, newest first, showing the short hash and message. It is how I check that the right commits were made and in the right order. |

**Difference between staging and committing:**

> Staging (`git add`) is like putting items into a box before sealing it. I can add more items, remove some, or look inside before closing the lid. Committing (`git commit`) seals the box, labels it, and stores it on the shelf permanently. I cannot change what is inside a commit once it is made (without rewriting history, which is discouraged).

---

### Task 6.2 — The `update-about` Branch

**Steps performed:**

```bash
git checkout -b update-about
```

This created a new branch starting from the current state of `main` and switched to it immediately.

The root `README.md` was then edited to add a "My Learning" section. The actual content added:

```
## My Learning

- **`>>` vs `>`** — Using `>>` appends to a file without erasing what is already
  there, while `>` replaces the entire contents. Getting these mixed up would
  silently delete work.
- **Process IDs (PIDs)** — The operating system assigns a unique PID to every
  running program so it can pause, resume, or stop exactly the right one.
- **Git staging area** — Git's staging area means you can change many files but
  commit only the ones you choose, keeping the history meaningful.
```

**Actual `git status` output after editing README.md (observed on `update-about`):**

```
On branch update-about
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)

        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

**Commands run to stage, commit, and push:**

```bash
git add README.md
git commit -m "Add My Learning section to root README"
git push origin update-about
```

**Actual commit that was created (`git show --stat HEAD` on `update-about`):**

```
commit 98e2579db929ec3dd2a6daf028fe0dcb6bd8895d
Author: Vanshika <vanshikasharmajs08065@gmail.com>
Date:   Wed Nov 25 23:35:22 2026 +0530

    Add My Learning section to root README

 README.md | 8 ++++++++
 1 file changed, 8 insertions(+)
```

---

### Task 6.3 — Pull Request

**What a branch is:**

A branch is a separate, independent line of development inside the same repository. When I create `update-about`, I get my own copy of the files to work on. Changes made there do not affect `main` until they are explicitly merged. Branches let me experiment or work on a feature safely without breaking the main project.

**What a Pull Request is:**

A Pull Request (PR) is a request made on GitHub to merge one branch into another. It shows exactly which lines were added, removed, or changed (the "diff"), lets team members leave comments or suggest edits, and records the decision to merge. It is the standard way teams review each other's work before it reaches the main branch.

**Why branches and PRs are useful when people work on the same project:**

If two people edited `main` directly at the same time, their changes would conflict. Branches let each person work in isolation. The PR is then the review checkpoint — the team reads the changes, discusses them, and approves before anything reaches the shared main branch. This prevents untested code from breaking the project for everyone.

---

**PR details (actual):**

| Field | Detail |
|-------|--------|
| PR number | #1 |
| URL | https://github.com/vnshiksharma/digital-detective-8035/pull/1 |
| From branch | `update-about` |
| Into branch | `main` |
| Title | Add My Learning section to root README |
| Changed file | `README.md` (+8 lines) |
| Status | **Open (not merged)** |

The assignment says: *"Merge the PR only if your instructor has asked you to complete the merge."* No instructor instruction to merge was given, so the PR is left **open and unmerged**. The changes in `update-about` are therefore **not** currently in `main`.

**Step 6 — Post-merge steps (to run if the instructor requires the merge):**

If the instructor asks for the PR to be merged, the steps after merging on GitHub are:

```bash
git checkout main        # switch back to the main branch locally
git pull origin main     # download the merged commit from GitHub to the local machine
```

This brings the "My Learning" content from `update-about` onto the local `main` branch.

---

### Task 6.4 — Git Command Glossary

| Command | One-line explanation in my own words |
|---------|--------------------------------------|
| `git init` | Initialise a new empty Git repository in the current folder — creates the hidden `.git` directory where all history is stored |
| `git status` | Show which files have changed, which are staged, and which Git does not yet know about |
| `git add <file>` | Stage a file — move its changes into the area that will be included in the next commit |
| `git commit -m "..."` | Save all staged changes as a permanent, labelled snapshot in the repository history |
| `git log` | View the full commit history — each entry shows the hash, author, date, and message |
| `git branch <name>` / `git branch` | Create a new branch with the given name; running it without a name lists all existing branches |
| `git checkout <branch>` | Switch the working directory to a different branch (or use `git switch <branch>` in modern Git) |
| `git push origin <branch>` | Upload local commits on the named branch to the remote repository on GitHub |
| `git fetch` | Download new commits and branches from the remote without changing any local files |
| `git pull` | Download remote changes **and** immediately merge them into the current local branch (`fetch` + `merge` in one step) |

## 5. Difficulties faced

The `update-about` branch commit happened after several mission commits were already on `main`. I had to make sure I created the branch from `main` correctly so the PR diff only showed the README change and not any other mission files.

## 6. How I resolved them

Used `git checkout -b update-about` while on `main` so the branch started from the correct point. Staged only `README.md` with `git add README.md` to keep the commit focused.

## 7. Evidence / files

| Item | Detail |
|------|--------|
| Branch `update-about` | https://github.com/vnshiksharma/digital-detective-8035/tree/update-about |
| Pull Request #1 (open) | https://github.com/vnshiksharma/digital-detective-8035/pull/1 |
| Commit on `update-about` | `98e2579` — Add My Learning section to root README |
| Root README (with My Learning) | [README.md](../README.md) on `update-about` branch |

## 8. Commit details

| Field | Value |
|-------|-------|
| Mission 6 README commit message | `Complete Git and GitHub collaboration mission` |
| Branch | `main` |
| `update-about` commit message | `Add My Learning section to root README` |
| `update-about` push status | Pushed to GitHub |
| PR status | **Open, not merged** |
| All changes pushed | ✅ Yes |
