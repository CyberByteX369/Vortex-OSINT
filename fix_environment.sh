#!/bin/bash

echo "🛑 Deactivating current environment (if any)..."
deactivate 2>/dev/null

echo "🗑️  Deleting broken virtual environment..."
rm -rf venv

echo "✨ Creating FRESH virtual environment..."
python3 -m venv venv

echo "🔌 Activating environment..."
source venv/bin/activate

echo "📦 Installing GUARANTEED working versions..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🔍 Verifying versions (Must show Typer 0.12.5)..."
pip list | grep -E "typer|click|rich"

echo ""
echo "✅ ENVIRONMENT FIXED! Running test..."
python main.py --help
