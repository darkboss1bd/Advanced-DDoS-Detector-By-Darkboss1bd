import argparse
import time
import threading
import geoip2.database
import requests
from datetime import datetime
from colorama import Fore, Style, init
import pyfiglet
import pandas as pd
import os
import sys

init(autoreset=True)  # Enable colored terminal output

class DarkBoss1bdDDOSDetector:
    def __init__(self):
        self.brand = "darkboss1bd"
        self.geoip_reader = geoip2.database.Reader('GeoLite2-City.mmdb')
        self.ip_counts = {}
        self.suspicious_ips = set()
        self.threshold = 100
        self.proxies = {}  # For proxy support
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

    def show_banner(self):
        """Display ASCII art banner."""
        banner = pyfiglet.figlet_format("DARKBOSS1BD", font="slant")
        print(Fore.RED + banner)
        print(Fore.CYAN + "🔥 Advanced DDoS Detector | Made in Bangladesh 🔥\n")

    def fetch_logs_from_url(self, url):
        """Simulate fetching logs from a website (modify as per API)."""
        try:
            headers = {"User-Agent": self.user_agent}
            response = requests.get(url, headers=headers, proxies=self.proxies)
            if response.status_code == 200:
                return response.text.split('\n')  # Replace with actual log parsing
            else:
                print(Fore.RED + f"[!] Error: Failed to fetch logs (HTTP {response.status_code})")
                return []
        except Exception as e:
            print(Fore.RED + f"[!] Error: {e}")
            return []

    def analyze_ips(self, logs):
        """Detect suspicious IPs based on request threshold."""
        for log in logs:
            if log.strip():
                ip = log.strip().split()[0]  # Extract IP (adjust as per log format)
                self.ip_counts[ip] = self.ip_counts.get(ip, 0) + 1
                if self.ip_counts[ip] > self.threshold:
                    self.suspicious_ips.add(ip)
                    print(Fore.YELLOW + f"[!] Suspicious IP: {ip} (Requests: {self.ip_counts[ip]})")

    def get_geolocation(self, ip):
        """Get country/city details for an IP."""
        try:
            response = self.geoip_reader.city(ip)
            return f"{response.country.name}, {response.city.name}"
        except:
            return "Unknown"

    def generate_report(self):
        """Export findings in TXT & HTML formats."""
        if not self.suspicious_ips:
            print(Fore.GREEN + "[+] No DDoS attack detected.")
            return

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        txt_report = f"ddos_report_{timestamp}.txt"
        html_report = f"ddos_report_{timestamp}.html"

        # TXT Report
        with open(txt_report, 'w') as f:
            f.write(f"[{self.brand}] DDoS Detection Report - {timestamp}\n")
            f.write("-" * 50 + "\n")
            for ip in self.suspicious_ips:
                geo = self.get_geolocation(ip)
                f.write(f"IP: {ip}\nRequests: {self.ip_counts[ip]}\nLocation: {geo}\n")
                f.write("-" * 20 + "\n")

        # HTML Report (Pandas)
        df = pd.DataFrame({
            "IP": list(self.suspicious_ips),
            "Requests": [self.ip_counts[ip] for ip in self.suspicious_ips],
            "Location": [self.get_geolocation(ip) for ip in self.suspicious_ips]
        })
        df.to_html(html_report, index=False)

        print(Fore.GREEN + f"\n[+] Reports saved:\n- TXT: {txt_report}\n- HTML: {html_report}")

def main():
    parser = argparse.ArgumentParser(description="darkboss1bd - Advanced DDoS Detector")
    parser.add_argument("--url", help="Website URL to fetch logs", required=False)
    parser.add_argument("--log", help="Local log file path", required=False)
    parser.add_argument("--threshold", type=int, help="Request threshold for DDoS alert", default=100)
    args = parser.parse_args()

    detector = DarkBoss1bdDDOSDetector()
    detector.show_banner()
    detector.threshold = args.threshold

    if args.url:
        logs = detector.fetch_logs_from_url(args.url)
        print(Fore.GREEN + "[*] Analyzing web traffic...")
        detector.analyze_ips(logs)
        detector.generate_report()
    elif args.log:
        if os.path.exists(args.log):
            with open(args.log, 'r') as f:
                detector.analyze_ips(f.readlines())
            detector.generate_report()
        else:
            print(Fore.RED + f"[!] Error: File '{args.log}' not found.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
