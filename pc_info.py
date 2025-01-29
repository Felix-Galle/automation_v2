import socket
import threading
import time
import sys
import json
import os
import platform
from settings_loader import Settings
from logger import log_message, log_error  # Import logging functions

settings = Settings()  # Create an instance of the Settings class
port_settings = settings.load_ports(filename="pc_info")  # Load the port settings

# Check if port settings are valid and extract broadcast port
if port_settings and "broadcast_port" in port_settings:
    BROADCAST_PORT = port_settings["broadcast_port"]
else:
    log_error("Error: Broadcast port setting not found.")
    sys.exit(1)  # Exit if broadcast port is not found

broadcasting_ips = set()  # Set to store unique broadcasting IPs

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def get_computer_info():
    ip = get_ip()
    computer_name = platform.node()
    username = getpass.getuser()

    return {"IP": ip, "ComputerName": computer_name, "Username": username}

def receive_broadcast():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', BROADCAST_PORT))  # Bind to all interfaces on the specified port

    log_message(f"{datetime.now()} - Listening for broadcasts on port {BROADCAST_PORT}...")
    
    while True:
        data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
        pc_name, ip = data.decode().split(',')
        
        # Add the broadcasting IP to the set
        if ip not in broadcasting_ips:
            broadcasting_ips.add(ip)
            log_message(f"{datetime.now()} - New broadcasting PC: {pc_name}, {ip}")
            print_broadcasting_ips()

def print_broadcasting_ips():
    broadcasting_list = [{"name": pc_name, "ip": ip} for pc_name, ip in broadcasting_ips]
    
    log_message(f"{datetime.now()} - All IPs found: {', '.join(broadcasting_ips)}")
    
    print(json.dumps(broadcasting_list))
    sys.stdout.flush()  # Ensure the output is flushed

def update_info_every_2_seconds():
    while True:
        computer_info = get_computer_info()  # Get the current computer info
        print(json.dumps([computer_info]))  # Output as JSON for Electron or other scripts
        sys.stdout.flush()  # Ensure the output is flushed
        time.sleep(2)  # Wait for 2 seconds before updating again

if __name__ == "__main__":
    log_message(f"{datetime.now()} - Program started.")
    threading.Thread(target=receive_broadcast, daemon=True).start()
    threading.Thread(target=update_info_every_2_seconds, daemon=True).start()

    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)  # Sleep to keep the main thread alive
    except KeyboardInterrupt:
        # Log the closure of the program
        log_message(f"{datetime.now()} - Program closed.")
        sys.exit(0)
