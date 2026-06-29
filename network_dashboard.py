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

def get_open_ports(ip, port_range=(1,1024)):
  open_ports=[]
  lock= threading.Lock()
  def scan_port(port):
     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.05)
        result= sock.connect_ex((ip, port))
        if result==0:
           with lock:
              open_ports.append(port)
  threads=[]
  for port in range(port_range[0], port_range[1]+1):
     t= threading.Thread(target=scan_port, args=(port,))
     threads.append(t)
     t.start()
  for t in threads:
      t.join()
  open_ports.sort()
  return open_ports 

def get_latency_and_loss(target="8.8.8.8", count=4):
   latencies= []
   sent= count
   received= 0
   for _ in range(count):
      result= subprocess.run(["ping","-n","1","-w","1000",target],capture_output=True,text=True)
      if result.returncode==0:
         received+=1
         match= re.search(r"time[=<](\d+)ms", result.stdout)
         if match:
            latencies.append(int(match.group(1)))
   packet_loss= ((sent- received)/sent)*100
   if latencies:
      avg_latency=sum(latencies)/ len(latencies)
   else:
      avg_latency= None
   return avg_latency, packet_loss

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
for index, d in enumerate(devices, start=1):
   print(f"   {index}.{d}")
print(" "+"-"*30)

choice= input("\n Enter the number of the device to scan for open ports:")
try:
   selected_index= int(choice)-1
   target_ip= devices[selected_index]
except(ValueError, IndexError):
   print("Invalid choice.Skipping port scan")
   target_ip= None
if target_ip:
   print(f"\n Scanning open ports on {target_ip}....")
   ports= get_open_ports(target_ip)
   print(f"Found {len(ports)} open port(s):")
   for p in ports:
      print(f"   - {p}")
print("\n Checking Internet Latency.....")
avg_latency, packet_loss = get_latency_and_loss()
if avg_latency is not None:
   print(f"Average Latency- {avg_latency:.1f} ms")
else:
   print(f"Average Latency- N/A (all pings failed)")
print(f"Packet Loss- {packet_loss:.0f}%")
print(" "+ "-"* 30 + "\n")