import json
import os

def load_settings(filename):
    settings_file = 'settings/settings.json'
    
    # Check if the settings file exists
    if not os.path.exists(settings_file):
        print(f"Error: The settings filepath '{settings_file}' does not exist.")
        return None
    
    try:
        # Read the settings file
        with open(settings_file, 'r') as f:
            settings = json.load(f)
        
        # Check if the settings for the given filename exist
        if filename in settings:
            return settings[filename]
        else:
            print(f"Error: No settings found for '{filename}'")
            return None
    except Exception as e:
        print(f"Error reading the settings file: {e}")
        return None

# Example usage
'''
    filename = "pc_info"  # This would be passed as an argument
    settings = load_settings(filename)
'''
