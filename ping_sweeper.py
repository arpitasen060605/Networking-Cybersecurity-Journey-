import subprocess 
import threading 
import datetime

alive_hosts= []
lock= threading.Lock()
def ping_ip(ip):
    result= subprocess.run(["ping","-n","1","-w","300",ip],capture_output= True, text=True)
    if result.returncode==0:
        with lock:
            alive_hosts.append(ip)
            print(f"{ip} is Active")
print("\n NETWORK PING SWEEPER")
print(" "+"-"*28)
network=input("Enter network prefix(e.g. 192.168.29.):").strip()
if not network.endswith("."):
    network+= "."
print(f"\n Sweeping: {network}0/24")
print(f"Started: {datetime.datetime.now().strftime('%H:%M:%S')}")
print(" "+"-"*28)
threads=[]
for i in range(1,255):
    ip= network + str(i)
    t= threading.Thread(target=ping_ip, args=(ip,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
alive_hosts.sort()
print(" "+"-"*30)
print(f"\nSweep/Scan Complete")
print(f"Hosts found: {len(alive_hosts)}")
print(f"Finished at: {datetime.datetime.now().strftime('%H:%M:%S')}\n")
filename= f"sweep_{network.replace('.','_')}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
with open(filename, "w") as f:
    f.write(f"Ping Sweep Report\n")
    f.write(f"{'='*30}\n")
    f.write(f"Network: {network}0/24\n")
    f.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"{'='*30}\n\n")
    if alive_hosts:
        for ip in alive_hosts:
            f.write(f"Active {ip}\n")
    else:
        f.write("No active hosts found.\n")
    f.write(f"\nTotal active hosts:{len(alive_hosts)}\n")
print(f"Report saved, {filename}\n")