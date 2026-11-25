# Mission 1 — Know Your Computer

## 1. Task / objective

Understand and explain the IPOS model (Input–Processing–Output–Storage), identify and classify hardware and software components, and describe three real-world computer-based systems.

## 2. Work completed

Completed all three tasks: IPOS analysis, hardware/software classification, and everyday computer systems.

## 3. Commands / tools used

No specific Terminal commands were required for this mission. Observations were made from the actual macOS machine.

## 4. My understanding

### Task 1.1 — IPOS Model: Searching for a Website

**Activity chosen:** Typing a search query in Google Chrome and receiving results.

| Stage | Description | Hardware / Component involved |
|-------|-------------|-------------------------------|
| **Input** | User types a query on the keyboard and presses Enter | Keyboard (input device) |
| **Processing** | The browser prepares an HTTP request; the CPU processes the keystrokes, runs Chrome, and handles the DNS lookup | CPU (Central Processing Unit), RAM |
| **Output** | The search results page is displayed on screen | Monitor / Display (output device) |
| **Storage** | The browser caches pages on disk; history is saved | SSD / Hard disk (secondary storage) |

The activity flows as follows: keystrokes travel from the keyboard → CPU reads them into RAM → CPU instructs the network adapter to send a DNS query → server responds → CPU processes the HTML → GPU renders it → the display shows the page → the browser writes cache data to the SSD.

---

### Task 1.2 — Hardware and Software

**Hardware examples (physical components):**

| Component | Type | Purpose |
|-----------|------|---------|
| MacBook keyboard | Input device | Sends characters and commands to the computer |
| MacBook display (Retina LCD) | Output device | Shows the visual interface to the user |
| Apple M-series SSD (926 GB) | Storage device | Stores the OS, apps, and user files permanently |
| Apple Silicon CPU / GPU | Processing unit | Executes all program instructions and renders graphics |
| RAM | Primary storage | Holds data and programs currently in use |

**Software examples and classification:**

| Software | Category | Purpose |
|----------|----------|---------|
| macOS 27.2 | Operating system | Manages hardware, runs programs, provides the user interface |
| Google Chrome | Application software | Lets the user browse the web |
| Discord | Application software | Voice, video, and text communication with others |
| Homebrew | Utility software | Manages installation and updates of command-line tools |
| Python 3.14 | Utility / language runtime | Runs Python programs and scripts |

---

### Task 1.3 — Everyday Computer Systems

**System 1: ATM (Automated Teller Machine)**

| Field | Detail |
|-------|--------|
| Main purpose | Allows bank customers to withdraw cash, check balances, and transfer money without visiting a teller |
| Input | User inserts a bank card and enters a PIN via the keypad |
| Output | Cash is dispensed and a receipt is printed |

**System 2: Smart Traffic-Light Controller**

| Field | Detail |
|-------|--------|
| Main purpose | Manages road traffic by changing signal timings in response to real-time vehicle flow |
| Input | Vehicle-detection sensors (magnetic loops or cameras) embedded in the road |
| Output | Red, amber, and green lights displayed to drivers |

**System 3: Self-Checkout Machine at a Supermarket**

| Field | Detail |
|-------|--------|
| Main purpose | Lets customers scan and pay for groceries without a cashier |
| Input | Barcode scanner reads product codes; touchscreen for payment selection |
| Output | Itemised bill shown on screen; receipt printed; payment terminal confirms transaction |

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

All findings are documented in this README. No additional files are required for this mission.

## 8. Commit details

| Field | Value |
|-------|-------|
| Commit message | `Complete computer basics and IPOS mission` |
| Branch | `main` |
| Push status | Pushed successfully to GitHub |
