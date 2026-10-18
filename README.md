# 🔍 Python Multi-Threaded Port & Banner Scanner

A fast, lightweight TCP network reconnaissance tool built in Python using `socket` and `threading`. Designed for Red Team reconnaissance to quickly identify open ports and grab service banners on target hosts.

## 🚀 Features
- **Multi-Threaded Scanning:** Scans top 1,024 ports concurrently in seconds.
- **Banner Grabbing:** Identifies running services and versions on open TCP ports to help spot vulnerable entry points.
- **Zero External Dependencies:** Built purely with Python standard libraries (`socket`, `threading`, `datetime`).

## 🛠️ Usage
Run the script in your terminal (Kali Linux / Windows):
```bash
python3 scanner.py
