import socket
ip="127.0.0.1"
print(f"Scanning {ip} .......")
print("-"*30)
for port in range(1,1025):
    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result= sock.connect_ex((ip, port))
    if result==0:
        print(f"Port {port} is OPEN")
    sock.close()
print("-"*30)
print("Scan Complete")