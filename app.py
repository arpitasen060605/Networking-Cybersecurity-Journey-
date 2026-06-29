from flask import Flask
from network_dashboard import get_local_ip, get_gateway, get_dns, get_cpu_usage, get_ram_usage
app= Flask(__name__)

@app.route("/")
def home():
    local_ip= get_local_ip()
    gateway= get_gateway()
    dns= get_dns()
    cpu= get_cpu_usage()
    ram= get_ram_usage()
      
    print(f"DEBUG: gateway value= '{gateway}'")

    html=f"""
    <h1>Network Monitoring Dashboard</h1>
    <p>Local IP: {local_ip}</p>
    <p>Gateway: {gateway}</p>
    <p>DNS: {dns}</p>
    <p>CPU Usage:{cpu}%</p>
    <p>RAM Usage: {ram}%</p>
    """
    return html
if __name__=="__main__":
    app.run(debug=True)