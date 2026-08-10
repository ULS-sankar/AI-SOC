import requests
import json
import os
import time


# ============================================================
# Ollama Configuration
# ============================================================

OLLAMA_URL = "http://10.0.2.2:11434/api/generate"
MODEL = "qwen2.5:3b"


# ============================================================
# File Configuration
# ============================================================

LOG_FILE = "logs/alerts.log"
ANALYSIS_FILE = "logs/ai_analysis.json"


# ============================================================
# MITRE ATT&CK Mapping
# ============================================================
MITRE_MAPPING = {

    "TCP SYN Scan": {
        "technique": "T1046",
        "name": "Network Service Discovery"
    },

    "Ping Flood": {
        "technique": "T1498.001",
        "name": "Network Denial of Service: Direct Network Flood"
    },

    "UDP Scan": {
        "technique": "T1046",
        "name": "Network Service Discovery"
    },

    "TCP SYN Flood": {
        "technique": "T1498.001",
        "name": "Network Denial of Service: Direct Network Flood"
    },

    "ICMP Sweep": {
        "technique": "T1046",
        "name": "Network Service Discovery"
    }

}


# ============================================================
# Parse Alert
# ============================================================

def parse_alert(line):

    parts = [
        part.strip()
        for part in line.split("|")
    ]

    if len(parts) < 7:
        return None

    alert = {

        "timestamp": parts[0],

        "severity": parts[1],

        "attack": parts[2],

        "source_ip":
            parts[3].replace("SRC=", ""),

        "destination_ip":
            parts[4].replace("DST=", ""),

        "source_port":
            parts[5].replace("SPORT=", ""),

        "destination_port":
            parts[6].replace("DPORT=", "")

    }

    return alert


# ============================================================
# Get MITRE Information
# ============================================================

def get_mitre_info(attack):

    return MITRE_MAPPING.get(

        attack,

        {
            "technique": "Unknown",
            "name": "Unknown"
        }

    )


# ============================================================
# Analyze Alert With AI
# ============================================================

def analyze_alert(alert):

    mitre = get_mitre_info(
        alert["attack"]
    )


    prompt = f"""
You are an AI cybersecurity SOC analyst.

Analyze this security alert.

Timestamp: {alert['timestamp']}
Severity: {alert['severity']}
Attack Type: {alert['attack']}
Source IP: {alert['source_ip']}
Destination IP: {alert['destination_ip']}
Source Port: {alert['source_port']}
Destination Port: {alert['destination_port']}

Known MITRE ATT&CK mapping:

Technique ID: {mitre['technique']}
Technique Name: {mitre['name']}

Return ONLY valid JSON.

Use exactly this structure:

{{
    "threat_summary": "Short explanation of what happened",
    "why_it_matters": "Short explanation of the security impact",
    "recommended_actions": [
        "Action 1",
        "Action 2",
        "Action 3"
    ]
}}

Rules:

- Do not invent another MITRE ATT&CK technique.
- Do not change the supplied MITRE ATT&CK mapping.
- Keep the response concise.
- Return JSON only.
- Do not use Markdown.
"""


    payload = {

        "model": MODEL,

        "prompt": prompt,

        "stream": False

    }


    try:

        response = requests.post(

            OLLAMA_URL,

            json=payload,

            timeout=120

        )


        response.raise_for_status()


        result = response.json()


        ai_response = result.get(
            "response",
            ""
        )


        # ----------------------------------------
        # Clean AI response
        # ----------------------------------------

        ai_response = ai_response.strip()


        if ai_response.startswith(
            "```json"
        ):

            ai_response = ai_response[7:]


        if ai_response.startswith(
            "```"
        ):

            ai_response = ai_response[3:]


        if ai_response.endswith(
            "```"
        ):

            ai_response = ai_response[:-3]


        ai_response = ai_response.strip()


        # ----------------------------------------
        # Parse JSON
        # ----------------------------------------

        try:

            analysis = json.loads(
                ai_response
            )


        except json.JSONDecodeError:

            analysis = {

                "threat_summary":
                    ai_response,

                "why_it_matters":
                    "",

                "recommended_actions":
                    []

            }


        # ----------------------------------------
        # Add trusted MITRE information
        # ----------------------------------------

        analysis["mitre_technique"] = \
            mitre["technique"]

        analysis["mitre_name"] = \
            mitre["name"]


        return analysis


    except requests.exceptions.RequestException as e:

        return {

            "error":
                f"Ollama connection error: {e}"

        }


