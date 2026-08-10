// ============================================================
// AI-SOC DASHBOARD.JS
// LIVE ALERTS + STATISTICS + CHARTS + MITRE + AI ANALYSIS
// ============================================================

let attackChart = null;
let barChart = null;
let lastAlertSignature = "";


// ============================================================
// ATTACK TYPES
// ============================================================

const ATTACK_TYPES = {
    "Ping Flood": 0,
    "TCP SYN Scan": 0,
    "TCP SYN Flood": 0,
    "ICMP Sweep": 0,
    "UDP Scan": 0
};


// ============================================================
// NORMALIZE API ALERT
// ============================================================

function normalizeAlert(alert) {

    // New API format:
    // {
    //     data: [...],
    //     mitre_technique: "...",
    //     mitre_name: "..."
    // }

    if (
        alert &&
        !Array.isArray(alert) &&
        Array.isArray(alert.data)
    ) {

        return {
            data: alert.data,
            mitre_technique:
                alert.mitre_technique || "N/A",
            mitre_name:
                alert.mitre_name || "Unknown"
        };

    }


    // Backward compatibility
    // If API still returns normal arrays

    if (Array.isArray(alert)) {

        return {
            data: alert,
            mitre_technique: "N/A",
            mitre_name: "Unknown"
        };

    }


    return null;
}


// ============================================================
// GET ATTACK STATISTICS
// ============================================================

function calculateStatistics(alerts) {

    const stats = {

        total: alerts.length,

        "Ping Flood": 0,

        "TCP SYN Scan": 0,

        "TCP SYN Flood": 0,

        "ICMP Sweep": 0,

        "UDP Scan": 0

    };


    alerts.forEach(function(alert) {

        const normalized =
            normalizeAlert(alert);

        if (!normalized) {
            return;
        }


        const data =
            normalized.data;


        if (!data || data.length < 3) {
            return;
        }


        const attack =
            data[2];


        if (
            Object.prototype.hasOwnProperty.call(
                stats,
                attack
            )
        ) {

            stats[attack]++;

        }

    });


    return stats;
}


// ============================================================
// SEVERITY STATISTICS
// ============================================================

function updateSeverityStats(alerts) {

    let high = 0;
    let medium = 0;
    let low = 0;


    alerts.forEach(function(alert) {

        const normalized =
            normalizeAlert(alert);

        if (!normalized) {
            return;
        }


        const data =
            normalized.data;


        if (!data || data.length < 2) {
            return;
        }


        const severity =
            data[1];


        if (severity === "High") {

            high++;

        }

        else if (severity === "Medium") {

            medium++;

        }

        else if (severity === "Low") {

            low++;

        }

    });


    const highElement =
        document.getElementById(
            "high-count"
        );


    const mediumElement =
        document.getElementById(
            "medium-count"
        );


    const lowElement =
        document.getElementById(
            "low-count"
        );


    if (highElement) {

        highElement.innerText =
            high;

    }


    if (mediumElement) {

        mediumElement.innerText =
            medium;

    }


    if (lowElement) {

        lowElement.innerText =
            low;

    }

}


// ============================================================
// UPDATE STATISTIC BANNERS
// ============================================================

function updateStatistics(stats) {

    console.log(
        "Updating statistics:",
        stats
    );


    const totalElement =
        document.getElementById(
            "total-alerts"
        );


    if (totalElement) {

        totalElement.innerText =
            stats.total;

    }


    const pingElement =
        document.getElementById(
            "ping-floods"
        );


    if (pingElement) {

        pingElement.innerText =
            stats["Ping Flood"];

    }


    const synScanElement =
        document.getElementById(
            "syn-scans"
        );


    if (synScanElement) {

        synScanElement.innerText =
            stats["TCP SYN Scan"];

    }


    const synFloodElement =
        document.getElementById(
            "syn-floods"
        );


    if (synFloodElement) {

        synFloodElement.innerText =
            stats["TCP SYN Flood"];

    }


    const icmpElement =
        document.getElementById(
            "icmp-sweeps"
        );


    if (icmpElement) {

        icmpElement.innerText =
            stats["ICMP Sweep"];

    }


    const udpElement =
        document.getElementById(
            "udp-scans"
        );


    if (udpElement) {

        udpElement.innerText =
            stats["UDP Scan"];

    }

}


