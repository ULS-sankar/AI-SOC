<div align="center">

# 🛡️ AI-SOC

### AI-Powered Security Operations Center

**Detect • Analyze • Correlate • Visualize**

A practical cybersecurity portfolio project combining **network intrusion detection, MITRE ATT&CK mapping, local Qwen AI threat analysis, and a Flask SOC dashboard.**

<br>

![Status](https://img.shields.io/badge/STATUS-WORKING%20PROTOTYPE-00c853?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![Scapy](https://img.shields.io/badge/Scapy-Network%20Detection-1f6feb?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-Local%20AI-black?style=for-the-badge)
![Qwen](https://img.shields.io/badge/Qwen-2.5--3B-purple?style=for-the-badge)
![MITRE%20ATT%26CK](https://img.shields.io/badge/MITRE-ATT%26CK-red?style=for-the-badge)

</div>

---

## 🔥 Project Snapshot

| Item | Details |
|---|---|
| 🎯 Focus | Security Operations / Detection Engineering |
| 🖥️ Sensor | Ubuntu Linux |
| 🧪 Attack Host | Kali Linux |
| 🔎 Detection | Python + Scapy |
| 🧠 AI | Qwen 2.5 3B + Ollama |
| 🎯 Threat Framework | MITRE ATT&CK |
| 🌐 Dashboard | Flask + Chart.js |
| 📦 Status | Working Prototype |

> **Design principle:** Detection first, AI second. The AI layer enriches detected events instead of replacing deterministic security controls.

---

# 📊 SOC Dashboard

![AI-SOC Dashboard](docs/screenshots/dashboard.png)

> 📸 Replace the image above with your actual dashboard screenshot.

---

# 🏗️ Architecture

```text
                         ┌──────────────────────┐
                         │      KALI LINUX      │
                         │   192.168.100.10     │
                         │                      │
                         │ Controlled Testing   │
                         └──────────┬───────────┘
                                    │
                         Attack / Scan Traffic
                                    │
                                    ▼
                    ┌──────────────────────────────┐
                    │       UBUNTU AI-SOC          │
                    │      192.168.100.20          │
                    │          enp0s8              │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │       DETECTION ENGINE       │
                    │          detector.py         │
                    │       Scapy inspection       │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │         ALERT LOGGER         │
                    │          logger.py           │
                    └──────────────┬───────────────┘
                                   │
                              alerts.log
                                   │
                    ┌──────────────┴──────────────┐
                    │                             │
                    ▼                             ▼
          ┌──────────────────┐          ┌──────────────────┐
          │   AI ANALYZER    │          │  FLASK DASHBOARD │
          │ ai_analyzer.py   │          │   dashboard.py   │
          └────────┬─────────┘          └────────┬─────────┘
                   │                             │
                   ▼                             ▼
          ┌──────────────────┐          ┌──────────────────┐
          │     OLLAMA       │          │     SOC WEB UI   │
          │    Qwen 2.5 3B   │          │ Alerts • Charts  │
          └──────────────────┘          │ Filters • AI     │
                                        └──────────────────┘
```

---

# 🚨 Detection Engine

The current prototype has been successfully tested against five controlled attack scenarios.

| # | Detection | Category | Status |
|---|---|---|---|
| 01 | 🔵 ICMP Sweep | Network Service Discovery | ✅ |
| 02 | 🌊 Ping Flood | Network DoS | ✅ |
| 03 | 🔍 TCP SYN Scan | Network Scanning | ✅ |
| 04 | ⚡ TCP SYN Flood | Network DoS | ✅ |
| 05 | 📡 UDP Scan | Network Scanning | ✅ |

---

# 🎯 MITRE ATT&CK Mapping

| Attack | Technique | ATT&CK Name |
|---|---|---|
| ICMP Sweep | T1046 | Network Service Discovery |
| Ping Flood | T1498.001 | Network Denial of Service: Direct Network Flood |
| TCP SYN Flood | T1498.001 | Network Denial of Service: Direct Network Flood |

---

# 🤖 AI Threat Analysis

AI-SOC uses a locally hosted Qwen 2.5 3B model through Ollama to enrich security alerts.

```text
Security Alert
      │
      ▼
Flask /api/analyze
      │
      ▼
ai_analyzer.py
      │
      ▼
Ollama
      │
      ▼
Qwen 2.5 3B
      │
      ▼
Threat Summary
      │
      ▼
Why It Matters
      │
      ▼
MITRE Context
      │
      ▼
Recommended Actions
      │
      ▼
SOC Dashboard
```

The AI layer acts as an investigation assistant and does not replace the packet-level detection engine.

---

# 🧪 Security Testing Lab

```text
┌─────────────────────┐
│      KALI LINUX     │
│                     │
│ eth1                │
│ 192.168.100.10/24   │
└──────────┬──────────┘
           │
           │ Isolated VirtualBox Network
           │
           ▼
┌─────────────────────┐
│    UBUNTU AI-SOC    │
│                     │
│ enp0s8              │
│ 192.168.100.20/24   │
└─────────────────────┘
```

### Connectivity Test
```bash
ping -c 4 192.168.100.20
```

### Packet Capture
```bash
sudo tcpdump -ni enp0s8 icmp
```

### ICMP Discovery
```bash
sudo nmap -PE -sn 192.168.100.0/24
```

### Ping Flood
```bash
sudo ping -f -c 100 192.168.100.20
```

### TCP SYN Scan
```bash
sudo nmap -sS -p 1-1000 192.168.100.20
```

### TCP SYN Flood
```bash
sudo hping3 -S --flood -p 80 192.168.100.20
```

### UDP Scan
```bash
sudo nmap -sU -p 1-100 192.168.100.20
```

⚠️ *These commands are intended only for an isolated, authorized cybersecurity laboratory environment.*

---

# 📸 Project Screenshots

- **SOC Dashboard**
- **Security Alerts**
- **AI Threat Analysis**
- **Detection Engine**
- **Network Testing**
- **Packet Capture**

---

# 🧩 Core Capabilities

| Capability | Implementation |
|---|---|
| 🔎 Packet Monitoring | Scapy |
| 🚨 Attack Detection | Python Detection Engine |
| 📝 Alert Logging | Structured Alert Log |
| 🎯 MITRE Mapping | MITRE ATT&CK |
| 🤖 AI Investigation | Qwen 2.5 3B + Ollama |
| 📊 SOC Visualization | Flask + Chart.js |
| 🔍 Alert Filtering | Attack / IP Filters |
| 📥 Log Export | Flask Endpoint |
| 🧪 Lab Testing | Kali + Ubuntu + VirtualBox |

---

# 📁 Project Structure

```text
AI-SOC/
│
├── detector.py
│   └── Network packet detection engine
│
├── logger.py
│   └── Security alert logging
│
├── ai_analyzer.py
│   └── Local AI threat analysis
│
├── dashboard.py
│   └── Flask web application
│
├── config.py
│   └── Project configuration
│
├── templates/
│   └── index.html
│       └── SOC dashboard interface
│
├── static/
│   └── css/
│       └── style.css
│
├── logs/
│   ├── alerts.log
│   └── ai_analysis.json
│
├── docs/
│   └── screenshots/
│       ├── dashboard.png
│       ├── alerts.png
│       ├── ai-analysis.png
│       ├── detection-engine.png
│       ├── network-test.png
│       └── tcpdump.png
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

### Clone the Repository
```bash
git clone [https://github.com/ULS-sankar/AI-SOC.git](https://github.com/ULS-sankar/AI-SOC.git)
cd AI-SOC
```

### Create Virtual Environment
```bash
python3 -m venv venv
```

### Activate Environment
```bash
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

# 🧠 Configure Ollama

Install and run Ollama on the system hosting the model.

Pull the Qwen model:
```bash
ollama pull qwen2.5:3b
```

Verify:
```bash
ollama list
```

The AI analyzer communicates with the local Ollama API.

---

# ▶️ Running AI-SOC

### Start Detection Engine
```bash
sudo venv/bin/python detector.py
```

### Start AI Analyzer
```bash
source venv/bin/activate
python3 ai_analyzer.py
```

### Start Dashboard
```bash
source venv/bin/activate
python3 dashboard.py
```

Then open: `http://127.0.0.1:5000`

---

# 🔄 SOC Workflow

```text
Network Traffic
      │
      ▼
Packet Capture
      │
      ▼
Detection Engine
      │
      ├── Normal Traffic
      │       └── Ignore
      │
      └── Suspicious Traffic
              │
              ▼
          Alert Logger
              │
              ▼
          alerts.log
              │
       ┌──────┴──────┐
       │             │
       ▼             ▼
   AI Analyzer    Dashboard
       │             │
       ▼             ▼
     Qwen       SOC Visualization
       │
       ▼
Threat Intelligence
```

---

# 📈 Dashboard Features

The SOC dashboard provides:
- 🚨 Total alert count
- 🌊 Ping flood statistics
- 🔍 TCP SYN scan statistics
- 📊 Attack distribution charts
- 📈 Attack count charts
- 🔎 Attack filtering
- 🌐 Source IP filtering
- 🤖 Manual AI analysis
- 📝 Security alert table
- 📥 Log download
- 🗑️ Log clearing
- 💾 Local AI analysis persistence

---

# 🛡️ Security Design

AI-SOC follows a layered security-monitoring approach:

- **Layer 1 — Network Visibility:** Scapy captures network traffic from the monitored interface.
- **Layer 2 — Detection:** Python rules identify suspicious traffic patterns.
- **Layer 3 — Alerting:** Detected events are written to structured security logs.
- **Layer 4 — Threat Mapping:** Selected detections are associated with MITRE ATT&CK techniques.
- **Layer 5 — AI Enrichment:** Qwen analyzes the alert and generates contextual information.
- **Layer 6 — Visualization:** Flask presents alerts and AI analysis through the SOC dashboard.

---

# 🚀 Roadmap

### ✅ Completed
- [x] Network packet monitoring
- [x] ICMP Sweep detection
- [x] Ping Flood detection
- [x] TCP SYN Scan detection
- [x] TCP SYN Flood detection
- [x] UDP Scan detection
- [x] Alert logging
- [x] MITRE ATT&CK mapping
- [x] Flask SOC dashboard
- [x] Chart.js visualization
- [x] IP and attack filtering
- [x] Local Qwen AI analysis
- [x] Ollama integration
- [x] VirtualBox testing environment
- [x] GitHub repository

### 🔄 Future Detection Improvements
- ARP spoofing detection
- DNS scanning detection
- SSH brute-force detection
- HTTP attack detection
- Port sweep correlation
- Behavioral baselining
- Anomaly detection
- Expanded MITRE ATT&CK coverage

### 🔮 Future SOC Improvements
- Database-backed alert storage
- WebSocket-based live updates
- Advanced alert correlation
- Authentication
- Role-Based Access Control
- Alert severity scoring
- Email notifications
- Telegram/Discord notifications
- Automated incident response

### 🤖 Future AI Improvements
- AI alert prioritization
- Automated incident summaries
- Multi-alert correlation
- Attack-chain reconstruction
- Threat-hunting assistance
- Automated remediation recommendations
- RAG-based security knowledge
- Historical incident analysis

---

# ⚠️ Limitations

AI-SOC is currently a working cybersecurity prototype and should not be considered a production enterprise SIEM.

Current limitations include:
- Rule/threshold-based detection
- Limited attack coverage
- Local file-based alert storage
- Single-node deployment
- Lightweight dashboard architecture
- AI analysis depends on local Ollama availability
- No enterprise authentication or RBAC
- No distributed sensor architecture

---

# 🎓 Learning Objectives

This project demonstrates practical experience with:
- Network security monitoring
- Packet analysis
- Intrusion detection
- Python cybersecurity development
- Scapy
- Linux networking
- Kali Linux
- VirtualBox networking
- Flask
- REST APIs
- JavaScript
- Chart.js
- Local LLM deployment
- Ollama
- MITRE ATT&CK
- Security alert engineering
- SOC dashboard development
- Git and GitHub

---

# 📚 Technologies

| Technology | Purpose |
|---|---|
| 🐍 Python | Detection & backend |
| 🕵️ Scapy | Packet analysis |
| 🌐 Flask | SOC web application |
| 📊 Chart.js | Dashboard visualization |
| 🤖 Ollama | Local AI runtime |
| 🧠 Qwen 2.5 3B | Threat analysis |
| 🎯 MITRE ATT&CK | Threat mapping |
| 🐧 Ubuntu | SOC host |
| 🐉 Kali Linux | Security testing |
| 📦 VirtualBox | Isolated lab environment |
| 🐙 GitHub | Version control |

---

# ⚠️ Disclaimer

This project is developed for educational purposes, cybersecurity learning, authorized testing, and isolated laboratory environments.

Do not use the detection-testing commands against systems or networks without explicit authorization.

The author is not responsible for misuse of this project.

---

<div align="center">

### 👨‍💻 Author

**Sasi Sankar**  
*M.Tech Integrated Computer Science Student*  
Cybersecurity • SOC • Network Security • Python • AI • Web Development  

🛡️ **Detect → Analyze → Understand → Respond**

[GitHub Repository](https://github.com/ULS-sankar/AI-SOC)

</div>