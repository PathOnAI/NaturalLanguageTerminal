@echo off
setlocal enabledelayedexpansion

if "%1"=="" goto :no_args
if "%1"=="disable" goto :disable_alias
goto :invalid_arg

:no_args
where python >nul 2>&1
if %errorlevel% equ 0 (
    set "nlt_PYTHON_PATH=python"
    goto :setup_alias
)

where python3 >nul 2>&1
if %errorlevel% equ 0 (
    set "nlt_PYTHON_PATH=python3"
    goto :setup_alias
)

exit /b 1

:setup_alias
set "TEMP_FILE=%TEMP%\git_alias_command.txt"

for %%I in ("%~dp0..\..") do set "PARENT_FOLDER=%%~nxI"

git config --global alias.autocommit "^!%nlt_PYTHON_PATH% -c \"from nlt.git.autocommit import main; main()\""

set GIT_AUTOCOMMIT_ACTIVE=1

:: Define the escape character
for /F %%a in ('echo prompt $E ^| cmd') do set "ESC=%%a"

:: Set the colored prefix
set "NAVY_BLUE_PREFIX=%ESC%[94m(nlt~%PARENT_FOLDER%)%ESC%[0m"

:: Modify the prompt
prompt %NAVY_BLUE_PREFIX% $P$G

:: Start a new command prompt session
cmd /k

del "%TEMP_FILE%"
exit /b 0

:disable_alias
git config --global --unset alias.autocommit
set GIT_AUTOCOMMIT_ACTIVE=0
prompt $P$G
cmd /k
exit /b 0

:invalid_arg
exit /b 1