import os
import winreg

APP_NAME = "OopsWrongLang"
RUN_BAT_PATH = os.path.abspath("run.bat")

def add_to_startup():
    """
    Adds the application to Windows startup.
    """
    try:
        key = winreg.HKEY_CURRENT_USER
        sub_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        print(f'bat file path: {RUN_BAT_PATH}')
        with winreg.OpenKey(key, sub_key, 0, winreg.KEY_SET_VALUE) as registry_key:
            winreg.SetValueEx(registry_key, APP_NAME, 0, winreg.REG_SZ, f'"{RUN_BAT_PATH}"')
    except OSError as e:
        print(f"Error adding to startup: {e}")

def remove_from_startup():
    """
    Removes the application from Windows startup.
    """
    try:
        key = winreg.HKEY_CURRENT_USER
        sub_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        with winreg.OpenKey(key, sub_key, 0, winreg.KEY_SET_VALUE) as registry_key:
            winreg.DeleteValue(registry_key, APP_NAME)
    except FileNotFoundError:
        # This is fine, it means the key doesn't exist
        pass
    except OSError as e:
        print(f"Error removing from startup: {e}")

def is_in_startup():
    """
    Checks if the application is in Windows startup.
    """
    try:
        key = winreg.HKEY_CURRENT_USER
        sub_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        with winreg.OpenKey(key, sub_key, 0, winreg.KEY_READ) as registry_key:
            winreg.QueryValueEx(registry_key, APP_NAME)
        return True
    except FileNotFoundError:
        return False
    except OSError as e:
        print(f"Error checking startup status: {e}")
        return False
