# Mission 5 — Number Systems, Python and Text Encoding

## 1. Task / objective

Perform manual number-system conversions (decimal ↔ binary, binary → hexadecimal), verify them with Python built-in functions, build a number converter program, and explain text encoding (ASCII and UTF-8).

## 2. Work completed

All four tasks completed: manual conversions (with working shown), Python verification, number converter program created and tested with four positive numbers, and text encoding explained.

## 3. Commands / tools used

```bash
python3 number_converter.py   # tested with inputs 13, 255, 42, 100
python3 -c "..."              # inline Python for verification
```

## 4. My understanding

### Task 5.1 — Manual Conversions (with working)

---

**1. Decimal 13 → Binary**

| Step | Division | Quotient | Remainder |
|------|----------|----------|-----------|
| 1 | 13 ÷ 2 | 6 | **1** |
| 2 | 6 ÷ 2 | 3 | **0** |
| 3 | 3 ÷ 2 | 1 | **1** |
| 4 | 1 ÷ 2 | 0 | **1** |

Read remainders bottom-up → **1101**

---

**2. Decimal 25 → Binary**

| Step | Division | Quotient | Remainder |
|------|----------|----------|-----------|
| 1 | 25 ÷ 2 | 12 | **1** |
| 2 | 12 ÷ 2 | 6 | **0** |
| 3 | 6 ÷ 2 | 3 | **0** |
| 4 | 3 ÷ 2 | 1 | **1** |
| 5 | 1 ÷ 2 | 0 | **1** |

Read remainders bottom-up → **11001**

---

**3. Binary 1010 → Decimal**

| Bit position | 2³ | 2² | 2¹ | 2⁰ |
|-------------|----|----|----|----|
| Bit value   |  1 |  0 |  1 |  0 |
| Contribution | 8 |  0 |  2 |  0 |

8 + 0 + 2 + 0 = **10**

---

**4. Binary 1101 → Decimal**

| Bit position | 2³ | 2² | 2¹ | 2⁰ |
|-------------|----|----|----|----|
| Bit value   |  1 |  1 |  0 |  1 |
| Contribution | 8 |  4 |  0 |  1 |

8 + 4 + 0 + 1 = **13**

---

**5. Hexadecimal A → Decimal**

Hex digit A = **10** in decimal (by definition: A=10, B=11, C=12, D=13, E=14, F=15).

---

**6. Hexadecimal 1F → Decimal**

| Hex digit | Position | Calculation |
|-----------|----------|-------------|
| 1 | 16¹ | 1 × 16 = 16 |
| F | 16⁰ | 15 × 1 = 15 |

16 + 15 = **31**

---

**7. Binary 1111 → Hexadecimal**

Group bits into nibbles of 4 (from right): `1111`

| Nibble | Binary | Hex |
|--------|--------|-----|
| 1111 | = 8+4+2+1 = 15 | F |

Binary 1111 = Hex **F**

---

### Task 5.2 — Python Verification

All conversions verified with Python built-in functions:

```python
>>> bin(13)
'0b1101'

>>> bin(25)
'0b11001'

>>> int('1010', 2)
10

>>> int('1101', 2)
13

>>> hex(13)
'0xd'

>>> hex(25)
'0x19'

>>> int('1F', 16)
31

>>> hex(int('1111', 2))
'0xf'   # F in uppercase
```

All manual results match the Python output. ✓

---

### Task 5.3 — Number Converter Program

**File:** [`number_converter.py`](number_converter.py)

```python
try:
    decimal_input = input("Enter a decimal integer: ")
    number = int(decimal_input)
    if number < 0:
        print("Please enter a positive integer.")
    else:
        binary_result = bin(number)
        hex_result = hex(number)
        print(f"Decimal     : {number}")
        print(f"Binary      : {binary_result}  ({binary_result[2:]})")
        print(f"Hexadecimal : {hex_result}  ({hex_result[2:].upper()})")
except ValueError:
    print("Invalid input. Please enter a whole number.")
```

**Test results (actual output from running `python3 number_converter.py`):**

| Input | Decimal | Binary | Hexadecimal |
|-------|---------|--------|-------------|
| 13 | 13 | 0b1101 (1101) | 0xd (D) |
| 255 | 255 | 0b11111111 (11111111) | 0xff (FF) |
| 42 | 42 | 0b101010 (101010) | 0x2a (2A) |
| 100 | 100 | 0b1100100 (1100100) | 0x64 (64) |

---

### Task 5.4 — Text Encoding

| Item | Value |
|------|-------|
| ASCII code of uppercase A | 65 (verified: `ord('A')` → 65) |
| ASCII code of lowercase a | 97 (verified: `ord('a')` → 97) |

**Why encoding standards are needed:**

Computers store everything as numbers (bits). An encoding standard defines which number represents which character. Without a shared standard, text created on one computer would appear as gibberish on another because each system might map number 65 to a different symbol.

**ASCII:** American Standard Code for Information Interchange. It uses 7 bits and defines 128 characters — the English alphabet (upper and lower case), digits 0–9, punctuation, and control characters. It was designed in the 1960s and is still the foundation of modern encoding.

**UTF-8:** A superset of ASCII that can represent over one million characters from all writing systems (Latin, Devanagari, Chinese, Arabic, emoji, etc.). It uses 1 byte for the first 128 characters (identical to ASCII) and 2–4 bytes for everything else. This makes it backwards-compatible and very efficient for English text.

**Character outside basic ASCII:**

The Indian Rupee symbol **₹** (U+20B9) is not in ASCII (which only covers 0–127). In Python:

```python
>>> ord('₹')
8377
>>> chr(8377)
'₹'
```

It requires 3 bytes in UTF-8 encoding. ASCII cannot represent it at all, which is why UTF-8 (or another Unicode encoding) must be used for multilingual text.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

| File | Description |
|------|-------------|
| [number_converter.py](number_converter.py) | Python program; tested with inputs 13, 255, 42, and 100 |

## 8. Commit details

| Field | Value |
|-------|-------|
| Commit message | `Build number converter and practise data representation` |
| Branch | `main` |
| Push status | Pushed successfully to GitHub |
