# Advanced-DDoS-Detector-By-Darkboss1bd
DDOS attack on any website, you can find out through these tools.


## Clone
```
bash
git clone https://github.com/darkboss1bd/Advanced-DDoS-Detector-By-Darkboss1bd.git
cd Advanced-DDoS-Detector-By-Darkboss1bd
```

## Usage: 
```
bash
Monitor a Website URL:
python darkboss1bd_ddos.py --url https://example.com/access.log --threshold 150
(Modify fetch_logs_from_url() to match your target API.)
Scan a Local Log File:
python darkboss1bd_ddos.py --log /var/log/nginx/access.log

```




## 🛠 Setup Guide:
Install Required Libraries:
pip install geoip2 requests colorama pyfiglet pandas
Download GeoLite2-City.mmdb from MaxMind and place it in your script directory.


```
bash
🔥 Features:
Real-Time Traffic Monitoring (from logs or website URLs)
IP Geolocation Tracking (Country + City detection via MaxMind GeoLite2)
Hacker-Style Terminal UI (ASCII art + colored output)
Automated Reports (HTML & TXT formats)
Multi-Threaded Scanning (Faster analysis)
Custom Thresholds (Adjustable request limit)
```
