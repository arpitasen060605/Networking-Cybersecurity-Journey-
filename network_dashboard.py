import socket
import subprocess
import re 
import psutil 

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

def get_gateway():
   result= subprocess.run(["ipconfig"], capture_output= True, text=True)
   output= result.stdout
   match= re.search(r"Default Gateway[. ]*:[^\n]*\n?\s*([\d.]+)",output)
   return match.group(1) if match else "Not Found"
      
def get_dns():
   result = subprocess.run(["ipconfig","/all"], capture_output= True, text= True)
   output= result.stdout
   match= re.search(r"DNS Servers[. ]*:[^\n]*\n?\s*([\d.]+)", output)
   return match.group(1) if match else "Not Found"

def get_cpu_usage():
   return psutil.cpu_percent(interval=1)

def get_ram_usage():
   memory= psutil.virtual_memory()
   return memory.percent 

print("\n Network Information")
print(" "+ "-"*30)
print(f"Local IP- {get_local_ip()}")
print(f"Gateway- {get_gateway()}")
print(f"DNS- {get_dns()}")
print(f"\nCPU Usage- {get_cpu_usage()}%")
print(f"RAM Usage- {get_ram_usage()}%")
print(" "+ "-"*30 + "\n")
