@echo off

rem Unset the git alias
git config --global --unset alias.autocommit

rem Restore the old PATH and PROMPT
set "PATH=%OLD_PATH%"
set "PROMPT=%OLD_PROMPT%"

rem Unset NLS-specific environment variables
set "NLS_ACTIVE="
set "NLS_PYTHON_PATH="
set "OLD_PATH="
set "OLD_PROMPT="

echo.
echo ┌────────────────────────────────────────────┐
echo │                                            │
echo │   NLS environment deactivated successfully │
echo │                                            │
echo └────────────────────────────────────────────┘
echo.
