import socket
import subprocess
import re 
def get_local_ip():
     s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     try:
        s.connect(("8.8.8.8", 80))
        ip= s.getsockname()[0]
     except Exception:
        ip= "127.0.0.1"
     finally:
        s.close()
     return ip
print("Local IP-", get_local_ip())

def get_gateway():
   result= subprocess.run(["ipconfig"], capture_output= True, text=True)
   output= result.stdout
   match= re.search(r"Default Gateway[. ]*:[^\n]*\n?\s*([\d.]+)",output)
   if match:
      return match.group(1)
   return "Not found"
print("Gateway-", get_gateway())

def get_dns():
   result = subprocess.run(["ipconfig","/all"], capture_output= True, text= True)
   output= result.stdout
   match= re.search(r"DNS Servers[. ]*:[^\n]*\n?\s*([\d.]+)", output)
   if match:
      return match.group(1)
   return "Not Found"
print("DNS-", get_dns())