import subprocess 
import threading 
network= "192.168.29."
alive_hosts= []
lock= threading.Lock()
def ping_ip(ip):
    result= subprocess.run(["ping","-n","1","-w","300",ip],capture_output= True, text=True)
    if result.returncode==0:
        with lock:
            alive_hosts.append(ip)
            print(f"{ip} is Active")
print(f"Sweeping the network {network}0/24....")
print("-"*30)
threads=[]
for i in range(1,255):
    ip= network + str(i)
    t= threading.Thread(target=ping_ip, args=(ip,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("-"*30)
print(f"Sweep/Scan Complete {len(alive_hosts)} hosts are active")
