import os
import requests
from dotenv import load_dotenv
load_dotenv()
API_KEY= os.getenv("VIRUSTOTAL_API_KEY")

def check_hash(file_hash):
     url= f"https://www.virustotal.com/api/v3/files/{file_hash}"
     headers= {
          "x-apikey": API_KEY
     }
     response= requests.get(url,headers= headers)
     print(response.status_code)
     result= response.json()
     attributes= result["data"]["attributes"]
     stats= attributes["last_analysis_stats"]
     return {
          "hash": file_hash,
          "malicious": stats["malicious"],
          "suspicious": stats["suspicious"],
          "harmless": stats["harmless"],
          "undetected": stats["undetected"],
          "file_type": attributes.get("type_description", "Unknown"),
          "file_name": attributes.get("meaningful_name", "Unknown")
     }
if __name__ == "__main__": 
     print(check_hash("275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"))
