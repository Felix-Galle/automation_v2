# pc_info.py
import socket
import threading
import time
import sys
import json

BROADCAST_PORT = 12000

broadcasting_ips = set()  # Set to store unique broadcasting IPs

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def receive_broadcast():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', BROADCAST_PORT))  # Bind to all interfaces on the specified port

    print(f"Listening for broadcasts on port {BROADCAST_PORT}...")
    
    while True:
        data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
        pc_name, ip = data.decode().split(',')
        
        # Add the broadcasting IP to the set
        if ip not in broadcasting_ips:
            broadcasting_ips.add(ip)
            print(f"New broadcasting PC: {pc_name}, {ip}")
            print_broadcasting_ips()

def print_broadcasting_ips():
    # Create a list of broadcasting PCs
    broadcasting_list = [{"name": pc_name, "ip": ip} for pc_name, ip in broadcasting_ips]
    
    # Send the list to the Electron app as JSON
    print(json.dumps(broadcasting_list))
    sys.stdout.flush()  # Ensure the output is flushed

if __name__ == "__main__":
    # Start the receiver in a separate thread
    threading.Thread(target=receive_broadcast, daemon=True).start()
    
    # Keep the main thread alive
    while True:
        time.sleep(1)  # Sleep to keep the main thread alive