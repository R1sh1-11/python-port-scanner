#Multi-threader scanner
import socket
import threading
from queue import Queue
from datetime import datetime

# Define the target (Please stick to a safe one)
target = "scanme.nmap.org"
target_ip = socket.gethostbyname(target)

print(f"Scanning Target: {target_ip}")
print(f"Time started: {datetime.now()}")
print("-" * 50)

# Holds all the port numbers we need to scan
queue = Queue()

# Port Scan Function:
def port_scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()
    except:
        pass

# Worker function
def worker():
    while True:
        port = queue.get()
        port_scan(port)
        queue.task_done()

# Creating threads
for _ in range(100):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

# Fill the Queue
for port in range(1, 1025):
    queue.put(port)

queue.join()

print("-" * 50)
print("Scan completed.")