import sys
import os
from datetime import datetime

LOG_DIR = 'log/pc_info-logs'
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def log_message(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_file_path = os.path.join(LOG_DIR, f"general_log.txt")
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"{timestamp} - {message}\n")

def log_error(error_message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_file_path = os.path.join(LOG_DIR, f"error_log.txt")
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"{timestamp} - {error_message}\n")

if __name__ == "__main__":
    message = sys.argv[1]
    log_message(message)
