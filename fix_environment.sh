#!/usr/bin/env bash

# --- OS DETECTION & PREP ---
if [[ "$OSTYPE" == "linux-android" ]] || [ -d "/data/data/com.termux" ]; then
    # --- TERMUX (Android) ---
    echo "📱 Termux detected!"
    echo "🔧 Installing build dependencies (Required for Pydantic/Rust)..."
    pkg update -y
    pkg install python rust binutils clang make -y
    echo "✅ Termux dependencies installed."

elif [ -f "/etc/debian_version" ]; then
    # --- KALI LINUX / UBUNTU / DEBIAN ---
    echo "🐧 Kali/Debian Linux detected!"
    echo "🔧 Installing python3-venv (Required for Virtual Envs)..."
    
    # We use sudo here because Kali requires root for apt
    # 2>/dev/null hides errors if the user is already root
    sudo apt-get update
    sudo apt-get install -y python3-venv python3-pip python3-dev build-essential
    echo "✅ System dependencies installed."
fi

# --- VIRTUAL ENVIRONMENT RESET ---
echo "🛑 Deactivating current environment (if any)..."
deactivate 2>/dev/null || true

echo "🗑️  Deleting broken virtual environment..."
rm -rf venv

echo "✨ Creating FRESH virtual environment..."
# This command often fails on Kali if python3-venv isn't installed (fixed above)
python3 -m venv venv

echo "🔌 Activating environment..."
source venv/bin/activate

echo "📦 Installing SPECIFIC FIXED VERSIONS (Direct Install)..."
pip install --upgrade pip

# Installing known compatible versions to prevent conflicts
pip install "typer==0.12.5" "click==8.1.7" "rich==13.9.4" "httpx==0.27.2" "dnspython==2.7.0" "pydantic==2.9.2" "aiofiles==24.1.0"

echo "📝 Overwriting requirements.txt with these working versions..."
pip freeze > requirements.txt

echo "🔍 Verifying versions..."
pip list | grep -E "typer|click"

echo ""
echo "✅ ENVIRONMENT FIXED! Running test..."
./venv/bin/python main.py --help
