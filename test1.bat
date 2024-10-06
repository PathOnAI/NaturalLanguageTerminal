@echo off
setlocal EnableDelayedExpansion

:: Define the escape character
for /F %%a in ('echo prompt $E ^| cmd') do set "ESC=%%a"

:: Set the colored prefix
set "GREEN_PREFIX=%ESC%[32m(prefix)%ESC%[0m"

:: Modify the prompt
prompt %GREEN_PREFIX% $P$G

:: Start a new command prompt session
cmd /k