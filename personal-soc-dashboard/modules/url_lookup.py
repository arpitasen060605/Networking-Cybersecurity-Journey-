import os
import requests
import time
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

def check_url(target_url):
    submit_endpoint = "https://www.virustotal.com/api/v3/urls"
    headers = {
        "x-apikey": API_KEY
    }
    data = {
        "url": target_url
    }
    submit_response = requests.post(submit_endpoint, headers=headers, data=data)
    submit_result = submit_response.json()
    analysis_id = submit_result["data"]["id"]

    analysis_endpoint = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"

    while True:
        analysis_response = requests.get(analysis_endpoint, headers=headers)
        analysis_result = analysis_response.json()
        status = analysis_result["data"]["attributes"]["status"]

        if status == "completed":
            break

        print("Scan still in progress, waiting 5 seconds...")
        time.sleep(5)

    stats = analysis_result["data"]["attributes"]["stats"]

    return {
        "url": target_url,
        "malicious": stats["malicious"],
        "suspicious": stats["suspicious"],
        "harmless": stats["harmless"],
        "undetected": stats["undetected"]
    }

if __name__ == "__main__":
    print(check_url("http://example.com"))