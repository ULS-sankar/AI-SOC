<div align="center">

# 🛡️ AI-SOC

### AI-Powered Security Operations Center

**Detect • Analyze • Correlate • Visualize**

A practical cybersecurity portfolio project combining **network intrusion detection, MITRE ATT&CK mapping, local Qwen AI threat analysis, and a Flask SOC dashboard**.

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
                    │       DETECTION ENGINE        │
                    │          detector.py          │
                    │       Scapy inspection        │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │        ALERT LOGGER           │
                    │          logger.py            │
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
🚨 Detection Engine

The current prototype has been successfully tested against five controlled attack scenarios.

#	Detection	Category	Status
01	🔵 ICMP Sweep	Network Service Discovery	✅
02	🌊 Ping Flood	Network DoS	✅
03	🔍 TCP SYN Scan	Network Scanning	✅
04	⚡ TCP SYN Flood	Network DoS	✅
05	📡 UDP Scan	Network Scanning	✅
🎯 MITRE ATT&CK
Attack	Technique	ATT&CK Name
ICMP Sweep	T1046	Network Service Discovery
Ping Flood	T1498.001	Network Denial of Service: Direct Network Flood
TCP SYN Flood	T1498.001	Network Denial of Service: Direct Network Flood
🤖 AI Threat Analysis

AI-SOC uses a locally hosted Qwen 2.5 3B model through Ollama to enrich security alerts.

Security Alert
      ↓
Flask /api/analyze
      ↓
ai_analyzer.py
      ↓
Ollama
      ↓
Qwen 2.5 3B
      ↓
Threat Summary
      ↓
Why It Matters
      ↓
MITRE Context
      ↓
Recommended Actions
      ↓
SOC Dashboard

The AI layer acts as an investigation assistant and does not replace the packet-level detection engine.

🧪 Security Testing Lab
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
Connectivity Test
ping -c 4 192.168.100.20
Packet Capture
sudo tcpdump -ni enp0s8 icmp
ICMP Discovery
sudo nmap -PE -sn 192.168.100.0/24
Ping Flood
sudo ping -f -c 100 192.168.100.20
TCP SYN Scan
sudo nmap -sS -p 1-1000 192.168.100.20
TCP SYN Flood
sudo hping3 -S --flood -p 80 192.168.100.20
UDP Scan
sudo nmap -sU -p 1-100 192.168.100.20

⚠️ These commands are intended only for an isolated, authorized cybersecurity lab environment.

📸 Project Screenshots
SOC Dashboard

Security Alerts

AI Threat Analysis

Detection Engine

Network Testing

Packet Capture

🧩 Core Capabilities
Capability	Implementation
🔎 Packet Monitoring	Scapy
🚨 Attack Detection	Python Detection Engine
📝 Alert Logging	Structured Alert Log
🎯 MITRE Mapping	MITRE ATT&CK
🤖 AI Investigation	Qwen 2.5 3B + Ollama
📊 SOC Visualization	Flask + Chart.js
🔍 Alert Filtering	Attack / IP Filters
📥 Log Export	Flask Endpoint
🧪 Lab Testing	Kali + Ubuntu + VirtualBox
📁 Project Structure
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
├── requirements.txt
├── .gitignore
└── README.md
⚙️ Installation
Clone the Repository
git clone https://github.com/ULS-sankar/AI-SOC.git
cd AI-SOC
Create Virtual Environment
python3 -m venv venv
Activate Environment
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
🧠 Configure Ollama

Install and run Ollama on the system hosting the model.

Pull the Qwen model:

ollama pull qwen2.5:3b

Verify:

ollama list

The AI analyzer communicates with the local Ollama API.

▶️ Running AI-SOC
Start Detection Engine
sudo venv/bin/python detector.py
Start AI Analyzer
source venv/bin/activate
python3 ai_analyzer.py
Start Dashboard
source venv/bin/activate
python3 dashboard.py

Then open:

http://127.0.0.1:5000
🔄 SOC Workflow
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
📈 Dashboard Features

The SOC dashboard provides:

🚨 Total alert count
🌊 Ping flood statistics
🔍 TCP SYN scan statistics
📊 Attack distribution charts
📈 Attack count charts
🔎 Attack filtering
🌐 Source IP filtering
🤖 Manual AI analysis
📝 Security alert table
📥 Log download
🗑️ Log clearing
💾 Local AI analysis persistence
🛡️ Security Design

