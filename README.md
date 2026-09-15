# 🔐 File Integrity Checker

A Python-based File Integrity Monitoring (FIM) tool that detects whether a file has been
tampered with, modified, or deleted — using cryptographic hashing.

---

## 📌 Overview

In cybersecurity, detecting unauthorized changes to critical system or configuration files
is a fundamental defensive control. This tool implements the core logic behind enterprise
FIM solutions such as **Wazuh**, **Tripwire**, and **AIDE**.

It works by generating cryptographic hash digests (**SHA-256** and **MD5**) for a file.
A hash acts as a unique digital fingerprint — even a single-byte change completely alters
the output. This fingerprint is stored as a trusted **baseline** in a JSON file along with
a timestamp.

---

## ⚙️ How It Works

1. **Baseline creation** — the tool hashes the target file(s) and saves the digests to `baseline.json`
2. **Integrity check** — on each run, it recalculates the current hash and compares it to the stored baseline

| Result | Meaning |
|---|---|
| ✅ **Unchanged** | Current hash matches the baseline |
| ⚠️ **Modified** | Hashes differ — original and current values are displayed for comparison |
| ❌ **Missing** | File no longer exists at its recorded path |

---

## ✨ Features

- SHA-256 and MD5 hash generation
- Persistent baseline stored in JSON with timestamps
- Monitors **multiple files** simultaneously
- Clear detection of Unchanged / Modified / Missing states
- Side-by-side hash comparison on modification
- No external dependencies — pure Python standard library

---

## 🚀 Usage

```bash
# Clone the repository
git clone https://github.com/Saqlain-Soc/file-integrity-checker.git
cd file-integrity-checker

# Run the tool
python file_integrity_checker.py
```

---

## 📸 Demo

### Baseline created
![Baseline](screenshots/01-baseline-created.png)

### File unchanged
![Unchanged](screenshots/02-unchanged.png)

### File modified
![Modified](screenshots/03-modified.png)

### File missing
![Missing](screenshots/04-missing.png)

---

## 🧠 Why This Matters

File Integrity Monitoring is a requirement in several security frameworks (PCI-DSS 11.5,
NIST CSF, CIS Controls). Attackers who gain access to a system frequently modify binaries,
configuration files, or log files to maintain persistence or cover their tracks. Hash-based
integrity checks make those modifications visible.

---

## 🛠️ Tech Stack

- Python 3
- `hashlib` — cryptographic hashing
- `json` — baseline persistence
- `os` / `datetime` — file handling and timestamps

---

## 📈 Future Improvements

- Directory-wide recursive monitoring
- Real-time watch mode
- Email / webhook alerting on change detection
- Log export for SIEM ingestion

---

## 👤 Author

**Saqlain Abbas**
Cybersecurity / SOC Analyst

---

## ⚠️ Disclaimer

This tool was built for educational and defensive security purposes.
