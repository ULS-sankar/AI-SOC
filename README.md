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

<br><br>

[📊 Dashboard](#-soc-dashboard) •
[🏗️ Architecture](#-architecture) •
[🚨 Detection](#-detection-engine) •
[🤖 AI Analysis](#-ai-threat-analysis) •
[🧪 Testing](#-security-testing-lab) •
[🚀 Roadmap](#-roadmap)

</div>

---

## 🔥 Project Snapshot

| | |
|---|---|
| 🎯 **Focus** | Security Operations / Detection Engineering |
| 🖥️ **Sensor** | Ubuntu Linux |
| 🧪 **Attack Host** | Kali Linux |
| 🔎 **Detection** | Python + Scapy |
| 🧠 **AI** | Qwen 2.5 3B + Ollama |
| 🎯 **Threat Framework** | MITRE ATT&CK |
| 🌐 **Dashboard** | Flask + Chart.js |
| 📦 **Status** | Working Prototype |

> **Design principle:** detection first, AI second. The AI layer enriches detected events instead of replacing deterministic security controls.

---

# 📊 SOC Dashboard

![AI-SOC Dashboard](docs/screenshots/dashboard.png)

> 📸 **Screenshot slot:** replace `docs/screenshots/dashboard.png` with the final dashboard capture.

### 🚨 Security Alerts

![Security Alerts](docs/screenshots/alerts.png)

### 🤖 AI Threat Analysis

![AI Threat Analysis](docs/screenshots/ai-analysis.png)

---

# 🧩 Core Capabilities

| Capability | Implementation |
|---|---|
| 🔎 Packet Monitoring | Scapy |
| 🚨 Attack Detection | Python detection engine |
| 📝 Alert Logging | Structured alert log |
| 🎯 MITRE Mapping | ATT&CK techniques |
| 🤖 AI Investigation | Qwen 2.5 3B + Ollama |
| 📊 SOC Visualization | Flask + Chart.js |
| 🔍 Alert Filtering | Attack / IP filters |
| 📥 Log Export | Flask endpoint |
| 🧪 Lab Testing | Kali + VirtualBox |

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
                    │          enp0s8               │
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
                    │        ALERT LOGGER          │
                    │           logger.py          │
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
          │   OLLAMA         │          │     SOC WEB UI   │
          │   Qwen 2.5 3B    │          │ Alerts • Charts  │
          └────────┬─────────┘          │ Filters • AI     │
                   │                    └──────────────────┘
                   ▼
             Threat Context