AI-SOC follows a layered security-monitoring approach:

Layer 1 — Network Visibility

Scapy captures network traffic from the monitored interface.

Layer 2 — Detection

Python rules identify suspicious traffic patterns.

Layer 3 — Alerting

Detected events are written to structured security logs.

Layer 4 — Threat Mapping

Selected detections are associated with MITRE ATT&CK techniques.

Layer 5 — AI Enrichment

Qwen analyzes the alert and generates contextual information.

Layer 6 — Visualization

Flask presents alerts and AI analysis through the SOC dashboard.

🚀 Roadmap
✅ Completed
 Network packet monitoring
 ICMP Sweep detection
 Ping Flood detection
 TCP SYN Scan detection
 TCP SYN Flood detection
 UDP Scan detection
 Alert logging
 MITRE ATT&CK mapping
 Flask SOC dashboard
 Chart.js visualization
 IP and attack filtering
 Local Qwen AI analysis
 Ollama integration
 VirtualBox testing environment
 GitHub repository
🔄 Future Detection Improvements
 ARP spoofing detection
 DNS scanning detection
 SSH brute-force detection
 HTTP attack detection
 Port sweep correlation
 Behavioral baselining
 Anomaly detection
 Expanded MITRE ATT&CK coverage
🔮 Future SOC Improvements
 Database-backed alert storage
 WebSocket-based live updates
 Advanced alert correlation
 Authentication
 Role-Based Access Control
 Alert severity scoring
 Email notifications
 Telegram/Discord notifications
 Automated incident response
🤖 Future AI Improvements
 AI alert prioritization
 Automated incident summaries
 Multi-alert correlation
 Attack-chain reconstruction
 Threat-hunting assistance
 Automated remediation recommendations
 RAG-based security knowledge
 Historical incident analysis
⚠️ Limitations

AI-SOC is currently a working cybersecurity prototype and should not be considered a production enterprise SIEM.

Current limitations include:

Rule/threshold-based detection
Limited attack coverage
Local file-based alert storage
Single-node deployment
Lightweight dashboard architecture
AI analysis depends on local Ollama availability
No enterprise authentication or RBAC
No distributed sensor architecture
🎓 Learning Objectives

This project demonstrates practical experience with:

Network security monitoring
Packet analysis
Intrusion detection
Python cybersecurity development
Scapy
Linux networking
Kali Linux
VirtualBox networking
Flask
REST APIs
JavaScript
Chart.js
Local LLM deployment
Ollama
MITRE ATT&CK
Security alert engineering
SOC dashboard development
Git and GitHub
📚 Technologies
<div align="center">
Technology	Purpose
🐍 Python	Detection & backend
🕵️ Scapy	Packet analysis
🌐 Flask	SOC web application
📊 Chart.js	Dashboard visualization
🤖 Ollama	Local AI runtime
🧠 Qwen 2.5 3B	Threat analysis
🎯 MITRE ATT&CK	Threat mapping
🐧 Ubuntu	SOC host
🐉 Kali Linux	Security testing
📦 VirtualBox	Isolated lab environment
🐙 GitHub	Version control
</div>
⚠️ Disclaimer

This project is developed for educational purposes, cybersecurity learning, authorized testing, and isolated laboratory environments.

Do not use the detection-testing commands against systems or networks without explicit authorization.

The author is not responsible for misuse of this project.

👨‍💻 Author
<div align="center">
Sasi Sankar

M.Tech Integrated Computer Science Student

Cybersecurity · SOC · Network Security · Python · AI · Web Development

🛡️ Detect → Analyze → Understand → Respond

GitHub Repository

https://github.com/ULS-sankar/AI-SOC

</div> ```
Then save and push

After replacing the file:

cd ~/ai-soc
git add README.md
git commit -m "Redesign professional cybersecurity README"
git push origin main

One important detail: don't paste the outer ```markdown and ``` into your README. Those are only the code-block markers for this chat. Your actual README.md should start with:

<div align="center">

and end with:

</div>

After that, refresh the GitHub repository page. The formatting should be completely different from the screenshot you're seeing now.

Pasted markdown(3).md
File
is this right 

Not quite, baba — the file you just uploaded is still the corrupted version. The Markdown is getting flattened after the Architecture section.

For example, your uploaded version has:

└──────────────────┘
🚨 Detection Engine

The current prototype...

instead of closing the architecture code block with:

and then starting:

# 🚨 Detection Engine

The same problem happens with your tables, testing commands, project structure, and later sections.

BUT — good news

I can see you already have a correctly formatted README version in your uploaded project files. It has proper Markdown headings, tables, fenced code blocks, screenshot placeholders, and the architecture diagram.

That version is the one you want.

What I recommend

Don't manually copy the giant README through the chat again. That's what's causing the formatting disaster.

Use the proper README.md version that already exists, then check it locally:

cd ~/ai-soc
code README.md

Make sure you see things like:

# 🛡️ AI-SOC

## 🔥 Project Snapshot

| | |
|---|---|

# 🏗️ Architecture

```text
...
🚨 Detection Engine

