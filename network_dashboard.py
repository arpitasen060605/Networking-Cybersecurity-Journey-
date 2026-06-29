import socket
import subprocess
import re 
import psutil 
import threading 

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

def get_connected_devices(network_prefix):
   alive_hosts=[]
   lock= threading.Lock()
   def ping_ip(ip):
      result= subprocess.run(["ping","-n","1","-w","300",ip], capture_output=True, text=True)
      if result.returncode==0:
         with lock:
            alive_hosts.append(ip)
   threads= []
   for i in range(1,255):
       ip= network_prefix + str(i)
       t= threading.Thread(target=ping_ip, args=(ip,))
       threads.append(t)
       t.start()
   for t in threads:
       t.join()
   alive_hosts.sort()
   return alive_hosts

def get_network_prefix(local_ip):
   parts= local_ip.split(".")
   prefix= ".".join(parts[:3]) + "."
   return prefix

local_ip= get_local_ip()
network_prefix = get_network_prefix(local_ip)

print("\n Network Information")
print(" "+ "-"*30)
print(f"Local IP- {get_local_ip()}")
print(f"Gateway- {get_gateway()}")
print(f"DNS- {get_dns()}")
print(f"\nCPU Usage- {get_cpu_usage()}%")
print(f"RAM Usage- {get_ram_usage()}%")
print(" "+ "-"*30 + "\n")
print("\nScanning for connected devices....")
devices= get_connected_devices(network_prefix)
print(f"Found {len(devices)} device(s):")
for d in devices:
   print(f"   -{d}")
print(" "+"-"*30+ "\n")