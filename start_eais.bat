@echo off
REM EAIS Startup Script (Windows)

echo Enhanced Enterprise Architecture Intelligence System (EAIS)
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.10 or higher and add it to your PATH
    pause
    exit /b 1
)

REM Check if pip is installed
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: pip is not installed or not in PATH
    echo Please ensure pip is installed with Python
    pause
    exit /b 1
)

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Create directories
if not exist "data" mkdir data
if not exist "logs" mkdir logs
if not exist "output" mkdir output

REM Check environment variables
if "%OPENAI_API_KEY%"=="" (
    echo Warning: OPENAI_API_KEY environment variable is not set
    echo Please set it before running the application:
    echo   set OPENAI_API_KEY=your-api-key-here
)

REM Present options to user
echo.
echo Choose how to start EAIS:
echo 1. Streamlit UI (Recommended - Modern Web Interface)
echo 2. Next.js Integration Portal (Professional Console)
echo 3. Docker Compose (All Services)
echo 4. Command Line Interface
echo.
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo Starting EAIS Streamlit Application...
    echo Access the application at: http://localhost:8501
    echo.
    python run_streamlit_app.py
) else if "%choice%"=="2" (
    echo.
    echo Starting Next.js Integration Portal...
    echo Backend: http://localhost:8000
    echo Portal: http://localhost:3000
    echo.
    start /b python run_full_system.py
    timeout /t 5 /nobreak >nul
    start http://localhost:3000
) else if "%choice%"=="3" (
    echo.
    echo Starting EAIS with Docker Compose...
    echo Streamlit UI: http://localhost:8503
    echo Flask API: http://localhost:8000
    echo Portal UI: http://localhost:3000
    echo.
    docker-compose up --build
) else if "%choice%"=="4" (
    echo.
    echo Starting EAIS Command Line Interface...
    python src\enhanced_enterprise_architecture_intelligence_system_e_eais\app.py
) else (
    echo Invalid choice. Starting Streamlit UI by default...
    echo.
    python run_streamlit_app.py
)

pause