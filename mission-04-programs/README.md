# Mission 4 — How Programs Run

## 1. Task / objective

Write and run a simple Python program, then compare how compilers and interpreters work.

## 2. Work completed

- Created `hello.py` and ran it with Python 3.
- Recorded the actual output.
- Compared compilers and interpreters in a table with four criteria.

## 3. Commands / tools used

```bash
python3 hello.py
```

## 4. My understanding

### Task 4.1 — The Python Program

**File:** [`hello.py`](hello.py)

```python
print("Hello from Python")
```

**Command run:**

```bash
python3 hello.py
```

**Actual output:**

```
Hello from Python
```

The Python interpreter read the source file line by line and immediately executed each instruction. No separate compilation step was needed.

---

### Task 4.2 — Compiler vs Interpreter

| Criterion | Compiler | Interpreter |
|-----------|----------|-------------|
| **When translation/execution happens** | The entire source code is translated into machine code **before** the program runs | The source code is translated and executed **line by line at runtime** |
| **Typical output** | A standalone executable file (e.g. `.exe` on Windows, a binary on Linux) | No separate file; output appears directly while the program runs |
| **One example** | C (compiled with `gcc`); C++ (compiled with `g++`) | Python (run with `python3`); JavaScript (run by a browser or Node.js) |
| **One advantage** | The resulting program runs faster because translation is done only once, before execution | Easier to test and debug — you see results immediately without a compile step |

**Simple explanation:**

A compiler reads your entire program and translates it all into machine code before the program starts. The result is a separate file that runs very fast. An interpreter works differently — it reads your program one line at a time and executes each line immediately. Python uses an interpreter, which is why running `python3 hello.py` shows the output straight away without creating a separate binary. Compilers are good for performance-sensitive programs; interpreters are good for quick development and learning.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

| File | Description |
|------|-------------|
| [hello.py](hello.py) | Python program that prints `Hello from Python` |

Actual output when running `python3 hello.py`:

```
Hello from Python
```

## 8. Commit details

| Field | Value |
|-------|-------|
| Commit message | `Compare compilers and interpreters` |
| Branch | `main` |
| Push status | Pushed successfully to GitHub |
