@echo off
echo Iniciando Backend LolliPop ERP...
cd /d %~dp0
cd development\backend
.venv\Scripts\python -m uvicorn main:app --port 8000 --reload --host 127.0.0.1
pause
