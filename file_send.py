import socket
import os
import sys

def send_file(file_path, destination_ip, destination_port=12345):
    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist.")
        return

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((destination_ip, destination_port))
        with open(file_path, 'rb') as f:
            s.sendall(f.read())
        print(f"File {file_path} sent to {destination_ip}")

# Example usage
# send_file("path/to/your/file.txt", "192.168.1.2")