// ============================================================
// UPDATE PIE CHART
// ============================================================

function updatePieChart(stats) {

    if (!attackChart) {
        return;
    }


    attackChart.data.labels = [

        "Ping Flood",
        "TCP SYN Scan",
        "TCP SYN Flood",
        "ICMP Sweep",
        "UDP Scan"

    ];


    attackChart.data.datasets[0].data = [

        stats["Ping Flood"],
        stats["TCP SYN Scan"],
        stats["TCP SYN Flood"],
        stats["ICMP Sweep"],
        stats["UDP Scan"]

    ];


    attackChart.update();

}


// ============================================================
// UPDATE BAR CHART
// ============================================================

function updateBarChart(stats) {

    if (!barChart) {
        return;
    }


    barChart.data.labels = [

        "Ping Flood",
        "TCP SYN Scan",
        "TCP SYN Flood",
        "ICMP Sweep",
        "UDP Scan"

    ];


    barChart.data.datasets[0].data = [

        stats["Ping Flood"],
        stats["TCP SYN Scan"],
        stats["TCP SYN Flood"],
        stats["ICMP Sweep"],
        stats["UDP Scan"]

    ];


    barChart.update();

}


// ============================================================
// CREATE CHARTS
// ============================================================

function initializeCharts() {

    const pieCanvas =
        document.getElementById(
            "attackChart"
        );


    const barCanvas =
        document.getElementById(
            "barChart"
        );


    if (!pieCanvas || !barCanvas) {

        console.error(
            "Chart canvas not found."
        );

        return;

    }


    const pingFloods =
        Number(
            pieCanvas.dataset.ping || 0
        );


    const synScans =
        Number(
            pieCanvas.dataset.syn || 0
        );


    const synFloods =
        Number(
            pieCanvas.dataset.synflood || 0
        );


    const icmpSweeps =
        Number(
            pieCanvas.dataset.icmp || 0
        );


    const udpScans =
        Number(
            pieCanvas.dataset.udp || 0
        );


    // ========================================================
    // PIE CHART
    // ========================================================

    attackChart =
        new Chart(
            pieCanvas,
            {

                type: "pie",

                data: {

                    labels: [

                        "Ping Flood",
                        "TCP SYN Scan",
                        "TCP SYN Flood",
                        "ICMP Sweep",
                        "UDP Scan"

                    ],

                    datasets: [{

                        label:
                            "Attack Distribution",

                        data: [

                            pingFloods,
                            synScans,
                            synFloods,
                            icmpSweeps,
                            udpScans

                        ],

                        borderWidth: 1

                    }]

                },

                options: {

                    responsive: true,

                    maintainAspectRatio: true,

                    animation: {

                        duration: 500

                    },

                    plugins: {

                        legend: {

                            position: "bottom"

                        }

                    }

                }

            }
        );


    // ========================================================
    // BAR CHART
    // ========================================================

    barChart =
        new Chart(
            barCanvas,
            {

                type: "bar",

                data: {

                    labels: [

                        "Ping Flood",
                        "TCP SYN Scan",
                        "TCP SYN Flood",
                        "ICMP Sweep",
                        "UDP Scan"

                    ],

                    datasets: [{

                        label:
                            "Alerts",

                        data: [

                            pingFloods,
                            synScans,
                            synFloods,
                            icmpSweeps,
                            udpScans

                        ],

                        borderWidth: 1

                    }]

                },

                options: {

                    responsive: true,

                    maintainAspectRatio: true,

                    animation: {

                        duration: 500

                    },

                    scales: {

                        y: {

                            beginAtZero: true,

                            ticks: {

                                precision: 0

                            }

                        }

                    }

                }

            }
        );

}


