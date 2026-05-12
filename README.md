# H4shmap

> A modern interactive terminal framework for building and executing powerful Nmap commands with ease.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Nmap](https://img.shields.io/badge/Nmap-Network%20Scanner-green?style=for-the-badge)
![CLI](https://img.shields.io/badge/Interface-CLI-black?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

---

# 📌 Overview

<img width="1034" height="457" alt="Capture d’écran 2026-05-12 à 17 29 55" src="https://github.com/user-attachments/assets/7a233002-a2fc-4c61-98d4-ccb7cfc352c1" />

**NmapFramework** is a Python-based interactive CLI made to simplify the use of Nmap through a beautiful and intuitive menu-driven interface.

Instead of remembering dozens of flags and command combinations, this framework lets you:

- Build scans interactively
- Save scan presets as shortcuts
- Launch advanced scans quickly
- Organize Nmap options by categories
- Execute commands directly from the terminal UI

---

# ✨ Features

## Scan Types
- SYN Scan | TCP Connect Scan | UDP Scan | (ACK / Window / FIN / NULL / Xmas Scans)
- SCTP Scans | IP Protocol Scan

## Host Discovery
- ICMP Discovery | TCP/UDP Ping | ARP Ping
- No-Ping Mode | DNS Control

## Port Management
- Top ports scanning | Full 65535 ports scan
- Custom port ranges | Fast scan mode

## Detection & Enumeration
- Service detection | OS fingerprinting | Aggressive detection
- Traceroute | NSE scripts support

## Evasion Techniques
- Packet fragmentation | MAC spoofing | Randomized hosts | Bad checksums
- Source port spoofing | Firewall bypass options

## 💾 Shortcuts System
- Save your commons scans | Load scans instantly
- Rename or delete presets | Auto-generated shortcut names

---

# ⚙️ Installation

## 1 — Clone the repository

```bash
git clone https://github.com/H4shme/H4shmap.git
cd H4shmap
```

## 2 — Install requirements

```bash
pip3 install -r requirements.txt
```

## 3 — Install Nmap

### Linux

```bash
sudo apt install nmap
```

### MacOS

```bash
brew install nmap
```

### Windows

Download:
https://nmap.org/download.html


# Dependencies

Required Python modules:

```txt
colorama
```

---

# 📁 Project Structure

```text
NmapFramework/
│
├── main.py
├── requirements.txt
├── nmap_shortcuts.json
└── README.md
```
---

# 🤝 Contributing

Contributions are welcome.

Feel free to:
- Fork the project
- Open pull requests
- Suggest improvements
- Report bugs

---

# ⚠️ Disclaimer

This tool is made for:
- Educational purposes
- Authorized security testing
- Ethical hacking environments

Do not use this framework against systems you do not own or have permission to test.

The author is not responsible for misuse.

---

# ⭐ Support

If you like this project:

- Leave a star ⭐
- Fork the repository
- Share it with others

---
