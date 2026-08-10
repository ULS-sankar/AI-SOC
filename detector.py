from scapy.all import sniff
from config import INTERFACE
import time
from scapy.layers.inet import IP, ICMP, TCP, UDP
from logger import log_alert


# ============================================================
# VARIABLES
# ============================================================

WINDOW_SIZE = 10  # seconds

# ---------------- ICMP Ping Flood ----------------

icmp_count = 0
icmp_window_start = time.time()

# ---------------- TCP SYN Scan ----------------

syn_scan_count = {}
syn_scan_ports = {}
syn_scan_window_start = time.time()

# ---------------- TCP SYN Flood ----------------

syn_flood_count = {}
syn_flood_window_start = time.time()

# ---------------- UDP Scan ----------------

udp_scan_ports = {}
udp_scan_window_start = time.time()

# ---------------- ICMP Sweep ----------------

icmp_sweep_targets = {}
icmp_sweep_window_start = time.time()


# ============================================================
# PRINT PACKET INFORMATION
# ============================================================

def print_packet_info(packet):

    print("-" * 40)

    print(f"Source IP          : {packet[IP].src}")
    print(f"Destination IP     : {packet[IP].dst}")


# ============================================================
# DETECT PING FLOOD
# ============================================================

def detect_ping_flood(packet):

    global icmp_count
    global icmp_window_start

    current_time = time.time()

    if current_time - icmp_window_start >= WINDOW_SIZE:

        icmp_count = 0
        icmp_window_start = current_time

    icmp_count += 1

    print(f"ICMP COUNT         : {icmp_count}")

    if icmp_count == 11:

        print("⚠️ ALERT: Possible Ping Flood Detected!")

        log_alert(
            "High",
            "Ping Flood",
            packet
        )


# ============================================================
# DETECT ICMP SWEEP
# ============================================================

def detect_icmp_sweep(packet):

    global icmp_sweep_targets
    global icmp_sweep_window_start

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst

    current_time = time.time()

    if current_time - icmp_sweep_window_start >= WINDOW_SIZE:

        icmp_sweep_targets = {}
        icmp_sweep_window_start = current_time

    if source_ip not in icmp_sweep_targets:

        icmp_sweep_targets[source_ip] = set()

    icmp_sweep_targets[source_ip].add(destination_ip)

    target_count = len(
        icmp_sweep_targets[source_ip]
    )

    print(
        f"ICMP SWEEP from {source_ip} : "
        f"{target_count} targets"
    )

    if target_count == 5:

        print(
            "⚠️ ALERT: Possible ICMP Sweep Detected!"
        )

        log_alert(
            "Medium",
            "ICMP Sweep",
            packet
        )


# ============================================================
# DETECT TCP SYN SCAN
# ============================================================

def detect_syn_scan(packet):

    global syn_scan_count
    global syn_scan_ports
    global syn_scan_window_start

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst
    destination_port = packet[TCP].dport

    current_time = time.time()

    if current_time - syn_scan_window_start >= WINDOW_SIZE:

        syn_scan_count = {}
        syn_scan_ports = {}
        syn_scan_window_start = current_time

    if source_ip not in syn_scan_count:

        syn_scan_count[source_ip] = 0

    if source_ip not in syn_scan_ports:

        syn_scan_ports[source_ip] = set()

    syn_scan_count[source_ip] += 1

    syn_scan_ports[source_ip].add(
        (destination_ip, destination_port)
    )

    port_count = len(
        syn_scan_ports[source_ip]
    )

    print(
        f"SYN SCAN from {source_ip} : "
        f"{port_count} ports"
    )

    # Detect scanning behaviour:
    # Multiple destination ports within the window

    if port_count == 5:

        print(
            "⚠️ ALERT: Possible TCP SYN Scan Detected!"
        )

        log_alert(
            "High",
            "TCP SYN Scan",
            packet
        )


# ============================================================
# DETECT TCP SYN FLOOD
# ============================================================

def detect_syn_flood(packet):

    global syn_flood_count
    global syn_flood_window_start

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst
    destination_port = packet[TCP].dport

    current_time = time.time()

    if current_time - syn_flood_window_start >= WINDOW_SIZE:

        syn_flood_count = {}
        syn_flood_window_start = current_time

    key = (
        source_ip,
        destination_ip,
        destination_port
    )

    if key not in syn_flood_count:

        syn_flood_count[key] = 0

    syn_flood_count[key] += 1

    count = syn_flood_count[key]

    print(
        f"SYN FLOOD {source_ip} -> "
        f"{destination_ip}:{destination_port} : "
        f"{count}"
    )

    # High number of SYN packets
    # toward the same destination/port

    if count == 20:

        print(
            "⚠️ ALERT: Possible TCP SYN Flood Detected!"
        )

        log_alert(
            "High",
            "TCP SYN Flood",
            packet
        )


# ============================================================
# DETECT UDP SCAN
# ============================================================

def detect_udp_scan(packet):

    global udp_scan_ports
    global udp_scan_window_start

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst
    destination_port = packet[UDP].dport

    current_time = time.time()

    if current_time - udp_scan_window_start >= WINDOW_SIZE:

        udp_scan_ports = {}
        udp_scan_window_start = current_time

    if source_ip not in udp_scan_ports:

        udp_scan_ports[source_ip] = set()

    udp_scan_ports[source_ip].add(
        (destination_ip, destination_port)
    )

    port_count = len(
        udp_scan_ports[source_ip]
    )

    print(
        f"UDP SCAN from {source_ip} : "
        f"{port_count} ports"
    )

    # Multiple UDP destination ports

    if port_count == 5:

        print(
            "⚠️ ALERT: Possible UDP Scan Detected!"
        )

        log_alert(
            "Medium",
            "UDP Scan",
            packet
        )


# ============================================================
# PROCESS PACKETS
# ============================================================

def process_packet(packet):

    if IP not in packet:

        return

    print_packet_info(packet)


    # ========================================================
    # ICMP
    # ========================================================

    if ICMP in packet:

        print("Protocol            : ICMP")

        if packet[ICMP].type == 8:

            print(
                "🔍 ICMP Echo Request Detected"
            )

            # Existing Ping Flood detection
            detect_ping_flood(packet)

            # New ICMP Sweep detection
            detect_icmp_sweep(packet)


    # ========================================================
    # TCP
    # ========================================================

    elif TCP in packet:

        print("Protocol            : TCP")

        print(
            f"Source Port         : "
            f"{packet[TCP].sport}"
        )

        print(
            f"Destination Port    : "
            f"{packet[TCP].dport}"
        )

        flags = packet[TCP].flags

        if flags == "S":

            print(
                "🔍 SYN Packet Detected"
            )

            # SYN scan detection
            detect_syn_scan(packet)

            # SYN flood detection
            detect_syn_flood(packet)


    # ========================================================
    # UDP
    # ========================================================

    elif UDP in packet:

        print("Protocol            : UDP")

        print(
            f"Source Port         : "
            f"{packet[UDP].sport}"
        )

        print(
            f"Destination Port    : "
            f"{packet[UDP].dport}"
        )

        # New UDP scan detection
        detect_udp_scan(packet)


    # ========================================================
    # OTHER
    # ========================================================

    else:

        print("Protocol            : Other")


# ============================================================
# START PACKET CAPTURE
# ============================================================

print("=" * 60)
print("              AI-SOC DETECTION ENGINE")
print("=" * 60)

print(f"Interface : {INTERFACE}")
print("Status    : Monitoring...")
print("=" * 60)


sniff(
    iface=INTERFACE,
    prn=process_packet
)