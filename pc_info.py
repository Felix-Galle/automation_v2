import socket
import threading
import time
import sys
import json
import os
import logging
from datetime import datetime

BROADCAST_PORT = 12000
broadcasting_ips = set()  # Set to store unique broadcasting IPs

# Set up logging
log_folder = 'log/pc_info-logs'
os.makedirs(log_folder, exist_ok=True)  # Create the log folder if it doesn't exist
log_file = os.path.join(log_folder, f'pc_info-{datetime.now()}.log')

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(message)s'
)

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def receive_broadcast():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', BROADCAST_PORT))  # Bind to all interfaces on the specified port

    logging.info(f"{datetime.now()} - Listening for broadcasts on port {BROADCAST_PORT}...")
    
    while True:
        data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
        pc_name, ip = data.decode().split(',')
        
        # Add the broadcasting IP to the set
        if ip not in broadcasting_ips:
            broadcasting_ips.add(ip)
            logging.info(f"{datetime.now()} - New broadcasting PC: {pc_name}, {ip}")
            print_broadcasting_ips()

def print_broadcasting_ips():
    # Create a list of broadcasting PCs
    broadcasting_list = [{"name": pc_name, "ip": ip} for pc_name, ip in broadcasting_ips]
    
    # Log the current broadcasting IPs
    logging.info(f"{datetime.now()} - All IPs found: {', '.join(broadcasting_ips)}")
    
    # Send the list to the Electron app as JSON
    print(json.dumps(broadcasting_list))
    sys.stdout.flush()  # Ensure the output is flushed

if __name__ == "__main__":
    # Log the start of the program
    logging.info(f"{datetime.now()} - Program started.")
    
    # Start the receiver in a separate thread
    threading.Thread(target=receive_broadcast, daemon=True).start()
    
    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)  # Sleep to keep the main thread alive
    except KeyboardInterrupt:
        # Log the closure of the program
        logging.info(f"{datetime.now()} - Program closed.")
        sys.exit(0)