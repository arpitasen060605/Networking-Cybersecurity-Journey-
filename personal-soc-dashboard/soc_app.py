from flask import Flask, render_template, request, redirect 
from modules.ip_lookup import check_ip
from modules.hash_lookup import check_hash
from modules.url_lookup import check_url 
from modules.whois_lookup import check_whois
from modules.dns_lookup import check_dns
from modules.cve_feed import get_recent_cves
from modules.ioc_db import init_db, add_ioc, get_all_iocs, delete_ioc

init_db()

app = Flask(__name__)

@app.route("/ip", methods=["GET", "POST"])
def home():
   result= None
   if request.method == "POST":
        ip_address= request.form["ip_address"]
        result = check_ip(ip_address)
   return render_template("index.html", result=result)

@app.route("/")
def dashboard():
    ioc_count = len(get_all_iocs())
    recent_cves = get_recent_cves(limit=3)
    return render_template("dashboard.html", ioc_count=ioc_count, recent_cves=recent_cves)

@app.route("/hash", methods= ["GET", "POST"])
def hash_page():
    result = None
    if request.method == "POST":
        file_hash = request.form["file_hash"]
        result= check_hash(file_hash)
    return render_template("hash.html", result= result)

@app.route("/url", methods=["GET", "POST"])
def url_page():
    result = None
    if request.method == "POST":
        target_url = request.form["target_url"]
        result = check_url(target_url)
    return render_template("url.html", result=result)

@app.route("/dns", methods=["GET", "POST"])
def dns_page():
    result = None
    if request.method == "POST":
        domain = request.form["domain"]
        result = check_dns(domain)
    return render_template("dns.html", result=result)


@app.route("/ioc", methods=["GET", "POST"])
def ioc_page():
    if request.method == "POST":
        indicator = request.form["indicator"]
        ioc_type = request.form["type"]
        threat_level = request.form["threat_level"]
        notes = request.form["notes"]
        add_ioc(indicator, ioc_type, threat_level, notes)

    all_iocs = get_all_iocs()
    return render_template("ioc.html", iocs=all_iocs)

@app.route("/whois", methods=["GET", "POST"])
def whois_page():
    result = None
    if request.method == "POST":
        domain = request.form["domain"]
        result = check_whois(domain)
    return render_template("whois.html", result=result)
@app.route("/cves")
def cve_page():
    cves = get_recent_cves()
    return render_template("cves.html", cves=cves)

@app.route("/ioc/delete/<int:ioc_id>")
def delete_ioc_route(ioc_id):
    delete_ioc(ioc_id)
    return redirect("/ioc")

if __name__ == "__main__":
    app.run(debug=True)