// ============================================================
// UPDATE ALERT TABLE
// ============================================================

function updateAlertTable(alerts) {

    const tbody =
        document.getElementById(
            "alerts-body"
        );


    if (!tbody) {
        return;
    }


    const signature =
        JSON.stringify(alerts);


    if (
        signature === lastAlertSignature
    ) {

        return;

    }


    lastAlertSignature =
        signature;


    tbody.innerHTML = "";


    alerts
        .slice(0, 10)
        .forEach(function(alert) {

            const normalized =
                normalizeAlert(alert);


            if (!normalized) {
                return;
            }


            const data =
                normalized.data;


            if (
                !data ||
                data.length < 7
            ) {

                return;

            }


            const row =
                document.createElement(
                    "tr"
                );


            // =================================================
            // TIME
            // =================================================

            const timeCell =
                document.createElement(
                    "td"
                );

            timeCell.innerText =
                data[0];


            // =================================================
            // SEVERITY
            // =================================================

            const severityCell =
                document.createElement(
                    "td"
                );


            const severitySpan =
                document.createElement(
                    "span"
                );


            severitySpan.innerText =
                data[1];


            if (data[1] === "High") {

                severitySpan.className =
                    "high";

            }

            else if (
                data[1] === "Medium"
            ) {

                severitySpan.className =
                    "medium";

            }

            else if (
                data[1] === "Low"
            ) {

                severitySpan.className =
                    "low";

            }


            severityCell.appendChild(
                severitySpan
            );


            // =================================================
            // ATTACK
            // =================================================

            const attackCell =
                document.createElement(
                    "td"
                );


            attackCell.innerText =
                data[2];


            // =================================================
            // SOURCE IP
            // =================================================

            const sourceCell =
                document.createElement(
                    "td"
                );


            sourceCell.innerText =
                data[3];


            // =================================================
            // DESTINATION IP
            // =================================================

            const destinationCell =
                document.createElement(
                    "td"
                );


            destinationCell.innerText =
                data[4];


            // =================================================
            // SOURCE PORT
            // =================================================

            const sourcePortCell =
                document.createElement(
                    "td"
                );


            sourcePortCell.innerText =
                data[5];


            // =================================================
            // DESTINATION PORT
            // =================================================

            const destinationPortCell =
                document.createElement(
                    "td"
                );


            destinationPortCell.innerText =
                data[6];


            // =================================================
            // AI BUTTON
            // =================================================

            const aiCell =
                document.createElement(
                    "td"
                );


            const aiButton =
                document.createElement(
                    "button"
                );


            aiButton.className =
                "ai-analyze-btn";


            aiButton.innerText =
                "🤖 Analyze";


            aiButton.addEventListener(
                "click",
                function() {

                    analyzeAlert(
                        data
                    );

                }
            );


            aiCell.appendChild(
                aiButton
            );


            // =================================================
            // MITRE CELL
            // =================================================

            const mitreCell =
                document.createElement(
                    "td"
                );


            const mitreTechnique =
                normalized.mitre_technique;


            const mitreName =
                normalized.mitre_name;


            if (
                mitreTechnique &&
                mitreTechnique !== "N/A"
            ) {

                mitreCell.innerText =
                    mitreTechnique +
                    " - " +
                    mitreName;

            }

            else {

                mitreCell.innerText =
                    "N/A";

            }


            // =================================================
            // ADD CELLS
            // =================================================

            row.appendChild(
                timeCell
            );

            row.appendChild(
                severityCell
            );

            row.appendChild(
                attackCell
            );

            row.appendChild(
                sourceCell
            );

            row.appendChild(
                destinationCell
            );

            row.appendChild(
                sourcePortCell
            );

            row.appendChild(
                destinationPortCell
            );

            row.appendChild(
                mitreCell
            );

            row.appendChild(
                aiCell
            );


            tbody.appendChild(
                row
            );

        });

}


