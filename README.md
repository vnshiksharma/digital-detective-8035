# Digital Detective — Diwali Independent Learning Assignment

**Repository:** `digital-detective-8035`  
**GitHub:** [vnshiksharma/digital-detective-8035](https://github.com/vnshiksharma/digital-detective-8035)

## Introduction

This repository documents the Digital Detective Diwali Assignment, a mission-based independent learning project. Each mission covers a core concept in computing — from hardware basics and the terminal to operating systems, programming, number systems, Git, and networking. All work was performed and recorded using real commands and actual observations on a macOS machine.

## Mission Index

| # | Mission | Link |
|---|---------|------|
| 0 | GitHub Workspace Setup | [mission-00-setup/README.md](mission-00-setup/README.md) |
| 1 | Know Your Computer | [mission-01-computer-basics/README.md](mission-01-computer-basics/README.md) |
| 2 | Terminal and File Management | [mission-02-terminal/README.md](mission-02-terminal/README.md) |
| 3 | Operating System | [mission-03-operating-system/README.md](mission-03-operating-system/README.md) |
| 4 | How Programs Run | [mission-04-programs/README.md](mission-04-programs/README.md) |
| 5 | Number Systems, Python and Text Encoding | [mission-05-numbers-data/README.md](mission-05-numbers-data/README.md) |
| 6 | Git and GitHub | [mission-06-git-github/README.md](mission-06-git-github/README.md) |
| 7 | Computer Networks | [mission-07-networking/README.md](mission-07-networking/README.md) |
| 8 | Final Review and Submission | [mission-08-final-report/README.md](mission-08-final-report/README.md) |

## Topics Explored

- IPOS model, hardware, software classification
- Terminal commands and file management (macOS/zsh)
- Operating system responsibilities, processes, paths, permissions
- Compilers vs interpreters; running Python programs
- Number systems: binary, decimal, hexadecimal; ASCII and UTF-8
- Git workflow: staging, committing, branching, pull requests
- Networking: LAN/WAN/DNS, packet switching, client-server model

## Running the Number Converter

```bash
cd mission-05-numbers-data
python3 number_converter.py
```

You will be prompted to enter a decimal integer. The program prints its binary and hexadecimal equivalents.

## Learning Summary

Through this assignment I practised real Terminal commands, understood how an operating system manages processes and files, wrote and ran Python programs, performed number-system conversions by hand and in code, and practised the full Git workflow including branching and pull requests.

## My Learning

Working through Missions 0–6 taught me several things that surprised me:

- **`>>` vs `>`** — Using `>>` appends to a file without erasing what is already there, while `>` replaces the entire contents. I learned this during Mission 2 when practising file edits in the terminal. Getting these mixed up would silently delete work.
- **Process IDs (PIDs)** — The operating system assigns a unique PID to every running program. This is how it manages hundreds of processes at the same time — each one has a unique number so the OS can pause, resume, or stop exactly the right one. I observed this in Mission 3 when inspecting the running process list.
- **Git staging area** — Git's staging area (the "index") means you can change many files but commit only the ones you choose. This keeps the commit history meaningful. I had assumed `git commit` automatically included all changed files, but it only includes what you have staged with `git add`.

## Commit Note

Each mission was documented and committed separately with a meaningful commit message, so the commit history shows the progress through the assignment step by step.
