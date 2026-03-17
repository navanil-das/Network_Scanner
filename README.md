# 🔍 Python Network Scanner

A multithreaded network scanner built in Python that detects open ports and identifies running services using banner grabbing. Designed as a lightweight, modular alternative to tools like Nmap.

---

## 🚀 Features

* ⚡ Multithreaded TCP port scanning
* 🎯 Custom port range support
* 🔎 Service detection via banner grabbing
* 💻 Command-line interface (CLI)
* 📁 JSON export of scan results
* 🧠 Basic OS detection using TTL

---

## 🏗️ Project Structure

```
network-scanner/
│
├── src/
│   ├── scanner.py          # core scanning logic
│   ├── banner_grabber.py   # service detection
│   └── utils.py            # helpers (port parsing, OS detection)
│
├── results/
│   └── scan_results.json   # saved outputs
│
├── main.py                 # CLI entry point
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/network-scanner.git
cd network-scanner
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python main.py --target 192.168.1.10 --ports 1-1000
```

### Arguments

| Argument   | Description                  |
| ---------- | ---------------------------- |
| `--target` | Target IP address            |
| `--ports`  | Port range (default: 1-1024) |

---

## 🧪 Example Output

```
Scanning 192.168.1.10...

OS Guess: Linux

[OPEN] 22 -> SSH-2.0-OpenSSH_8.2
[OPEN] 80 -> Apache/2.4.41
[OPEN] 443 -> Unknown

Results saved to results/scan_results.json
```

---

## 📦 Output (JSON)

```json
{
  "target": "192.168.1.10",
  "open_ports": [
    {"port": 22, "banner": "SSH-2.0-OpenSSH_8.2"},
    {"port": 80, "banner": "Apache/2.4.41"}
  ]
}
```

---

## 🧠 Concepts Used

* TCP/IP & Port Scanning
* Multithreading (I/O-bound optimization)
* Banner Grabbing
* CLI Tool Development
* JSON Serialization

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes only**.
Do not scan networks without proper authorization.

---

## ⭐ Future Improvements

* UDP scanning
* Service version fingerprinting
* GUI interface
* Integration with vulnerability scanning

---

## 👨‍💻 Author

### Navanil Das

- GitHub: [https://github.com/yourusername](https://github.com/navanil-das)
- LinkedIn: [https://linkedin.com/in/yourprofile](https://www.linkedin.com/in/navanil-das-83ba41296/)

---