// ============================================================
// LIVE ALERT LOADING
// ============================================================

async function loadAlerts() {

    try {

        const response =
            await fetch(
                "/api/alerts",
                {
                    method: "GET",
                    cache: "no-store"
                }
            );


        if (!response.ok) {

            throw new Error(
                "API request failed"
            );

        }


        const alerts =
            await response.json();


        console.log(
            "Live alerts:",
            alerts
        );


        // ====================================================
        // SEVERITY
        // ====================================================

        updateSeverityStats(
            alerts
        );


        // ====================================================
        // FILTERS
        // ====================================================

        const params =
            new URLSearchParams(
                window.location.search
            );


        const attackFilter =
            params.get("attack");


        const ipFilter =
            params.get("ip");


        let filteredAlerts =
            alerts;


        // ====================================================
        // ATTACK FILTER
        // ====================================================

        if (attackFilter) {

            filteredAlerts =
                filteredAlerts.filter(
                    function(alert) {

                        const normalized =
                            normalizeAlert(
                                alert
                            );


                        return (
                            normalized &&
                            normalized.data[2]
                            ===
                            attackFilter
                        );

                    }
                );

        }


        // ====================================================
        // IP FILTER
        // ====================================================

        if (ipFilter) {

            filteredAlerts =
                filteredAlerts.filter(
                    function(alert) {

                        const normalized =
                            normalizeAlert(
                                alert
                            );


                        if (!normalized) {
                            return false;
                        }


                        const data =
                            normalized.data;


                        return (
                            data[3].includes(
                                ipFilter
                            )
                            ||
                            data[4].includes(
                                ipFilter
                            )
                        );

                    }
                );

        }


        // ====================================================
        // STATISTICS
        // ====================================================

        const stats =
            calculateStatistics(
                alerts
            );


        updateStatistics(
            stats
        );


        // ====================================================
        // CHARTS
        // ====================================================

        updatePieChart(
            stats
        );


        updateBarChart(
            stats
        );


        // ====================================================
        // TABLE
        // ====================================================

        updateAlertTable(
            filteredAlerts
        );

    }

    catch (error) {

        console.error(
            "Live alert update error:",
            error
        );

    }

}


// ============================================================
// DISPLAY AI ANALYSIS
// ============================================================

function displayAIAnalysis(result) {

    const container =
        document.getElementById(
            "ai-analysis-container"
        );


    const summary =
        document.getElementById(
            "ai-threat-summary"
        );


    const whyMatters =
        document.getElementById(
            "ai-why-matters"
        );


    const mitre =
        document.getElementById(
            "ai-mitre"
        );


    const actions =
        document.getElementById(
            "ai-actions"
        );


    if (!container) {
        return;
    }


    container.style.display =
        "block";


    if (summary) {

        summary.innerText =
            result.threat_summary
            ||
            result.summary
            ||
            "No summary available.";

    }


    if (whyMatters) {

        whyMatters.innerText =
            result.why_it_matters
            ||
            result.why_matters
            ||
            "No information available.";

    }


    if (mitre) {

        if (result.mitre_technique) {

            mitre.innerText =
                result.mitre_technique +
                (
                    result.mitre_name
                    ?
                    " - " +
                    result.mitre_name
                    :
                    ""
                );

        }

        else {

            mitre.innerText =
                "No MITRE ATT&CK technique identified.";

        }

    }


    if (actions) {

        actions.innerHTML = "";


        if (
            Array.isArray(
                result.recommended_actions
            )
        ) {

            result.recommended_actions
                .forEach(
                    function(action) {

                        const li =
                            document.createElement(
                                "li"
                            );


                        li.innerText =
                            action;


                        actions.appendChild(
                            li
                        );

                    }
                );

        }

        else {

            const li =
                document.createElement(
                    "li"
                );


            li.innerText =
                "No recommended actions returned.";


            actions.appendChild(
                li
            );

        }

    }

}


