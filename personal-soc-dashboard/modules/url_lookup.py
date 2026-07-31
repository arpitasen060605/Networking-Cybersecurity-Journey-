import os
import requests
import time
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
def check_url(target_url):
    submit_endpoint = "http://www.virustotal.com/api/v3/urls"
    headers = {
        "x-apikey": API_KEY
    }
    data = {
        "url": target_url
    }
    submit_response = requests.post(submit_endpoint, headers=headers, data=data)
    print(submit_response.status_code)
    print(submit_response.json())
if __name__ == "__main__":
    check_url("http://example.com")