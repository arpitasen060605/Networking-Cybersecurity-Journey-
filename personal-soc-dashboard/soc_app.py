from flask import Flask, render_template, request
from modules.ip_lookup import check_ip

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
   result= None
   if request.method == "POST":
        ip_address= request.form["ip_address"]
        result = check_ip(ip_address)
   return render_template("index.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)