@echo off
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0beheer\geest.ps1" -Actie Status
pause
