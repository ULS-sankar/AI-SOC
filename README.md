# AI-SOC

## AI-Powered Security Operations Center

AI-SOC is a lightweight Security Operations Center (SOC) prototype designed to detect common network-based attacks, generate security alerts, map detected attacks to MITRE ATT&CK techniques, and use a local AI model to analyze the detected threats.

The project uses Scapy for network traffic monitoring, Flask for the security dashboard, and Qwen 2.5 running through Ollama for AI-powered threat analysis.

---

## Features

- Real-time network packet monitoring
- Network attack detection using Scapy
- Security alert generation and logging
- MITRE ATT&CK technique mapping
- Local AI-powered threat analysis
- Qwen 2.5 3B model integration through Ollama
- Flask-based SOC dashboard
- Attack statistics and charts
- Source IP filtering
- Attack-type filtering
- Alert log download
- Alert log clearing
- AI threat analysis panel

---

## Detected Attacks

The current version detects five network attack patterns:

| Attack | Detection |
|---|---|
| ICMP Sweep | Detects ICMP requests targeting multiple hosts |
| Ping Flood | Detects a high volume of ICMP Echo Requests |
| TCP SYN Scan | Detects repeated TCP SYN packets from a source |
| TCP SYN Flood | Detects a high volume of TCP SYN packets |
| UDP Scan | Detects repeated UDP traffic across ports |

---

## MITRE ATT&CK Mapping

Detected attacks are mapped to relevant MITRE ATT&CK techniques.

| Attack | MITRE Technique | Technique Name |
|---|---|---|
| ICMP Sweep | T1046 | Network Service Discovery |
| Ping Flood | T1498.001 | Network Denial of Service: Direct Network Flood |
| TCP SYN Flood | T1498.001 | Network Denial of Service: Direct Network Flood |

Additional attack mappings can be extended as the detection engine grows.

---

## System Architecture

```text
                    ┌─────────────────────┐
                    │    Kali Linux       │
                    │ Attack Generation   │
                    └──────────┬──────────┘
                               │
                               │ Network Traffic
                               ▼
                    ┌─────────────────────┐
                    │   Scapy Detector    │
                    │    detector.py      │
                    └──────────┬──────────┘
                               │
                               │ Security Alert
                               ▼
                    ┌─────────────────────┐
                    │     Alert Logger    │
                    │     logger.py       │
                    └──────────┬──────────┘
                               │
                               ▼
                       logs/alerts.log
                               │
                  ┌────────────┴────────────┐
                  │                         │
                  ▼                         ▼
        ┌──────────────────┐      ┌──────────────────┐
        │ MITRE ATT&CK     │      │ Qwen 2.5 3B AI   │
        │ Technique Mapping│      │ Ollama Analyzer  │
        └──────────────────┘      └─────────┬────────┘
                                            │
                                            ▼
                                  ┌──────────────────┐
                                  │ Flask Dashboard  │
                                  │   dashboard.py   │
                                  └──────────────────┘
