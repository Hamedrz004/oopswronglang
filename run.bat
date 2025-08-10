@echo off
cd /d "%~dp0"

call venv\Scripts\activate.bat
echo Starting the application...

start "OopsWrongLang" /B pythonw src\main.pyw

pause