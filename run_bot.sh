#!/bin/bash

# Aktifkan virtualenv kalau ada
# source venv/bin/activate

echo "Install dependencies..."
pip install -r requirements.txt

echo "Jalankan bot..."
python3 bot.py
