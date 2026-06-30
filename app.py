from flask import Flask, render_template, render_template, request 
from network_dashboard import (get_local_ip, get_gateway, get_dns, get_cpu_usage, get_ram_usage, get_network_prefix, get_connected_devices, get_open_ports, get_latency_and_loss)
app= Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    local_ip= get_local_ip()
    gateway= get_gateway()
    dns= get_dns()
    cpu= get_cpu_usage()
    ram= get_ram_usage()

    network_prefix= get_network_prefix(local_ip)
    devices= get_connected_devices(network_prefix)

    avg_latency, packet_loss = get_latency_and_loss()

    open_ports= None
    selected_device= None

    if request.method== "POST":
       selected_device= request.form.get("device")
       if selected_device:
          open_ports= get_open_ports(selected_device)

    return render_template("dashboard.html",
     local_ip= local_ip,
     gateway=gateway,
     dns=dns, 
     cpu=cpu, 
     ram=ram,
    devices= devices,
    open_ports=open_ports,
    selected_device= selected_device,
    avg_latency= avg_latency,
    packet_loss= packet_loss
    )
if __name__=="__main__":
    app.run(debug=True)