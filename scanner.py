import socket
import threading
from datetime import datetime

target = input("Enter Target IP or Domain: ")
target_ip = socket.gethostbyname(target)

print("-" * 50)
print(f"Scanning Target: {target_ip}")
print(f"Scan started at: {datetime.now()}")
print("-" * 50)

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            try:
                s.send(b"HEAD / HTTP/1.0\r\n\r\n")
                banner = s.recv(1024).decode().strip().split('\n')[0]
            except:
                banner = "Unknown Service"
            print(f"[+] Port {port:<5} OPEN  | Service/Banner: {banner}")
        s.close()
    except Exception:
        pass

threads = []
for port in range(1, 1025):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("-" * 50)
print("Scan Completed!")
