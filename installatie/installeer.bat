@echo off
title De Geest in de Fles - installatie
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0installeer.ps1" %*
pause
