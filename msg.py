# pc_info.py
import os
import socket
import threading

# Constants
BROADCAST_PORT = 12110
RECEIVE_PORT = 12100
BUFFER_SIZE = 1024

# Function to receive messages
def receive_messages():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', RECEIVE_PORT))  # Bind to all interfaces on the specified port
    print(f"Listening for messages on port {RECEIVE_PORT}...")

    while True:
        data, addr = sock.recvfrom(BUFFER_SIZE)  # Buffer size is 1024 bytes
        print(f"Received message from {addr}: {data.decode()}")
        if data.decode() == "exit":
            break

    sock.close()
    os._exit(0)

# Function to send messages
def send_message():
    choice = input("Do you want to broadcast the message? (yes/no): ").strip().lower()
    if choice == 'yes':
        host = '255.255.255.255'  # Broadcast address
    else:
        host = input("Enter the target IP address: ").strip()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        data = input("Enter message to send or type 'exit': ")
        sock.sendto(data.encode(), (host, BROADCAST_PORT))
        if data == "exit":
            break

    sock.close()
    os._exit(0)

if __name__ == "__main__":
    # Start the receiver in a separate thread
    threading.Thread(target=receive_messages, daemon=True).start()
    
    # Start sending messages
    send_message()