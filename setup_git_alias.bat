@echo off
setlocal enabledelayedexpansion

REM Check if an argument is provided
if "%1"=="" goto :no_args
if "%1"=="check" goto :check_alias
if "%1"=="disable" goto :disable_alias
goto :invalid_arg

:no_args
REM Check for Python
where python >nul 2>&1
if %errorlevel% equ 0 (
    set "NLS_PYTHON_PATH=python"
    goto :setup_alias
)

REM If Python not found, check for Python3
where python3 >nul 2>&1
if %errorlevel% equ 0 (
    set "NLS_PYTHON_PATH=python3"
    goto :setup_alias
)

echo Error: Neither python nor python3 found in PATH
exit /b 1

:setup_alias
REM Set up the Git alias using a temporary file
set "TEMP_FILE=%TEMP%\git_alias_command.txt"
echo !%NLS_PYTHON_PATH% -c "from nls.git.autocommit import main; main()" > "%TEMP_FILE%"

git config --global alias.autocommit "^!%NLS_PYTHON_PATH% -c \"from nls.git.autocommit import main; main()\""

echo Git alias 'autocommit' has been set up.
echo Alias command:
type "%TEMP_FILE%"
del "%TEMP_FILE%"
exit /b 0

:check_alias
REM Check if the alias exists
git config --global --get alias.autocommit
if %errorlevel% equ 0 (
    echo Git alias 'autocommit' is active.
    exit /b 0
) else (
    echo Git alias 'autocommit' is not active.
    exit /b 1
)

:disable_alias
REM Remove the alias
git config --global --unset alias.autocommit
if %errorlevel% equ 0 (
    echo Git alias 'autocommit' has been removed.
    exit /b 0
) else (
    echo Failed to remove Git alias 'autocommit'. It may not exist.
    exit /b 1
)

:invalid_arg
echo Invalid argument. Use 'check' to check alias status or 'disable' to remove the alias.
exit /b 1