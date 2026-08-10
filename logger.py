from datetime import datetime
from scapy.layers.inet import IP, TCP, UDP

def log_alert(severity, alert_type, packet):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    source_ip = packet[IP].src
    destination_ip = packet[IP].dst
    source_port = "-"
    destination_port = "-"

    if TCP in packet:
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport
    elif UDP in packet:
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport

    with open("logs/alerts.log", "a") as log_file:
        log_file.write(
            f"{timestamp} | {severity} | {alert_type} | "
            f"SRC={source_ip} | DST={destination_ip} | "
            f"SPORT={source_port} | DPORT={destination_port}\n"
        )