@echo off
echo Installing required programs. Please wait...

pip install -r requirements.txt > NUL 2>&1

if %ERRORLEVEL% == 0 (
    echo Installation completed successfully
) else (
    echo Installation failed
    exit /b 1
)

python main.py
