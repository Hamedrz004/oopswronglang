@echo off
REM run.bat
REM Activates the virtual environment and runs your main Python script.

REM Activate the virtual environment
call venv\Scripts\activate.bat

REM Run your main Python script (replace main.py with your script name if different)
start "OopsWrongLang" /B python src\main.pyw
echo application is running in the background. you can close this window.
pause