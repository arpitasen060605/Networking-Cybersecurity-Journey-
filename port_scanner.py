import socket
ip="127.0.0.1"
print(f"Scanning {ip} .......")
print("-"*30)
for port in range(1,1025):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
     sock.settimeout(0.05)
     result= sock.connect_ex((ip, port))
     if result==0:
        print(f"Port {port} is OPEN")
print("-"*30)
print("Scan Complete")