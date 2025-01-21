import json
import os

class Settings:

    PORT_SETTINGS_FILE = 'settings/port_settings.json' 

    def load_ports(self, filename):
        
        # Access the class variable using self (instance) or Settings (class)
        if not os.path.exists(Settings.PORT_SETTINGS_FILE):
            print(f"Error: The settings filepath '{Settings.PORT_SETTINGS_FILE}' does not exist.")
            return None
        
        try:
            # Read the settings file
            with open(Settings.PORT_SETTINGS_FILE, 'r') as f:
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
        
        
    def load_broadcast_ports(self, filename):

        if not os.path.exists(Settings.PORT_SETTINGS_FILE):
            print(f"Error: The settings filepath '{Settings.PORT_SETTINGS_FILE}' does not exist.")
            return None

        try:
            with open(Settings.PORT_SETTINGS_FILE, 'r') as f:
                settings = json.load(f)
            
            if filename in settings:
                broadcast_port = settings[filename].get("broadcast_port")
                if broadcast_port is not None:
                    return broadcast_port
            else:
                print(f"Error: No settings found for '{filename}'")
                return None
        except Exception as e:
            print(f"Error reading the settings file: {e}")
            return None
