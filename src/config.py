import os
import keyboard

CONFIG_FILE = "shortcut.txt"

def get_shortcut():
    """
    Retrieves the shortcut from the config file.
    If the file doesn't exist, it prompts the user to create one by pressing the desired keys.
    """
    if not os.path.exists(CONFIG_FILE):
        print("It seems this is the first time you are running the application.")
        while True:
            print("Please press the key combination you want to use as a shortcut and then press ESC.")
            shortcut = keyboard.read_hotkey(suppress=False)
            print(f"You pressed: {shortcut}")
            confirm = input("Is this correct? (y/n): ").lower()
            if confirm == 'y':
                with open(CONFIG_FILE, "w") as f:
                    f.write(shortcut)
                return shortcut
            else:
                print("Let's try again.")
    else:
        with open(CONFIG_FILE, "r") as f:
            return f.read().strip()