If those backticks and line breaks are actually present, **you're good**.

Your README also already has the screenshot structure:

```markdown
![AI-SOC Dashboard](docs/screenshots/dashboard.png)

![Security Alerts](docs/screenshots/alerts.png)

![AI Threat Analysis](docs/screenshots/ai-analysis.png)

![Detection Engine](docs/screenshots/detection-engine.png)

which is exactly what we wanted.

So don't push the corrupted pasted version. If you want, I can give you the final clean README as a downloadable .md file so you can simply replace ~/ai-soc/README.md and push it — zero copy/paste formatting headache.

can you give me that readme so i canj copy and paste 

Absolutely, baba. Here is the clean, copy-paste-ready README.md. The important part is that all Markdown headings, tables, and code blocks have the proper line breaks.

Copy everything inside this block into README.md — don't include the outer ```markdown line itself.

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
                    │       DETECTION ENGINE        │
                    │          detector.py          │
                    │       Scapy inspection        │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │        ALERT LOGGER           │
                    │          logger.py            │
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
🚨 Detection Engine

The current prototype has been successfully tested against five controlled attack scenarios.

#	Detection	Category	Status
01	🔵 ICMP Sweep	Network Service Discovery	✅
02	🌊 Ping Flood	Network DoS	✅
03	🔍 TCP SYN Scan	Network Scanning	✅
04	⚡ TCP SYN Flood	Network DoS	✅
05	📡 UDP Scan	Network Scanning	✅
🎯 MITRE ATT&CK Mapping
Attack	Technique	ATT&CK Name
ICMP Sweep	T1046	Network Service Discovery
Ping Flood	T1498.001	Network Denial of Service: Direct Network Flood
TCP SYN Flood	T1498.001	Network Denial of Service: Direct Network Flood
🤖 AI Threat Analysis

AI-SOC uses a locally hosted Qwen 2.5 3B model through Ollama to enrich security alerts.

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

The AI layer acts as an investigation assistant and does not replace the packet-level detection engine.

🧪 Security Testing Lab
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
Connectivity Test
ping -c 4 192.168.100.20
Packet Capture
sudo tcpdump -ni enp0s8 icmp
ICMP Discovery
sudo nmap -PE -sn 192.168.100.0/24
Ping Flood
sudo ping -f -c 100 192.168.100.20
TCP SYN Scan
sudo nmap -sS -p 1-1000 192.168.100.20
TCP SYN Flood
sudo hping3 -S --flood -p 80 192.168.100.20
UDP Scan
sudo nmap -sU -p 1-100 192.168.100.20

⚠️ These commands are intended only for an isolated, authorized cybersecurity laboratory environment.

📸 Project Screenshots
SOC Dashboard

Security Alerts

AI Threat Analysis

Detection Engine

Network Testing

Packet Capture

🧩 Core Capabilities
Capability	Implementation
🔎 Packet Monitoring	Scapy
🚨 Attack Detection	Python Detection Engine
📝 Alert Logging	Structured Alert Log
🎯 MITRE Mapping	MITRE ATT&CK
🤖 AI Investigation	Qwen 2.5 3B + Ollama
📊 SOC Visualization	Flask + Chart.js
🔍 Alert Filtering	Attack / IP Filters
📥 Log Export	Flask Endpoint
🧪 Lab Testing	Kali + Ubuntu + VirtualBox
📁 Project Structure
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
⚙️ Installation
Clone the Repository
git clone https://github.com/ULS-sankar/AI-SOC.git
cd AI-SOC
Create Virtual Environment
python3 -m venv venv
Activate Environment
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
🧠 Configure Ollama

Install and run Ollama on the system hosting the model.

Pull the Qwen model:

ollama pull qwen2.5:3b

Verify:

ollama list

The AI analyzer communicates with the local Ollama API.

