from flask import Flask, render_template_string, jsonify
from scapy.all import sniff, Dot11
from collections import defaultdict
import threading

app = Flask(__name__)

# Data storage
packet_count = 0
device_data = defaultdict(int)

# Packet processing function
def handle_packet(pkt):
    global packet_count
    
    if pkt.haslayer(Dot11):
        packet_count += 1
        
        mac = pkt.addr2
        if mac:
            device_data[mac] += 1

# Start sniffing
def start_sniffing():
    sniff(prn=handle_packet, store=False)

# Run sniffer in background
thread = threading.Thread(target=start_sniffing, daemon=True)
thread.start()

# HTML Dashboard (inline)
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Wi-Fi Traffic Monitor</title>
    <style>
        body {
            font-family: Arial;
            background: #f0f2f5;
            text-align: center;
        }
        h1 {
            margin-top: 20px;
        }
        .card {
            display: inline-block;
            background: white;
            padding: 20px;
            margin: 10px;
            border-radius: 10px;
        }
        table {
            margin: auto;
            border-collapse: collapse;
            width: 60%;
            background: white;
        }
        th, td {
            padding: 10px;
            border: 1px solid #ccc;
        }
    </style>
</head>
<body>

<h1>Wi-Fi Traffic Monitoring Dashboard</h1>

<div class="card">
    <h2>Total Packets</h2>
    <p id="packets">0</p>
</div>

<div class="card">
    <h2>Unique Active Clients</h2>
    <p id="clients">0</p>
</div>

<h2>Device Activity</h2>

<table>
    <thead>
        <tr>
            <th>MAC Address</th>
            <th>Packets</th>
        </tr>
    </thead>
    <tbody id="tableData"></tbody>
</table>

<script>
async function loadData() {
    const res = await fetch('/data');
    const data = await res.json();

    document.getElementById('packets').innerText = data.packet_count;
    document.getElementById('clients').innerText = Object.keys(data.devices).length;

    let rows = "";
    for (let mac in data.devices) {
        rows += `<tr><td>${mac}</td><td>${data.devices[mac]}</td></tr>`;
    }

    document.getElementById('tableData').innerHTML = rows;
}

setInterval(loadData, 1000);
</script>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/data')
def data():
    return jsonify({
        "packet_count": packet_count,
        "devices": dict(device_data)
    })

if __name__ == "__main__":
    app.run(debug=True)
