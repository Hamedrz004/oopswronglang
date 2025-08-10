import os
import json
import keyboard
import time
import msvcrt

CONFIG_FILE = "config.json"
SHORTCUT_FILE = "shortcut.txt" # For migrating old config

def load_config():
    """
    Loads the configuration from config.json.
    If the file doesn't exist, it creates it with default values.
    It also migrates the old shortcut.txt if it exists.
    """
    if not os.path.exists(CONFIG_FILE):
        config = {"run_on_startup": False, "shortcut": "ctrl+space"}
        if os.path.exists(SHORTCUT_FILE):
            with open(SHORTCUT_FILE, "r") as f:
                shortcut = f.read().strip()
                if shortcut:
                    config["shortcut"] = shortcut
            os.remove(SHORTCUT_FILE) # remove old config file
        save_config(config)
        return config
    else:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)

def save_config(config):
    """
    Saves the configuration to config.json.
    """
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

def get_shortcut():
    """
    Retrieves the shortcut from the config file.
    If the file doesn't exist, it prompts the user to create one by pressing the desired keys.
    """
    config = load_config()
    if "shortcut" not in config:
        print("It seems this is the first time you are running the application.")
        while True:
            print("Please press the key combination you want to use as a shortcut and then press ESC.")
            shortcut = keyboard.read_hotkey(suppress=False)
            print(f"You pressed: {shortcut}")
            confirm = input("Is this correct? (y/n): ").lower()
            if confirm == 'y':
                config["shortcut"] = shortcut
                save_config(config)
                return shortcut
            else:
                print("Let's try again.")
    return config["shortcut"]

if __name__ == "__main__":
    config = load_config()
    print(f"Your shortcut is set to: {config.get('shortcut', 'Not set')}")
    print(f"Run on startup is set to: {config.get('run_on_startup', 'Not set')}")

    print('Do you want to change the shortcut? (y/n): ', end='')
    if input().lower() == 'y':
        while True:
            time.sleep(0.2)
            print("Please press the key combination you want to use as a shortcut and then press ESC.")
            new_shortcut = keyboard.read_hotkey(suppress=False)
            print(f"You pressed: {new_shortcut}")
            time.sleep(0.01)
            # Clear the input buffer
            while msvcrt.kbhit():
                msvcrt.getch()

            confirm = input("Is this correct? (y/n): ").lower()
            if confirm.lower() == 'y':
                config['shortcut'] = new_shortcut
                save_config(config)
                print("Shortcut updated successfully.")
                break
            else:
                print("Let's try again.")
    else:
        print("No changes made to the shortcut.")
        print("Exiting without changes.")
    input("Press Enter to exit.")
