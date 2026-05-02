#!/bin/bash

# Ireland SAR Toolkit v2.1 Setup Script
# Run this script to set up the toolkit for the first time.

set -e

echo "🛠️  Setting up Ireland SAR Toolkit v2.1..."

# Check Python 3.8+
PY_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
PY_MAJOR=$(echo "$PY_VERSION" | cut -d. -f1)
PY_MINOR=$(echo "$PY_VERSION" | cut -d. -f2)

if [ "$PY_MAJOR" -lt 3 ] || ([ "$PY_MAJOR" -eq 3 ] && [ "$PY_MINOR" -lt 8 ]); then
    echo "❌ Python 3.8+ is required. Found: $PY_VERSION"
    exit 1
fi

echo "✅ Python $PY_VERSION detected"

# Create a virtual environment
echo "🔹 Creating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
echo "🔹 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Copy my_details.json template if it doesn't exist
if [ ! -f "config/my_details.json" ]; then
    echo "🔹 Copying my_details_template.json to my_details.json..."
    cp config/my_details_template.json config/my_details.json
    echo "✏️  Edit config/my_details.json with your personal details."
fi

# Create output directories
mkdir -p output forensic responses

# Initialize tracker if it doesn't exist
if [ ! -f "tracking/sar_tracker.csv" ]; then
    echo "🔹 Initializing SAR tracker..."
    cp tracking/sar_tracker_template.csv tracking/sar_tracker.csv
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit config/my_details.json with your personal details."
echo "2. Review templates/ and add agency-specific templates as needed."
echo "3. Run: python scripts/generate_sar.py --list-agencies"
echo "4. Run: python scripts/generate_sar.py --all --custodian "Your Name""
echo ""
echo "To activate the virtual environment later:"
echo "  source .venv/bin/activate"
