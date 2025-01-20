import socket
import os

# Function to send a file over UDP
def send_file(file_path, receiver_ip, receiver_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Read the file and send it in chunks
    with open(file_path, 'rb') as f:
        while True:
            bytes_read = f.read(1024)  # Read in 1KB chunks
            if not bytes_read:
                break  # File transmission is complete
            sock.sendto(bytes_read, (receiver_ip, receiver_port))
    
    sock.close()
    print(f"File {os.path.basename(file_path)} sent to {receiver_ip}:{receiver_port}")

# Example usage
# send_file('path/to/your/file.txt', 'receiver_ip_address', 12200)

# You can call the send_file function with the actual file path and receiver details