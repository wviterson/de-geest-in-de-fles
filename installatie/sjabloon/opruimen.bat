@echo off
rem Draait vanuit een kopie in %TEMP%, omdat deze map tijdens het opruimen verdwijnt.
if not "%~1"=="--vanuit-temp" (
    copy /y "%~f0" "%TEMP%\geest-opruimen.bat" >nul
    "%TEMP%\geest-opruimen.bat" --vanuit-temp "%~dp0"
)
cd /d "%TEMP%"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~2beheer\geest.ps1" -Actie Opruimen
pause
(goto) 2>nul & del "%~f0"