# Information Security Ciphers in Python

A practical **Information Security** project that demonstrates classic cryptography algorithms in Python, including **Caesar Cipher**, **Playfair Cipher**, **Rail Fence Cipher**, **Vigenère Cipher**, and a simple **Stream Cipher (XOR-based)**.

This repository is useful for students, beginners, and cybersecurity learners who want to understand encryption and decryption step by step with interactive terminal programs.

## Keywords (SEO)

Information Security, Cryptography, Python Cipher Project, Caesar Cipher Python, Playfair Cipher Python, Rail Fence Cipher, Vigenere Cipher, Stream Cipher XOR, Encryption Decryption, Cybersecurity Learning

## Table of Contents

- [Project Overview](#project-overview)
- [Cipher Implementations](#cipher-implementations)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Example Usage](#example-usage)
- [Educational Note](#educational-note)
- [How to Make This Publicly Available](#how-to-make-this-publicly-available)
- [License](#license)

## Project Overview

This project contains command-line Python programs that perform:

- Text encryption
- Text decryption
- Tabular step-by-step output for learning
- Key-based and transposition-based cipher workflows

It is designed for academic demonstration and concept learning in cryptography.

## Cipher Implementations

### 1) Caesar Cipher
- File: `CeaserCipher.py`
- Type: Substitution cipher
- Key idea: Shifts letters by a fixed numeric key

### 2) Playfair Cipher
- File: `PlayfairCipher.py`
- Type: Digraph substitution cipher
- Key idea: Uses a 5x5 key matrix and pair-based transformation rules

### 3) Rail Fence Cipher
- File: `RailfnceCipher.py`
- Type: Transposition cipher
- Key idea: Rearranges text in zig-zag rail pattern

### 4) Stream Cipher (XOR)
- File: `StreamCipher.py`
- Type: Symmetric XOR-based stream encryption
- Key idea: Repeats key bytes and XORs with plaintext bytes

### 5) Vigenère Cipher
- File: `VigenereCipher.py`
- Type: Polyalphabetic substitution cipher
- Key idea: Uses repeating alphabetic key shifts

## Project Structure

```bash
.
├── CeaserCipher.py
├── PlayfairCipher.py
├── RailfnceCipher.py
├── StreamCipher.py
├── VigenereCipher.py
└── README.md
```

## Requirements

- Python 3.8+ (recommended)
- No external dependencies required

## How to Run

Run any script directly from terminal:

```bash
python3 CeaserCipher.py
python3 PlayfairCipher.py
python3 RailfnceCipher.py
python3 StreamCipher.py
python3 VigenereCipher.py
```

## Example Usage

- Enter input text when prompted.
- Provide cipher key (shift value, word key, or rail count depending on the algorithm).
- Select encryption (`e`) or decryption (`d`) where requested.
- Review generated tables and formatted output.

## Educational Note

These algorithms are classic and important for learning cryptography fundamentals. They are **not suitable for modern secure communication** in production systems.

## How to Make This Publicly Available

To publish and improve visibility on GitHub:

1. Create a new GitHub repository (public).
2. Push this project:

```bash
git init
git add .
git commit -m "Add classic cipher implementations"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

3. In repository settings:
   - Confirm visibility is **Public**
   - Add repository description with keywords like “Python cryptography ciphers”
   - Add topics: `cryptography`, `python`, `cipher`, `caesar-cipher`, `vigenere-cipher`, `cybersecurity`, `information-security`
   - Enable README display on repository home

4. Optional SEO improvements:
   - Add a social preview image
   - Add badges (Python version, license)
   - Keep README title and headings keyword-focused

## License

You can use an MIT License for open educational use. Add a `LICENSE` file if you want formal open-source licensing.
