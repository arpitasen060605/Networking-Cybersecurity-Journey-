import threading
import time
import random 
def check_port(port):
    time.sleep(random.uniform(0.1, 1.0))
    print(f"Port {port} is checked")
print("\t\t Without Threading\t\t")
start= time.time()
for port in[1,2,3,4,5]:
    check_port(port)
print(f"Time taken: {time.time()- start:.1f} seconds\n")
print("\t\t With threading\t\t")
start= time.time()
threads=[]
for port in [1,2,3,4,5]:
    t= threading.Thread(target=check_port, args=(port,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print(f"Time taken: {time.time()-start:.1f} seconds")
