import socket
ip="127.0.0.1"
port=135
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result= sock.connect_ex((ip, port))
if result==0:
    print(f"Port {port} is OPEN")
else:
    print(f"Port {port} is CLOSED(error code: {result})")
sock.close()