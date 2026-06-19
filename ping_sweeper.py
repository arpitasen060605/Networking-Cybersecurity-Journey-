import subprocess 
ip= "127.0.0.1"
result= subprocess.run(["ping", "-n","1", ip], capture_output= True, text= True)
if result.returncode==0:
    print(f"{ip} is Active")
else:
    print(f"{ip} is Dead")