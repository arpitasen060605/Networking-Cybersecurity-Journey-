import subprocess 
network= "192.168.29."
print(f"Sweeping(Scanning) {network}0/24...")
print("-"*30)

alive_hosts= []

for i in range(1,255):   
     ip= network + str(i)
     result= subprocess.run(["ping", "-n","1", "-w", "300", ip], capture_output= True, text= True) 

     if result.returncode==0:
        print(f"{ip} is Active")
        alive_hosts.append(ip)

print("-"*30)
print(f"Sweep(Scan)Complete, {len(alive_hosts)} hosts are active.")

