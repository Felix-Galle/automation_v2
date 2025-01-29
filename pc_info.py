import socket
import threading
import time
import sys
import json
import os
import platform
import getpass
from datetime import datetime
from settings_loader import Settings
from logger import general_log, error_log  # Import logging functions

settings = Settings()  # Create an instance of the Settings class
port_settings = settings.load_ports(filename="pc_info")  # Load the port settings

# Check if port settings are valid and extract broadcast port
if port_settings and "broadcast_port" in port_settings:
    BROADCAST_PORT = port_settings["broadcast_port"]
else:
    error_log("Error: Broadcast port setting not found.")
    sys.exit(1)  # Exit if broadcast port is not found

broadcasting_ips = []  # List to store unique broadcasting IPs

def get_ip():
    """Get the local IP address of this machine."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))  # Connect to Google's DNS to get the local IP
    ip = s.getsockname()[0]  # Get the local IP address
    s.close()
    return ip

def get_computer_info():
    """Get computer information like IP, computer name, and username."""
    ip = get_ip()
    computer_name = platform.node()  # Get the machine's hostname
    username = getpass.getuser()  # Get the username of the logged-in user

    return {"IP": ip, "ComputerName": computer_name, "Username": username}

def receive_broadcast():
    """Listen for incoming broadcasts from other computers."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', BROADCAST_PORT))  # Bind to all interfaces on the specified port

    general_log(f"{datetime.now()} - Listening for broadcasts on port {BROADCAST_PORT}...")

    while True:
        data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
        pc_name, ip = data.decode().split(',')  # Extract the pc_name and IP from the received data

        # Add the broadcasting IP to the list if it's not already there
        if ip not in [entry[1] for entry in broadcasting_ips]:  # Check by IP to avoid duplicates
            broadcasting_ips.append((pc_name, ip))  # Add as tuple (pc_name, ip)
            general_log(f"{datetime.now()} - New broadcasting PC: {pc_name}, {ip}")

def get_broadcasting_ips():
    """Return the list of broadcasting IPs (name, IP) as tuples."""
    return broadcasting_ips

def update_info_every_2_seconds():
    """Continuously update and print the computer info every 2 seconds."""
    while True:
        computer_info = get_computer_info()  # Get the current computer info
        print(json.dumps([computer_info]))  # Output as JSON for Electron or other scripts
        sys.stdout.flush()  # Ensure the output is flushed
        time.sleep(2)  # Wait for 2 seconds before updating again

if __name__ == "__main__":
    general_log(f"{datetime.now()} - Program started.")
    
    # Start threads for receiving broadcasts and updating computer info
    threading.Thread(target=receive_broadcast, daemon=True).start()
    threading.Thread(target=update_info_every_2_seconds, daemon=True).start()

    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)  # Sleep to keep the main thread alive
    except KeyboardInterrupt:
        # Log the closure of the program
        general_log(f"{datetime.now()} - Program closed.")
        sys.exit(0)