# ============================================================
# Save AI Analysis
# ============================================================

def save_analysis(alert, analysis):

    os.makedirs(
        os.path.dirname(ANALYSIS_FILE),
        exist_ok=True
    )


    # Load existing analyses

    try:

        with open(
            ANALYSIS_FILE,
            "r"
        ) as file:

            data = json.load(file)


    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):

        data = []


    # Create analysis record

    record = {

        "alert": alert,

        "analysis": analysis

    }


    data.append(record)


    # Save

    with open(
        ANALYSIS_FILE,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


# ============================================================
# Get Existing Alert Count
# ============================================================

def get_existing_alert_count():

    try:

        with open(
            LOG_FILE,
            "r"
        ) as file:

            lines = [

                line.strip()

                for line in file

                if line.strip()

            ]

            return len(lines)


    except FileNotFoundError:

        return 0


# ============================================================
# Analyze New Alerts
# ============================================================

def analyze_new_alerts(
    processed_count
):

    try:

        with open(
            LOG_FILE,
            "r"
        ) as file:

            lines = [

                line.strip()

                for line in file

                if line.strip()

            ]


    except FileNotFoundError:

        return processed_count


    current_count = len(lines)


    # ----------------------------------------
    # No new alerts
    # ----------------------------------------

    if current_count <= processed_count:

        return current_count


    # ----------------------------------------
    # New alerts detected
    # ----------------------------------------

    new_lines = lines[
        processed_count:
    ]


    print()
    print("=" * 60)
    print("       NEW SECURITY ALERT DETECTED")
    print("=" * 60)


    for line in new_lines:

        alert = parse_alert(line)


        if not alert:

            print(
                "⚠ Invalid alert format"
            )

            continue


        print()
        print(
            f"Attack : {alert['attack']}"
        )

        print(
            f"Source : {alert['source_ip']}"
        )

        print(
            f"Target : {alert['destination_ip']}"
        )

        print(
            "AI analyzing..."
        )


        # ----------------------------------------
        # AI Analysis
        # ----------------------------------------

        analysis = analyze_alert(
            alert
        )


        # ----------------------------------------
        # Save
        # ----------------------------------------

        save_analysis(
            alert,
            analysis
        )


        print()
        print(
            "AI analysis completed."
        )


        if "error" in analysis:

            print(
                "ERROR:",
                analysis["error"]
            )

        else:

            print(
                "Threat:",
                analysis.get(
                    "threat_summary",
                    ""
                )
            )


    print("=" * 60)


    return current_count


# ============================================================
# Automatic Monitoring
# ============================================================

def monitor_alerts():

    print()
    print("=" * 60)
    print("          AI-SOC AUTO ANALYZER")
    print("=" * 60)

    print(
        f"Monitoring: {LOG_FILE}"
    )

    print(
        f"Model     : {MODEL}"
    )

    print(
        "Status    : RUNNING"
    )

    print("=" * 60)


    # Start from existing alerts

    processed_count = \
        get_existing_alert_count()


    print(
        f"Existing alerts: {processed_count}"
    )

    print(
        "Waiting for new alerts..."
    )


    # ----------------------------------------
    # Continuous monitoring
    # ----------------------------------------

    while True:

        try:

            processed_count = \
                analyze_new_alerts(
                    processed_count
                )


            time.sleep(5)


        except KeyboardInterrupt:

            print()
            print(
                "AI-SOC analyzer stopped."
            )

            break


        except Exception as e:

            print(
                "Monitoring error:",
                e
            )

            time.sleep(5)


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":

    monitor_alerts()