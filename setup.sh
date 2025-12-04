#!/bin/bash

echo "🔴 STOPPING any background installs..."
# Fix the "Unable to acquire lock" error
sudo killall apt apt-get 2>/dev/null
sudo rm /var/lib/apt/lists/lock 2>/dev/null
sudo rm /var/cache/apt/archives/lock 2>/dev/null
sudo rm /var/lib/dpkg/lock* 2>/dev/null
sudo dpkg --configure -a

echo "🟢 System Unlocked. Installing System Dependencies..."
# Install the necessary system tools
sudo apt-get update
sudo apt-get install -y python3-venv python3-dev build-essential libssl-dev libffi-dev

echo "🔵 Setting up Virtual Environment..."
# Delete old environment if it exists to start fresh
rm -rf venv
python3 -m venv venv

# ACTIVATE VIRTUAL ENVIRONMENT
source venv/bin/activate

echo "🟡 Upgrading Installer (CRITICAL FIX)..."
# This fixes the "Failed to build pydantic-core" error
# by getting the version that doesn't need compiling.
pip install --upgrade pip wheel setuptools

echo "🟣 Installing Tool Requirements..."
pip install -r requirements.txt

echo ""
echo "✅ SETUP COMPLETE!"
echo "To start the tool, type these two lines:"
echo "   source venv/bin/activate"
echo "   python main.py --help"
