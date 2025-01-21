import socket
import argparse
import os

def send_file(file_path, destination_ip, destination_port=12200, source_port=12210):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the source port (12210)
    sock.bind(('', source_port))

    # Open the file and read it in chunks
    try:
        with open(file_path, 'rb') as file:
            # Read file in chunks of 1024 bytes
            chunk = file.read(1024)
            while chunk:
                # Send each chunk to the destination IP and port
                sock.sendto(chunk, (destination_ip, destination_port))
                chunk = file.read(1024)
                
                print(f"Sent a chunk of size {len(chunk)} bytes.")

    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
    finally:
        sock.close()
        print("File transmission complete.")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Send a file over UDP.")
    parser.add_argument("file_path", help="Path to the file to send.")
    parser.add_argument("destination_ip", help="IP address of the destination computer.")
    
    # Parse the arguments
    args = parser.parse_args()

    # Send the file
    send_file(args.file_path, args.destination_ip)
