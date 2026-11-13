@echo off
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0controleer.ps1" %*
pause