// ============================================================
// ANALYZE ALERT
// ============================================================

async function analyzeAlert(alert) {

    const container =
        document.getElementById(
            "ai-analysis-container"
        );


    const summary =
        document.getElementById(
            "ai-threat-summary"
        );


    const whyMatters =
        document.getElementById(
            "ai-why-matters"
        );


    const mitre =
        document.getElementById(
            "ai-mitre"
        );


    const actions =
        document.getElementById(
            "ai-actions"
        );


    if (container) {

        container.style.display =
            "block";

    }


    if (summary) {

        summary.innerText =
            "⏳ Analyzing alert with Qwen AI...";

    }


    if (whyMatters) {

        whyMatters.innerText =
            "";

    }


    if (mitre) {

        mitre.innerText =
            "";

    }


    if (actions) {

        actions.innerHTML =
            "";

    }


    try {

        const response =
            await fetch(
                "/api/analyze",
                {

                    method: "POST",

                    headers: {

                        "Content-Type":
                            "application/json"

                    },

                    body:
                        JSON.stringify({

                            timestamp:
                                alert[0],

                            severity:
                                alert[1],

                            attack:
                                alert[2],

                            source_ip:
                                alert[3],

                            destination_ip:
                                alert[4],

                            source_port:
                                alert[5],

                            destination_port:
                                alert[6]

                        })

                }
            );


        const result =
            await response.json();


        if (result.error) {

            if (summary) {

                summary.innerText =
                    "❌ AI analysis failed: " +
                    result.error;

            }

            return;

        }


        localStorage.setItem(

            "ai_analysis_" +
            JSON.stringify(alert),

            JSON.stringify(result)

        );


        localStorage.setItem(

            "last_analyzed_alert",

            JSON.stringify(alert)

        );


        displayAIAnalysis(
            result
        );

    }

    catch (error) {

        console.error(
            "AI Analysis Error:",
            error
        );


        if (summary) {

            summary.innerText =
                "❌ Unable to connect to AI analyzer.";

        }

    }

}


// ============================================================
// CONNECT EXISTING AI BUTTONS
// ============================================================

function connectAnalyzeButtons() {

    const buttons =
        document.querySelectorAll(
            ".ai-analyze-btn"
        );


    buttons.forEach(
        function(button) {

            if (
                button.dataset.connected
                ===
                "true"
            ) {

                return;
            }


            button.dataset.connected =
                "true";


            button.addEventListener(
                "click",
                function() {

                    try {

                        const alert =
                            JSON.parse(
                                this.dataset.alert
                            );


                        analyzeAlert(
                            alert
                        );

                    }

                    catch (error) {

                        console.error(
                            "Invalid alert data:",
                            error
                        );

                    }

                }
            );

        }
    );

}


// ============================================================
// RESTORE LAST AI ANALYSIS
// ============================================================

function restoreLastAnalysis() {

    const savedAlert =
        localStorage.getItem(
            "last_analyzed_alert"
        );


    if (!savedAlert) {
        return;
    }


    try {

        const alert =
            JSON.parse(
                savedAlert
            );


        const savedAnalysis =
            localStorage.getItem(
                "ai_analysis_" +
                JSON.stringify(alert)
            );


        if (!savedAnalysis) {
            return;
        }


        const result =
            JSON.parse(
                savedAnalysis
            );


        displayAIAnalysis(
            result
        );

    }

    catch (error) {

        console.error(
            "Could not restore AI analysis:",
            error
        );

    }

}


// ============================================================
// INITIALIZATION
// ============================================================

document.addEventListener(
    "DOMContentLoaded",
    function() {

        console.log(
            "AI-SOC Dashboard initialized."
        );


        initializeCharts();


        connectAnalyzeButtons();


        restoreLastAnalysis();


        loadAlerts();

    }
);


// ============================================================
// REALTIME POLLING
// ============================================================

// Every 2 seconds

setInterval(
    loadAlerts,
    2000
);