▶️ Running AI-SOC
Start Detection Engine
sudo venv/bin/python detector.py
Start AI Analyzer
source venv/bin/activate
python3 ai_analyzer.py
Start Dashboard
source venv/bin/activate
python3 dashboard.py

Then open:

http://127.0.0.1:5000
🔄 SOC Workflow
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
📈 Dashboard Features

The SOC dashboard provides:

🚨 Total alert count
🌊 Ping flood statistics
🔍 TCP SYN scan statistics
📊 Attack distribution charts
📈 Attack count charts
🔎 Attack filtering
🌐 Source IP filtering
🤖 Manual AI analysis
📝 Security alert table
📥 Log download
🗑️ Log clearing
💾 Local AI analysis persistence
🛡️ Security Design

AI-SOC follows a layered security-monitoring approach.

Layer 1 — Network Visibility

Scapy captures network traffic from the monitored interface.

Layer 2 — Detection

Python rules identify suspicious traffic patterns.

Layer 3 — Alerting

Detected events are written to structured security logs.

Layer 4 — Threat Mapping

Selected detections are associated with MITRE ATT&CK techniques.

Layer 5 — AI Enrichment

Qwen analyzes the alert and generates contextual information.

Layer 6 — Visualization

Flask presents alerts and AI analysis through the SOC dashboard.

🚀 Roadmap
✅ Completed
 Network packet monitoring
 ICMP Sweep detection
 Ping Flood detection
 TCP SYN Scan detection
 TCP SYN Flood detection
 UDP Scan detection
 Alert logging
 MITRE ATT&CK mapping
 Flask SOC dashboard
 Chart.js visualization
 IP and attack filtering
 Local Qwen AI analysis
 Ollama integration
 VirtualBox testing environment
 GitHub repository
🔄 Future Detection Improvements
 ARP spoofing detection
 DNS scanning detection
 SSH brute-force detection
 HTTP attack detection
 Port sweep correlation
 Behavioral baselining
 Anomaly detection
 Expanded MITRE ATT&CK coverage
🔮 Future SOC Improvements
 Database-backed alert storage
 WebSocket-based live updates
 Advanced alert correlation
 Authentication
 Role-Based Access Control
 Alert severity scoring
 Email notifications
 Telegram/Discord notifications
 Automated incident response
🤖 Future AI Improvements
 AI alert prioritization
 Automated incident summaries
 Multi-alert correlation
 Attack-chain reconstruction
 Threat-hunting assistance
 Automated remediation recommendations
 RAG-based security knowledge
 Historical incident analysis
⚠️ Limitations

AI-SOC is currently a working cybersecurity prototype and should not be considered a production enterprise SIEM.

Current limitations include:

Rule/threshold-based detection
Limited attack coverage
Local file-based alert storage
Single-node deployment
Lightweight dashboard architecture
AI analysis depends on local Ollama availability
No enterprise authentication or RBAC
No distributed sensor architecture
🎓 Learning Objectives

This project demonstrates practical experience with:

Network security monitoring
Packet analysis
Intrusion detection
Python cybersecurity development
Scapy
Linux networking
Kali Linux
VirtualBox networking
Flask
REST APIs
JavaScript
Chart.js
Local LLM deployment
Ollama
MITRE ATT&CK
Security alert engineering
SOC dashboard development
Git and GitHub
📚 Technologies
Technology	Purpose
🐍 Python	Detection & backend
🕵️ Scapy	Packet analysis
🌐 Flask	SOC web application
📊 Chart.js	Dashboard visualization
🤖 Ollama	Local AI runtime
🧠 Qwen 2.5 3B	Threat analysis
🎯 MITRE ATT&CK	Threat mapping
🐧 Ubuntu	SOC host
🐉 Kali Linux	Security testing
📦 VirtualBox	Isolated lab environment
🐙 GitHub	Version control
⚠️ Disclaimer

This project is developed for educational purposes, cybersecurity learning, authorized testing, and isolated laboratory environments.

Do not use the detection-testing commands against systems or networks without explicit authorization.

The author is not responsible for misuse of this project.

👨‍💻 Author
<div align="center">
Sasi Sankar

M.Tech Integrated Computer Science Student

Cybersecurity · SOC · Network Security · Python · AI · Web Development

🛡️ Detect → Analyze → Understand → Respond

GitHub Repository

https://github.com/ULS-sankar/AI-SOC

</div> ```