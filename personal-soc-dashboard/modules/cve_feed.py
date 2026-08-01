import requests
from datetime import datetime, timedelta, timezone

def get_recent_cves(limit=10):
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

    end_date = datetime.now(timezone.utc)
    start_date = end_date - timedelta(days=30)

    params = {
        "resultsPerPage": limit,
        "pubStartDate": start_date.strftime("%Y-%m-%dT%H:%M:%S.000"),
        "pubEndDate": end_date.strftime("%Y-%m-%dT%H:%M:%S.000")
    }

    response = requests.get(url, params=params)
    result = response.json()

    cve_list = []
    for item in result["vulnerabilities"]:
        cve_data = item["cve"]
        cve_id = cve_data["id"]

        descriptions = cve_data["descriptions"]
        description_text = descriptions[0]["value"]

        try:
            severity = cve_data["metrics"]["cvssMetricV31"][0]["cvssData"]["baseSeverity"]
        except (KeyError, IndexError):
            severity = "Unknown"

        cve_list.append({
            "id": cve_id,
            "description": description_text,
            "severity": severity
        })

    return cve_list

if __name__ == "__main__":
    cves = get_recent_cves()
    for cve in cves:
        print(cve)