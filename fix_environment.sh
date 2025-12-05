#!/bin/bash

echo "🗑️  Cleaning up broken environment..."
rm -rf venv

echo "✨ Creating fresh virtual environment..."
python3 -m venv venv

echo "🔌 Activating environment..."
source venv/bin/activate

echo "📦 Installing correct versions..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ FIXED! Try running the tool now:"
echo "   source venv/bin/activate"
echo "   python main.py --help"
