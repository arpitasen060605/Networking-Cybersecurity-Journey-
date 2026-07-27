from flask import Flask, render_template, request
from modules.ip_lookup import check_ip
from modules.hash_lookup import check_hash

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
   result= None
   if request.method == "POST":
        ip_address= request.form["ip_address"]
        result = check_ip(ip_address)
   return render_template("index.html", result=result)

@app.route("/hash", methods= ["GET", "POST"])
def hash_page():
    result = None
    if request.method == "POST":
        file_hash = request.form["file_hash"]
        result= check_hash(file_hash)
    return render_template("hash.html", result= result)

if __name__ == "__main__":
    app.run(debug=True)
