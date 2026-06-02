# 🔍 Network Scanner

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

## 🏗️ Project Architecture

### Architecture Overview

```text
+------------------+
|      User        |
+--------+---------+
         |
         v
+------------------+
| Command Line UI  |
+--------+---------+
         |
         v
+------------------+
| Scanner Engine   |
| (Main Logic)     |
+---+----------+---+
    |          |
    v          v
+-------+  +--------+
| Socket|  | Thread |
| Module|  | Pool   |
+---+---+  +---+----+
    |          |
    +-----+----+
          |
          v
+------------------+
| Target Network   |
| IPs & Ports      |
+--------+---------+
         |
         v
+------------------+
| Result Processor |
+--------+---------+
         |
         v
+------------------+
| Output / Report  |
+------------------+
```

### Components

 1. Command Line Interface (CLI)
Acts as the entry point of the application. It accepts user inputs such as the target IP address, hostname, and port range to scan.

 2. Scanner Engine
The core component responsible for coordinating the scanning workflow. It validates inputs, manages scan execution, and collects results.

 3. Socket Module
Uses Python socket programming to establish TCP connections with target ports and determine whether they are open, closed, or filtered.

 4. Thread Pool
Implements multithreading to scan multiple ports concurrently, significantly reducing overall scan time compared to sequential scanning.

 5. Target Network Layer
Represents the destination hosts and ports being scanned. The scanner interacts with this layer to perform connectivity checks.

 6. Result Processor
Aggregates scan results, filters relevant information, and prepares the output in a user-friendly format.

 7. Output Layer
Displays the final scan results, including open ports and associated services, through the console interface.

---

## 🔄 Data Flow

```text
User Input
    │
    ▼
Command Line Interface
    │
    ▼
Scanner Engine
    │
    ▼
Threaded Port Scanning
    │
    ▼
Socket Connections
    │
    ▼
Port Status Detection
    │
    ▼
Result Aggregation
    │
    ▼
Console Output
```
---
### Workflow

1. The user provides the target host and port range.
2. The CLI forwards the information to the Scanner Engine.
3. The Scanner Engine creates worker threads for concurrent scanning.
4. Each thread uses sockets to attempt connections to target ports.
5. The scanner determines whether each port is open or closed.
6. Results from all threads are aggregated and processed.
7. The final report is displayed to the user.

---

## ⚡ Design Highlights

- Multithreaded architecture for faster scanning performance.
- Modular design separating scanning logic, networking, and output handling.
- Efficient socket-based port detection using Python networking libraries.
- Scalable structure that can be extended with service detection, banner grabbing, OS fingerprinting, or vulnerability scanning modules.
- Lightweight and easy to run without external dependencies.

---

## ⚙️ Installation

```bash
git clone https://github.com/navanil-das/network-scanner.git
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

- GitHub: [https://github.com/navanil-das](https://github.com/navanil-das)
- LinkedIn: [https://linkedin.com/in/navanil-das](https://www.linkedin.com/in/navanil-das-83ba41296/)

---
