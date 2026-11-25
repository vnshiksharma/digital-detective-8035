# Mission 2 — Terminal and File Management

## 1. Task / objective

Practise core Terminal commands for navigating the file system, creating and managing files, using flags and pipes, and understanding the package manager available on macOS.

## 2. Work completed

All four tasks completed: basic Terminal operations, file changes inside `terminal-practice/`, flags and pipes demonstration, and Homebrew inspection.

## 3. Commands / tools used

```bash
# Navigation and inspection
pwd
ls
ls -l
ls -lah
cd ..

# Directory and file creation
mkdir test-dir
touch notes.txt

# File content and copying
printf 'First line\n' > notes.txt
printf 'Second line\n' >> notes.txt
cat notes.txt
cp notes.txt notes-backup.txt
mv notes-backup.txt notes-backup-renamed.txt

# Pipes
ls -lah | head -n 5

# Homebrew
brew --version
brew list
```

## 4. My understanding

### Task 2.1 — Basic Terminal Operations

| Command | Purpose | Observed result |
|---------|---------|----------------|
| `pwd` | Print working directory — shows the full path of the current folder | `/Users/vanshikasharma/.gemini/antigravity/scratch/digital-detective-8035/mission-02-terminal/terminal-practice` |
| `ls` | List files and folders in the current directory | Shows `notes.txt` and `notes-backup-renamed.txt` |
| `ls -l` | Detailed listing — shows permissions, owner, size, date | Each entry shows `-rw-r--r--`, owner `vanshikasharma`, size, and timestamp |
| `cd ..` | Move up one directory level | Moved from `terminal-practice/` up to `mission-02-terminal/` |
| `mkdir` | Create a new directory | Creates a folder at the given path |
| `touch notes.txt` | Create a new empty file (or update its timestamp) | Created `notes.txt` |
| `cp notes.txt notes-backup.txt` | Copy a file | Created an identical `notes-backup.txt` |
| `mv notes-backup.txt notes-backup-renamed.txt` | Rename (or move) a file | `notes-backup.txt` became `notes-backup-renamed.txt` |
| `cat notes.txt` | Display the contents of a file | Printed both lines to the terminal |

---

### Task 2.2 — File Changes inside `terminal-practice/`

**Commands run in order:**

```bash
cd mission-02-terminal/terminal-practice/
touch notes.txt
printf 'First line\n' > notes.txt
printf 'Second line\n' >> notes.txt
cat notes.txt
cp notes.txt notes-backup.txt
mv notes-backup.txt notes-backup-renamed.txt
ls -lah
```

**Actual output of `cat notes.txt`:**

```
First line
Second line
```

**Actual output of `ls -lah`:**

```
total 16
drwxr-xr-x@ 4 vanshikasharma  staff   128B Nov 25 23:26 .
drwxr-xr-x@ 3 vanshikasharma  staff    96B Nov 25 23:26 ..
-rw-r--r--@ 1 vanshikasharma  staff    23B Nov 25 23:26 notes-backup-renamed.txt
-rw-r--r--@ 1 vanshikasharma  staff    23B Nov 25 23:26 notes.txt
```

**Key concepts:**

- `>` **replaces** the file contents. `>>` **appends** without deleting the existing text.
- `cp` makes a **copy** — both original and copy exist afterwards.
- `mv` **moves or renames** — the original name is gone; only the new name exists.
- `pwd` shows exactly where you are, which prevents mistakes when running destructive commands.
- `ls` confirms whether a file was actually created, copied, or renamed.

---

### Task 2.3 — Flags and Pipes

```bash
# Plain listing
ls

# Detailed listing (permissions, size, date)
ls -l

# Include hidden files, human-readable sizes
ls -lah

# Pipe the detailed listing into head to see only the first 5 lines
ls -lah | head -n 5
```

**Actual output of `ls -lah | head -n 5` (inside `terminal-practice/`):**

```
total 16
drwxr-xr-x@ 4 vanshikasharma  staff   128B Nov 25 23:26 .
drwxr-xr-x@ 3 vanshikasharma  staff    96B Nov 25 23:26 ..
-rw-r--r--@ 1 vanshikasharma  staff    23B Nov 25 23:26 notes-backup-renamed.txt
-rw-r--r--@ 1 vanshikasharma  staff    23B Nov 25 23:26 notes.txt
```

A **pipe** (`|`) sends the output of one command directly into the input of the next. Here, `ls -lah` produces many lines and `head -n 5` keeps only the first five, which is useful when a folder contains many files.

---

### Task 2.4 — Package Manager (Homebrew)

Homebrew is installed on this machine.

```bash
brew --version
# Output: Homebrew 7.0.9

brew list
```

**Packages managed by Homebrew (first 20 shown):**

```
ca-certificates  dav1d  ffmpeg  gettext  git  json-c  lame  libunistring
libvmaf  libvpx  mpg123  openssl@4  opus  pcre2  sdl2-compat  sdl3
svt-av1  x264  x265  xz
```

**What a package manager does:** A package manager is a tool that lets you install, update, and remove software from a central catalogue using simple commands. Homebrew does this for macOS command-line tools and apps. Instead of downloading an installer manually, you run `brew install <package>` and Homebrew handles downloading, verifying, and placing the files in the right location. No packages were installed or removed during this mission.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

| File | Description |
|------|-------------|
| [terminal-practice/notes.txt](terminal-practice/notes.txt) | File created during the practice task; contains two lines |
| [terminal-practice/notes-backup-renamed.txt](terminal-practice/notes-backup-renamed.txt) | Renamed copy of notes.txt; contains the same two lines |

## 8. Commit details

| Field | Value |
|-------|-------|
| Commit message | `Complete Terminal and file management mission` |
| Branch | `main` |
| Push status | Pushed successfully to GitHub |
