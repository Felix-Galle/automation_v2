import json
import os


def load_settings(file_path):
    if not os.path.exists(file_path):
        print(f"Error: The settings file '{file_path}' does not exist.")
        return None
    
    try:
        with open(file_path, 'r') as f:
            settings = json.load(f)
            return settings
    except Exception as e:
        print(f"Error reading the settings file: {e}")
        return None