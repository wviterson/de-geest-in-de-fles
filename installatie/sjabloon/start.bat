@echo off
title De Geest in de Fles
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0beheer\geest.ps1" -Actie Start
if errorlevel 1 pause
