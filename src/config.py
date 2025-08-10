import os
import keyboard
import time
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

if __name__ == "__main__":
    shortcut = get_shortcut()
    print(f"Your shortcut is set to: {shortcut}")
    print("You can now use this shortcut in the application.")
    print('do you want to change the shortcut? (y/n): ', end='')
    if input().lower() == 'y':
        while True:
            time.sleep(0.2)
            print("Please press the key combination you want to use as a shortcut and then press ESC.")
            new_shortcut = keyboard.read_hotkey(suppress=False)
            print(f"You pressed: {new_shortcut}")
            time.sleep(0.5)
            confirm = input("Is this correct? (y/n): ").lower()
            if confirm.lower() == 'y':
                with open(CONFIG_FILE, "w") as f:
                    f.write(new_shortcut)
                print("Shortcut updated successfully.")
                break
            else:
                print("Let's try again.")

    else:
        print("No changes made to the shortcut.")
        print("Exiting without changes.")
        input("Press Enter to exit.")