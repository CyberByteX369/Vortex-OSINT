#!/bin/bash

echo "[*] Setting up Vortex-OSINT..."

# Check if python3-venv is installed
if ! dpkg -s python3-venv >/dev/null 2>&1; then
    echo "[!] Installing python3-venv..."
    sudo apt-get update
    sudo apt-get install -y python3-venv
fi

# Create Virtual Environment
echo "[*] Creating virtual environment 'venv'..."
python3 -m venv venv

# Activate and Install
echo "[*] Installing dependencies inside venv..."
source venv/bin/activate
pip install -r requirements.txt

echo ""
echo "✅ Setup Complete!"
echo "To run the tool, type:"
echo "   source venv/bin/activate"
echo "   python main.py --help"
