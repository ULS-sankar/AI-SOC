from flask import Flask, render_template, request, redirect, send_file, jsonify
from ai_analyzer import analyze_alert
import math
import os


app = Flask(__name__)
# ============================================================
# MITRE ATT&CK MAPPING
# ============================================================

MITRE_MAPPING = {

    "Ping Flood": {
        "technique": "T1498.001",
        "name": "Network Denial of Service: Direct Network Flood"
    },

    "TCP SYN Flood": {
        "technique": "T1498.001",
        "name": "Network Denial of Service: Direct Network Flood"
    },

    "ICMP Sweep": {
        "technique": "T1046",
        "name": "Network Service Discovery"
    },

    "TCP SYN Scan": {
        "technique": "T1046",
        "name": "Network Service Discovery"
    },

    "UDP Scan": {
        "technique": "T1046",
        "name": "Network Service Discovery"
    }
}

# ============================================================
# HOME / DASHBOARD
# ============================================================

@app.route("/")
def home():

    alerts = []

    attack_filter = request.args.get("attack")
    ip_filter = request.args.get("ip")

    page = request.args.get("page", 1, type=int)
    per_page = 10

    # ========================================================
    # READ ALERT LOG
    # ========================================================

    try:

        with open("logs/alerts.log", "r") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                parts = [
                    part.strip()
                    for part in line.split("|")
                ]

                # Remove SRC= DST= SPORT= DPORT=
                for i in range(len(parts)):

                    if "=" in parts[i]:

                        parts[i] = parts[i].split(
                            "=",
                            1
                        )[1]

                # ------------------------------------------------
                # Make sure alert has enough fields
                # ------------------------------------------------

                if len(parts) < 7:
                    continue

                # =================================================
                # ATTACK FILTER
                # =================================================

                if attack_filter:

                    if attack_filter != parts[2]:
                        continue

                # =================================================
                # IP FILTER
                # =================================================

                if ip_filter:

                    if (
                        ip_filter not in parts[3]
                        and
                        ip_filter not in parts[4]
                    ):
                        continue

                alerts.append(parts)

    except FileNotFoundError:

        pass


    # ============================================================
    # LATEST ALERTS FIRST
    # ============================================================

    alerts.reverse()


    # ============================================================
    # STATISTICS
    # ============================================================

    total_alerts = len(alerts)

    ping_floods = 0
    syn_scans = 0
    syn_floods = 0
    icmp_sweeps = 0
    udp_scans = 0


    for alert in alerts:

        attack = alert[2]


        # --------------------------------------------------------
        # Ping Flood
        # --------------------------------------------------------

        if attack == "Ping Flood":

            ping_floods += 1


        # --------------------------------------------------------
        # TCP SYN Scan
        # --------------------------------------------------------

        elif attack == "TCP SYN Scan":

            syn_scans += 1


        # --------------------------------------------------------
        # TCP SYN Flood
        # --------------------------------------------------------

        elif attack == "TCP SYN Flood":

            syn_floods += 1


        # --------------------------------------------------------
        # ICMP Sweep
        # --------------------------------------------------------

        elif attack == "ICMP Sweep":

            icmp_sweeps += 1


        # --------------------------------------------------------
        # UDP Scan
        # --------------------------------------------------------

        elif attack == "UDP Scan":

            udp_scans += 1


    # ============================================================
    # PAGINATION
    # ============================================================

    total_pages = max(
        1,
        math.ceil(
            total_alerts / per_page
        )
    )


    # Prevent invalid page numbers

    if page < 1:

        page = 1

    if page > total_pages:

        page = total_pages


    start = (page - 1) * per_page

    end = start + per_page


    alerts = alerts[start:end]


    # ============================================================
    # RENDER DASHBOARD
    # ============================================================

    return render_template(

        "index.html",

        alerts=alerts,

        total_alerts=total_alerts,

        ping_floods=ping_floods,

        syn_scans=syn_scans,

        syn_floods=syn_floods,

        icmp_sweeps=icmp_sweeps,

        udp_scans=udp_scans,

        page=page,

        total_pages=total_pages,

        request=request
    )


# ============================================================
# API - GET ALERTS
# ============================================================

@app.route("/api/alerts")
def api_alerts():

    alerts = []


    try:

        with open("logs/alerts.log", "r") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue


                parts = [
                    part.strip()
                    for part in line.split("|")
                ]


                for i in range(len(parts)):

                    if "=" in parts[i]:

                        parts[i] = parts[i].split(
                            "=",
                            1
                        )[1]


                if len(parts) >= 7:

                    attack = parts[2]

                    mitre = MITRE_MAPPING.get(
                        attack,
                        {
                            "technique": "N/A",
                            "name": "Unknown"
                        }
                    )

                    alerts.append({
                        "data": parts,
                        "mitre_technique": mitre["technique"],
                        "mitre_name": mitre["name"]
                    })

    except FileNotFoundError:

        pass


    # Latest alerts first

    alerts.reverse()


    return jsonify(alerts)


# ============================================================
# CLEAR LOGS
# ============================================================

@app.route("/clear", methods=["POST"])
def clear_logs():

    with open(
        "logs/alerts.log",
        "w"
    ):

        pass


    return redirect("/")


# ============================================================
# DOWNLOAD LOGS
# ============================================================

@app.route("/download")
def download_logs():

    if os.path.exists(
        "logs/alerts.log"
    ):

        return send_file(

            "logs/alerts.log",

            as_attachment=True,

            download_name="alerts.log"
        )


    return "No log file found."


# ============================================================
# AI ANALYSIS API
# ============================================================

@app.route(
    "/api/analyze",
    methods=["POST"]
)
def api_analyze():

    data = request.get_json()


    if not data:

        return {
            "error": "No alert data received"
        }, 400


    try:

        analysis = analyze_alert(data)

        return analysis


    except Exception as e:

        return {
            "error": str(e)
        }, 500


# ============================================================
# RUN FLASK
# ============================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )