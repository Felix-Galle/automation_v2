import json
import os

class Settings:

    PORT_SETTINGS_FILE = 'settings/port_settings.json' 
    WIN_DIM_FILE = 'settings/win_dim_settings.json'

    def load_ports(self, filename):
        if not os.path.exists(Settings.PORT_SETTINGS_FILE):
            print(f"Error: The settings filepath '{Settings.PORT_SETTINGS_FILE}' does not exist.")
            return None
        
        try:
            with open(Settings.PORT_SETTINGS_FILE, 'r') as f:
                settings = json.load(f)
            
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

    def load_win_dim(self, filename):
        if not os.path.exists(Settings.WIN_DIM_FILE):
            print(f"Error: The settings filepath '{Settings.WIN_DIM_FILE}' does not exist.")
            return None
        
        try:
            with open(Settings.WIN_DIM_FILE, 'r') as f:
                win_dim = json.load(f)
                
            print(f"Loaded window dimensions: {win_dim}")  # Log the loaded dimensions
            
            if 'window_position' in win_dim:
                print(f"Returning window position: {win_dim['window_position']}")  # Log the return value
                return win_dim['window_position']
            else:
                print(f"Error: No settings found for '{filename}'")
                return None
        except Exception as e:
            print(f"Error reading the settings file: {e}")
            return None
