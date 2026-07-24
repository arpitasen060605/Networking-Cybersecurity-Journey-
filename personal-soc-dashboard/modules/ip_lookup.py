import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ABUSEIPDB_API_KEY")

def check_ip(ip_address):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }
    params = {
        "ipAddress": ip_address,
        "maxAgeInDays": 90
    }
    response = requests.get(url, headers=headers, params=params)
    print(response.status_code)
    result = response.json()
    ip_data= result["data"]
    print("IP:", ip_data["ipAddress"])
    print("Abuse Score:", ip_data["abuseConfidenceScore"],"/100")
    print("Country:", ip_data["countryCode"])
    print("ISP:", ip_data["isp"])
    print("Total Reports:", ip_data["totalReports"])
    print("Is Tor:", ip_data["isTor"]) 

if __name__ == "__main__":
    check_ip("185.220.101.1")