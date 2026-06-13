import socket
import datetime
import threading 
COMMON_PORTS= {21:"FTP",22:"SSH",23:"Telnet",25:"SMTP",53:"DNS",80:"HTTP",110:"POP3",135:"Windows RPC",143:"IMAP",443:"HTTPS",445:" WindowsSMB",3306:"MySQL",3389:"RDP",5040:"Windows Service",8080:"HTTP-Alt"}
open_ports = []
lock= threading.Lock()
def scan_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
     sock.settimeout(0.05)
     result= sock.connect_ex((ip, port))
     if result==0:
        service=COMMON_PORTS.get(port, "Unknown")
        with lock:
         open_ports.append((port, service))
         print(f"[OPEN] Port {port}- {service}")
print("\n Simple Port Scanner(Threaded)")
print(" "+"-"*30)
target=input("Enter an IP Address to scan: ").strip()
try:
   ip=socket.gethostbyname(target)
except socket.gaierror:
    print(f"Unable to resolve {target} . Please check the IP address")
    exit()
print(f"\n Target: {ip}")
print(f"Ports: 1-1024")
print(f"Started: {datetime.datetime.now().strftime('%H:%M:%S')}")
print(" "+"-"*30)
threads= []
for port in range(1,1025):
    t= threading.Thread(target=scan_port, args=(ip, port))
    threads.append(t)
    t.start()
for t in threads:
   t.join()

print(" "+"-"*30)
print(f"\n Scan Complete")
print(f"Open ports found : {len(open_ports)}")
print(f" Finished at: {datetime.datetime.now().strftime('%H:%M:%S')}\n")