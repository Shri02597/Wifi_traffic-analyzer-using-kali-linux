📡 Wi-Fi Traffic Monitoring System

** Overview:**
This project is a Wi-Fi Traffic Monitoring System that captures and analyzes wireless network packets in real time. It identifies active devices and displays network statistics through a web-based dashboard.



 **Objectives:**
- Capture Wi-Fi packets in real time  
- Analyze network traffic  
- Identify unique active clients  
- Display results on a dashboard  

---

 **Features:**
- Real-time packet monitoring  
- Detection of active devices (MAC addresses)  
- Live dashboard display  
- Device activity tracking  

---

**Technologies Used:**
- Python  
- Flask  
- Scapy  
- HTML, CSS, JavaScript  
- Kali Linux  

  **Working:**
1. Enable monitor mode on Wi-Fi adapter  
2. Capture packets using Scapy  
3. Extract MAC addresses from packets  
4. Process and send data to Flask server  
5. Display real-time data on dashboard

  ** Run Commands (Kali Linux)**

1. Update system
sudo apt update

2. Install Python (if not installed)
sudo apt install python3 python3-pip -y

3. Install project dependencies
pip install flask scapy

4. Check wireless interface
iwconfig

5. Kill interfering processes
sudo airmon-ng check kill

6. Enable monitor mode
sudo airmon-ng start wlan0

(After this, interface becomes wlan0mon)

7. Verify monitor mode
iwconfig

8. Run the project
sudo python app.py

9. Open dashboard in browser
http://127.0.0.1:5000


**Stop Monitor Mode (After Use)**

Stop monitor interface
sudo airmon-ng stop wlan0mon

Restart network services
sudo service NetworkManager restart
<img width="1916" height="839" alt="Screenshot 2026-02-28 001836" src="https://github.com/user-attachments/assets/c71cb506-0407-4c1f-a0a6-62d4deecb1f5" />

