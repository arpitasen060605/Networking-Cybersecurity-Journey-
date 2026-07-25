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
    return{
        "ip": ip_data["ipAddress"],
        "abuse_score": ip_data["abuseConfidenceScore"],
        "country": ip_data["countryCode"],
        "isp": ip_data["isp"],
        "total_reports": ip_data["totalReports"],
        "is_tor": ip_data["isTor"]
    }


if __name__ == "__main__":
    print(check_ip("185.220.101.1"))