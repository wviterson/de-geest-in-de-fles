@echo off
title De Geest in de Fles - docent-server
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0beheer\geest.ps1" -Actie Server
pause
