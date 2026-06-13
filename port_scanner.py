import socket
import datetime
COMMON_PORTS= {21:"FTP",22:"SSH",23:"Telnet",25:"SMTP",53:"DNS",80:"HTTP",110:"POP3",135:"Windows RPC",143:"IMAP",443:"HTTPS",445:" WindowsSMB",3306:"MySQL",3389:"RDP",5040:"Windows Service",8080:"HTTP-Alt"}
print("\n Simple Port Scanner")
print(" "+"-"*28)
target=input("Enter an IP Address to scan: ").strip()
try:
   ip=socket.gethostbyname(target)
except socket.gaierror:
    print(f"Unable to resolve {target} . Please check the IP address")
    exit()
print(f"\n Target: {ip}")
print(f"Ports: 1-1024")
print(f"Started: {datetime.datetime.now().strftime('%H:%M:%S')}")
print(" "+"-"*28)
open_ports= []
for port in range(1,1025):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
     sock.settimeout(0.05)
     result= sock.connect_ex((ip, port))
     if result==0:
        service=COMMON_PORTS.get(port, "Uknown")
        open_ports.append((port, service))
        print(f"[OPEN] Port {port}- {service}")
print(" "+"-"*28)
print(f"\n Scan Complete")
print(f"Open ports found : {len(open_ports)}")
print(f" Finished at: {datetime.datetime.now().strftime('%H:%M:%S')}\n")