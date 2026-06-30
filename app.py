from flask import Flask, render_template
from network_dashboard import get_local_ip, get_gateway, get_dns, get_cpu_usage, get_ram_usage
app= Flask(__name__)

@app.route("/")
def home():
    local_ip= get_local_ip()
    gateway= get_gateway()
    dns= get_dns()
    cpu= get_cpu_usage()
    ram= get_ram_usage()

    return render_template("dashboard.html",
     local_ip= local_ip,
     gateway=gateway,
     dns=dns, 
     cpu=cpu, 
     ram=ram)
if __name__=="__main__":
    app.run(debug=True)