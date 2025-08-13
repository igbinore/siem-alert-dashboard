@echo off
REM === Activate virtual environment ===
call venv\Scripts\activate

REM === Start FastAPI backend in a new window ===
start cmd /k "cd backend && uvicorn app:app --reload --port 8000"

REM === Start simple HTTP server for frontend in a new window ===
start cmd /k "cd frontend && python -m http.server 5500"

echo Dashboard starting...
echo Backend:   http://127.0.0.1:8000
echo Frontend:  http://127.0.0.1:5500/index.html
pause
