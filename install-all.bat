@echo off
echo ========================================
echo Installing All Dependencies
echo ========================================
echo.
echo Installing Frontend Dependencies...
call npm install
echo.
echo Installing Backend Dependencies...
cd backend
call pip install -r requirements.txt
cd ..
echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo To run the application:
echo 1. Double-click start-backend.bat
echo 2. Double-click start-frontend.bat
echo.
pause
