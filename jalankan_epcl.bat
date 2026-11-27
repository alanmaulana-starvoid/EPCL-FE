@echo off
title EPCL-FE v1.0 - Mode Interaktif
cls

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [GAGAL] Python belum terinstal di komputer ini!
    echo Silakan hubungi guru atau instal Python 3 terlebih dahulu.
    pause
    exit /b
)

python epcl.py
pause
