#  Personal SOC Dashboard

A full-stack security operations dashboard that brings together the tools a SOC (Security Operations Center) analyst uses daily-IP/URL/hash reputation checks, WHOIS and DNS lookups, a live CVE feed, and a personal indicator-of-compromise (IOC) tracker-all in one clean, dark-themed web interface.

**🔗 Live demo:** [personal-soc-dashboard.onrender.com](https://personal-soc-dashboard.onrender.com)

> Note: the live app runs on a free hosting tier, so the first request after a period of inactivity may take 20–30 seconds to wake up. Subsequent requests are fast.

##  Features

| Module | What it does |
|---|---|
| **Dashboard** | Live overview-active IOC count, module status, and the 3 most recent CVEs at a glance |
| **IP Reputation** | Checks any IP against [AbuseIPDB](https://www.abuseipdb.com/) - abuse score, ISP, country, Tor exit node detection |
| **Hash Lookup** | Checks a file hash (MD5/SHA1/SHA256) against [VirusTotal](https://www.virustotal.com/)- detection counts across 60+ antivirus engines |
| **URL Checker** | Submits a URL to VirusTotal and polls asynchronously until the scan completes |
| **WHOIS Lookup** | Domain registration info-registrar, creation/expiry dates, name servers |
| **DNS Lookup** | Resolves A, MX, NS, and TXT records for any domain |
| **Recent CVEs** | Live feed of recently published vulnerabilities from the [NVD API](https://nvd.nist.gov/), with severity badges |
| **IOC Manager** | Add, view, and delete your own tracked indicators-backed by a persistent PostgreSQL database |

---

##  Tech Stack

- **Backend:** Python, Flask
- **Templating:** Jinja2 (with template inheritance for a shared sidebar/layout)
- **Database:** PostgreSQL, hosted on [Supabase](https://supabase.com/)
- **Deployment:** [Render](https://render.com/) (Gunicorn as the production WSGI server)
- **APIs:** AbuseIPDB, VirusTotal, NVD (National Vulnerability Database)
- **Libraries:** `requests`, `python-whois`, `dnspython`, `psycopg2`, `python-dotenv`

---

##  What I Learned Building This

This was my first full-stack project, built from scratch to practice real networking and cybersecurity concepts alongside web development:

- Consuming REST APIs with authentication headers, query parameters, and JSON parsing
- Handling **asynchronous APIs** (submit → poll → retrieve pattern, used in the URL checker)
- Flask routing, forms (GET vs POST), and Jinja2 templating/inheritance
- Relational databases- first with SQLite, then migrated to PostgreSQL for persistent cloud storage
- Defensive coding with `try/except` for unpredictable real-world API responses
- Environment variables and `.env` files for keeping API keys and credentials out of source control
- Deploying a Python web app to production with Gunicorn and a managed database

---

##  Running Locally

1. **Clone the repo and navigate into the project folder:**
   ```bash
   git clone https://github.com/arpitasen060605/Networking-Cybersecurity-Journey-.git
   cd Networking-Cybersecurity-Journey-/personal-soc-dashboard
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\Activate.ps1
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in this folder with the following:
   ```
   ABUSEIPDB_API_KEY=your_abuseipdb_key
   VIRUSTOTAL_API_KEY=your_virustotal_key
   DATABASE_URL=your_postgresql_connection_string
   ```
   Free API keys can be obtained from [AbuseIPDB](https://www.abuseipdb.com/register) and [VirusTotal](https://www.virustotal.com/gui/join-us). A free PostgreSQL database can be created on [Supabase](https://supabase.com/).

5. **Run the app:**
   ```bash
   python soc_app.py
   ```
   Visit `http://127.0.0.1:5000` in your browser.

---

##  Known Limitations

- **Free-tier cold starts:** The live demo sleeps after inactivity (Render free tier)-the first load may be slow.
- **No authentication:** This is a personal/demo tool, not intended for handling real production security data- there's no login system protecting the IOC Manager.
- **CVE severity gaps:** Some very recently published CVEs don't yet have a CVSS severity score assigned by NVD, and will show as "Unknown."

---

##  Project Status

All planned modules are complete and deployed. Possible future additions: GeoIP mapping with visual location data, user authentication, and email/Slack alerting for high-severity CVE matches against a tracked software inventory.