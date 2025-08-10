# OopsWrongLang

A simple utility to fix text that you accidentally typed in the wrong keyboard layout (English to Persian and vice-versa).

## Features

- Converts selected text between English and Persian keyboard layouts.
- Runs in the background with a system tray icon.
- Easy to use with a simple keyboard shortcut.

## How it Works

The application runs in the background and monitors for a specific keyboard shortcut. When you press the shortcut, it does the following:

1.  Copies the currently selected text to the clipboard.
2.  Converts the text to the other keyboard layout (e.g., English to Persian).
3.  Pastes the converted text, replacing your selection.

## Prerequisites

-only tested on Windows.
- You must have Python installed on your system. You can download it from [python.org](https://www.python.org/).

## Installation

1.  Clone this repository or download the source code.
2.  **For Windows users:**
    Run the `install.bat` script to create a virtual environment and install the required dependencies.
    ```batch
    install.bat
    ```

## Usage

**For Windows users:**

1.  Run the `run.bat` script to start the application.
    ```batch
    run.bat
    ```

2.  The application will start running in the background, and you will see its icon in the system tray.
3.  Select any text you want to convert.
4.  Press `Ctrl+Space`. (or any other shorcut in the shortcut.txt file. see [configuration](https://github.com/Hamedrz004/oopswronglang/tree/add-readme?tab=readme-ov-file#configuration) for details.)
5.  The selected text will be instantly converted.

To quit the application, right-click the tray icon and select "Quit".

## Configuration

**For Windows users:**
use the `configure&run.bat` for ease of use.
it automatically updates `shortcut.txt` file and runs the app.
you can edit the `shortcut.txt` yourself too but be cautious.

**For macOS/Linux users:**
after activating the virtual environment, you can run:
```bash
python src/config.py
```
it automatically updates `shortcut.txt` file and runs the app.
you can edit the `shortcut.txt` yourself too but be cautious.

## Dependencies

This project uses the following Python libraries:

- `keyboard`
- `pyperclip`
- `pystray`
- `Pillow`

These dependencies are listed in `requirements.txt` and will be installed automatically when you run `install.bat`.
