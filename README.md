# 🔐 FILE INTEGRITY CHECKER

![Cybersecurity](https://img.shields.io/badge/Focus-Cybersecurity-blue)
![Python](https://img.shields.io/badge/Language-Python%203-yellow)
![Hashing](https://img.shields.io/badge/Crypto-SHA--256%20%7C%20MD5-red)
![Blue Team](https://img.shields.io/badge/Domain-Blue%20Team-navy)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

Detecting File Tampering, Modification & Deletion using Cryptographic Hashing

*PYTHON | FILE INTEGRITY MONITORING | DEFENSIVE SECURITY*

---

## 🔹 Project Overview

| **Field** | **Details** |
| :--- | :--- |
| 👨‍💻 **Developer** | **Saqlain Abbas** |
| 🧪 **Project Type** | **Security Tool Development** |
| 🎯 **Category** | **File Integrity Monitoring (FIM)** |
| 🐍 **Language** | **Python 3** |
| 🔐 **Algorithms** | **SHA-256, MD5** |
| 💾 **Storage** | **JSON Baseline (Persistent)** |
| 📌 **Domain** | **Blue Team / Defensive Security** |
| ✅ **Status** | **Completed** |

---

## 1. ⚠️ Liability Disclaimer

This tool was developed strictly for **educational and defensive security purposes**. It performs read-only hashing operations on files explicitly specified by the user. It does not modify, transmit, or exfiltrate any data. Use it only on systems you own or are authorized to monitor.

---

## 2. 📖 Introduction

In cybersecurity, detecting **unauthorized changes to critical system or configuration files** is a fundamental defensive control. Attackers who gain access to a system frequently modify binaries, configuration files, or log files to maintain persistence or cover their tracks.

This project implements the **core logic behind enterprise File Integrity Monitoring solutions** such as Wazuh, Tripwire, and AIDE — from scratch, in Python.

The tool generates cryptographic hash digests for a file. A hash acts like a **unique digital fingerprint** — even a single-byte change completely alters the output. This fingerprint is stored as a trusted **baseline**, and every subsequent check compares the file's current state against it.

---

## 🛠️ 3. Tech Stack

| **Component** | **Purpose** |
| :--- | :--- |
| 🐍 **Python 3** | Core application logic |
| 🔐 **hashlib** | SHA-256 and MD5 hash generation |
| 💾 **json** | Persistent baseline storage |
| 📁 **os** | File existence checks and path handling |
| 🕐 **datetime** | Baseline timestamping |

> **Zero external dependencies** — built entirely on the Python standard library.

---

## ⚙️ 4. How It Works

### 4.1 Baseline Creation

The tool reads the target file, computes its **SHA-256** and **MD5** digests, and writes them to `baseline.json` along with the file path and a timestamp. This becomes the trusted reference state.

### 4.2 Integrity Verification

On every run, the tool recalculates the file's current hash and compares it against the stored baseline value.

| **State** | **Condition** | **Output** |
| :---: | :--- | :--- |
| ✅ **UNCHANGED** | Current hash matches baseline | File integrity verified |
| ⚠️ **MODIFIED** | Current hash differs from baseline | Original and current hashes displayed side by side |
| ❌ **MISSING** | File no longer exists at recorded path | Deletion / relocation flagged |

### 4.3 Multi-File Monitoring

The tool supports monitoring **multiple files simultaneously**, maintaining all baselines in a single persistent JSON record that survives across sessions.

---

## 🚀 5. Installation & Usage

```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/file-integrity-checker.git

# Navigate into the project directory
cd file-integrity-checker

# Run the tool
python file_integrity_checker.py
```

> **Requirements:** Python 3.6 or higher. No `pip install` needed.

---

## 📸 6. Evidence Collected

### E01 — Baseline Creation

The tool computes SHA-256 and MD5 digests for the target file and stores them in `baseline.json`.

![Baseline Created](screenshots/01-baseline-created.png)

---

### E02 — Unchanged File Detection

The integrity check is re-run with no modifications made. The recalculated hash matches the baseline.

![Unchanged](screenshots/02-unchanged.png)

---

### E03 — Modified File Detection

The file content is altered. The recalculated hash no longer matches, and both hash values are displayed for comparison.

![Modified](screenshots/03-modified.png)

---

### E04 — Missing File Detection

The file is removed from its recorded path. The tool flags the file as missing.

![Missing](screenshots/04-missing.png)

---

## ⚠️ 7. Security Significance

| **#** | **Scenario** | **Real-World Relevance** | **Severity** |
| :---: | :--- | :--- | :---: |
| 01 | **Unauthorized binary modification** | Attacker replaces a system binary to establish persistence | <span style="color:red">●</span> **High** |
| 02 | **Configuration file tampering** | Security settings silently weakened or disabled | <span style="color:red">●</span> **High** |
| 03 | **Log file deletion** | Attacker removes evidence to cover their tracks | <span style="color:orange">●</span> **Medium** |
| 04 | **Unexpected file removal** | Critical data loss or sabotage | <span style="color:orange">●</span> **Medium** |

### 🔑 Severity Key

<span style="color:red">●</span> **High**    <span style="color:orange">●</span> **Medium**    <span style="color:green">●</span> **Low**

---

## 🏢 8. Real-World Context

This tool replicates the detection logic used by production FIM solutions:

| **Solution** | **Type** |
| :--- | :--- |
| 🛡️ **Wazuh** | Open-source SIEM / XDR with built-in FIM module |
| 🔍 **Tripwire** | Enterprise file integrity and change management |
| 🐧 **AIDE** | Advanced Intrusion Detection Environment (Linux) |

File Integrity Monitoring is also a **compliance requirement** under several frameworks:

* **PCI-DSS** — Requirement 11.5
* **NIST Cybersecurity Framework** — Detect (DE.CM)
* **CIS Controls** — Control 3 (Data Protection)

---

## 🛡️ 9. Recommendations for Production Use

* Monitor **critical system directories** rather than individual files only
* Store the baseline in a **write-protected or offline location** to prevent tampering
* Schedule integrity checks via **cron** or **Task Scheduler** for continuous coverage
* Forward detection results to a **SIEM** for centralized alerting
* Investigate every **MODIFIED** result — legitimate changes should be documented and re-baselined
* Prefer **SHA-256** over MD5 for security-critical verification; MD5 is retained here for legacy comparison only

---

## 📈 10. Future Improvements

* [ ] Recursive directory-wide monitoring
* [ ] Real-time watch mode using filesystem event hooks
* [ ] Email / webhook alerting on change detection
* [ ] Structured log export for SIEM ingestion
* [ ] Command-line argument support for automation
* [ ] Baseline encryption to prevent tampering

---

## ✅ 11. Conclusion

Building this tool from scratch gave me a much clearer understanding of what actually happens under the hood when a **FIM alert fires in a SIEM**. Rather than treating file integrity monitoring as a black box, I implemented the full detection cycle — baseline creation, hash recalculation, state comparison, and result classification.

The project demonstrates practical application of **cryptographic hashing, persistent state management, and defensive detection logic** — all core competencies for a SOC analyst or security engineer.

---

## 📊 12. Project Summary

| **Category** | **Details** |
| :--- | :--- |
| **Project** | File Integrity Checker |
| **Focus** | File Integrity Monitoring (FIM) |
| **Language** | Python 3 |
| **Algorithms** | SHA-256, MD5 |
| **Detection States** | Unchanged / Modified / Missing |
| **Baseline Storage** | JSON (persistent) |
| **Multi-File Support** | ✅ Yes |
| **External Dependencies** | None |
| **Status** | **Completed** |

---

## 👤 Author

### Saqlain Abbas

**🔐 Cybersecurity / SOC Analyst**

> `Learning → Building → Detecting → Defending`

This repository forms part of my practical cybersecurity learning portfolio and documents my hands-on security tool development.

<p align="center">
  <a href="www.linkedin.com/in/saqlain-abbas-a61b59414">
    <img src="https://img.shields.io/badge/🔵_LinkedIn-Professional%20Profile-0A66C2?style=for-the-badge" />
  </a>
  &nbsp;
  <a href="https://github.com/Saqlain-Soc/file-integrity-checker">
    <img src="https://img.shields.io/badge/⚫_GitHub-Security%20Projects-181717?style=for-the-badge" />
  </a>
</p>

---
