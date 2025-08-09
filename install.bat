@echo off
REM install.bat
REM This script sets up a Python virtual environment and installs required libraries.
REM Make sure to run this script in the project directory.

REM Create Python virtual environment
python -m venv venv

REM Activate the virtual environment
call venv\Scripts\activate.bat

REM Upgrade pip
pip install --upgrade pip

REM Install required libraries from requirements.txt
pip install -r requirements.txt --no-cache-dir

echo Environment setup complete.
pause