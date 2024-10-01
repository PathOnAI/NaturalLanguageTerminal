@echo off
set "SCRIPT_DIR=%~dp0"
set "FILE_DIR=%~dp0"

rem Save the current PATH and PROMPT
set "OLD_PATH=%PATH%"
set "OLD_PROMPT=%PROMPT%"

rem Add the script directory to PATH
set "PATH=%SCRIPT_DIR%;%PATH%"

rem Save the current Python interpreter path
for /f "delims=" %%i in ('where python') do set "NLS_PYTHON_PATH=%%i"

rem Create the git-autocommit alias (updated for Git Bash compatibility)
rem git config --global alias.autocommit "!cmd //c \"\\\"%%NLS_PYTHON_PATH%%\\\" -c \\\"from nls.git.autocommit import main; main()\\\"\""

doskey nls_end=%FILE_DIR%nls_end.bat

rem Set a flag to indicate NLS is active
set "NLS_ACTIVE=1"

call "%FILE_DIR%nls_interceptor.bat"

rem Modify PROMPT to show the active environment
set "PROMPT=[{{ENV_NAME}}] %PROMPT%"

echo.
echo ┌────────────────────────────────────────────┐
echo │                                            │
echo │   NLS environment activated successfully   │
echo │                                            │
echo ├────────────────────────────────────────────┤
echo │                                            │
echo │   Environment: {{ENV_NAME}}                     │
echo │   To end the session, type: nls_end          │
echo │                                            │
echo └────────────────────────────────────────────┘
echo.