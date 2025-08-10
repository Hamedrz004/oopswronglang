@echo off
cd /d "%~dp0"

REM Activate the virtual environment
call venv\Scripts\activate.bat

REM run the config script
python src\config.py
REM Check if the activation was successful
if errorlevel 1 (
    echo Failed to activate the virtual environment.
    pause
    exit /b 1
)

REM Run your main Python script (replace main.py with your script name if different)
start "OopsWrongLang" /B pythonw src\main.pyw
echo application is running in the background. you can close this window.
pause