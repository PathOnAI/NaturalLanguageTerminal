@echo off
setlocal enabledelayedexpansion

echo Method 1: Caret Escaping
echo This is an exclamation mark: ^!

echo.
echo Method 2: Delayed Expansion with Caret
set "message=This is an exclamation mark: ^!"
echo !message!

echo.
echo Method 3: Immediate Expansion
set "message=This is an exclamation mark: !"
echo %message%

echo.
echo Method 4: Using Special Character Code
echo This is an exclamation mark: ^^!

echo.
echo Method 5: Echo without quotes
echo This is an exclamation mark: !