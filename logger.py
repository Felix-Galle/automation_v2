import sys
import os
from datetime import datetime

PC_LOG_DIR = 'log/pc_info-logs'
ERROR_LOG_DIR = 'log/errors-logs'
GENERAL_LOG_DIR = 'log/general-logs'

if not os.path.exists(PC_LOG_DIR):
    os.makedirs(PC_LOG_DIR)
if not os.path.exists(ERROR_LOG_DIR):
    os.makedirs(ERROR_LOG_DIR)
if not os.path.exists(GENERAL_LOG_DIR):
    os.makedirs(GENERAL_LOG_DIR)

def general_log(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_file_path = os.path.join(PC_LOG_DIR, f"general_log-{datetime.now()}.txt")
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"{timestamp} - {message}\n")

def error_log(error_message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_file_path = os.path.join(ERROR_LOG_DIR, f"error_log-{datetime.now()}.txt")
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"{timestamp} - {error_message}\n")



