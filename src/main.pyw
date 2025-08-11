# oopswronglang/main.py
# This script listens for a keyboard shortcut (Ctrl + Space) and converts the text
# from English characters to Persian characters using the `persian` library.
import keyboard
import pyperclip
import time
import threading
import pystray
from PIL import Image
import re
from config import load_config, save_config, get_shortcut
from startup import add_to_startup, remove_from_startup, is_in_startup

def convert_en_characters(input_str):
    """
        Assumes that characters written with standard persian keyboard
        not windows arabic layout
    :param input_str: String contains English chars
    :return: New string with related characters on Persian standard keyboard
    """
    mapping = {
        'q': 'ض',
        'w': 'ص',
        'e': 'ث',
        'r': 'ق',
        't': 'ف',
        'y': 'غ',
        'u': 'ع',
        'i': 'ه',
        'o': 'خ',
        'p': 'ح',
        '[': 'ج',
        ']': 'چ',
        'a': 'ش',
        's': 'س',
        'd': 'ی',
        'f': 'ب',
        'g': 'ل',
        'h': 'ا',
        'j': 'ت',
        'k': 'ن',
        'l': 'م',
        ';': 'ک',
        "'": 'گ',
        'z': 'ظ',
        'x': 'ط',
        'c': 'ز',
        'v': 'ر',
        'b': 'ذ',
        'n': 'د',
        'm': 'ئ',
        ',': 'و',
        '?': '؟',
        '\\':'پ',
        'ض': 'q',
        'ص': 'w',
        'ث': 'e',
        'ق': 'r',
        'ف': 't',
        'غ': 'y',
        'ع': 'u',
        'ه': 'i',
        'خ': 'o',
        'ح': 'p',
        'ج': '[',
        'چ': ']',
        'ش': 'a',
        'س': 's',
        'ی': 'd',
        'ب': 'f',
        'ل': 'g',
        'ا': 'h',
        'ت': 'j',
        'ن': 'k',
        'م': 'l',
        'ک': ';',
        'گ': "'",
        'ظ': 'z',
        'ط': 'x',
        'ز': 'c',
        'ر': 'v',
        'ذ': 'b',
        'د': 'n',
        'ئ': 'm',
        'و': ',',
        '؟': '?',
        'پ': '\\',
        'H':'آ',
        'آ': 'H',
        'C':'ژ',
        'ژ': 'C',
        'T':'،',
        '،': 'T',
        '؛':'Y',
        'Y':'؛',
    }
    return _multiple_replace(mapping, input_str)
def _multiple_replace(mapping, text):
    """
    Internal function for replace all mapping keys for a input string
    :param mapping: replacing mapping keys
    :param text: user input string
    :return: New string with converted mapping keys to values
    """
    pattern = "|".join(map(re.escape, mapping.keys()))
    return re.sub(pattern, lambda m: mapping[m.group()], str(text))

# Function to handle the keyboard shortcut
def on_shortcut():
    """This function is called when the shortcut is pressed."""
    orginal_text = pyperclip.paste()  # Get the current clipboard content
    time.sleep(0.1)
    keyboard.press_and_release('ctrl+c') # Simulate pressing Ctrl+C to copy selected text
    time.sleep(0.1)
    text = pyperclip.paste()
    # If no text is selected, do nothing
    if not text or text== orginal_text:
        print("No text was selected.")
        return
    converted_text = convert_en_characters(text)
    pyperclip.copy(converted_text)
    print(f"Converted text: {converted_text}")
    keyboard.press_and_release('ctrl+v')  # Paste the converted text
    time.sleep(0.2)
    if load_config().get("lang_change", True):
        # Change the keyboard layout to Persian
        keyboard.press_and_release('windows+space')
def quit_app(icon, item):
    icon.stop()
    import os
    os._exit(0)

def setup_tray(config):
    def on_toggle_lang_change(icon, item):
        config["lang_change"] = not item.checked
        save_config(config)

    def on_toggle_startup(icon, item):
        config["run_on_startup"] = not item.checked
        save_config(config)
        if config["run_on_startup"]:
            add_to_startup()
        else:
            remove_from_startup()

    image = Image.open("assets/icon.png")
    menu = pystray.Menu(
        pystray.MenuItem(f'Current Shortcut: {get_shortcut()}',lambda icon, item: None),
        pystray.MenuItem(
            'change keyboard language layout after transformation',
            on_toggle_lang_change,
            checked=lambda item: config["lang_change"]
        ),
        pystray.MenuItem(
            'Run on Startup',
            on_toggle_startup,
            checked=lambda item: config["run_on_startup"]
        ),
        pystray.MenuItem('Quit', quit_app)
    )
    icon = pystray.Icon("oopswronglang", image, "OopsWrongLang", menu)
    icon.run()

def main():
    config = load_config()
    # Sync startup state just in case it was changed externally
    config["run_on_startup"] = is_in_startup()
    save_config(config)

    # Start the tray icon in a separate thread
    tray_thread = threading.Thread(target=lambda: setup_tray(config), daemon=True)
    tray_thread.start()

    # Register the keyboard shortcut
    shortcut = get_shortcut()
    keyboard.add_hotkey(shortcut, on_shortcut)
    print(f"Press {shortcut} to convert text to Persian.")

    # Keep the script running
    keyboard.wait(suppress=True)

if __name__ == "__main__":
    main()
