#!/bin/bash
# Setup script for Code Security Evaluation System
# This script automates the installation and setup process

set -e  # Exit on error

echo "=========================================="
echo "Code Security Evaluation System Setup"
echo "=========================================="
echo ""

# Check Python version
echo "Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "Found Python $PYTHON_VERSION"

# Check if version is 3.8 or higher
if [ "$(printf '%s\n' "3.8" "$PYTHON_VERSION" | sort -V | head -n1)" != "3.8" ]; then
    echo "Warning: Python 3.8+ is recommended. Current version: $PYTHON_VERSION"
fi

# Create virtual environment
echo ""
echo "Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created"
else
    echo "Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo ""
echo "Installing dependencies..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "Dependencies installed successfully"
else
    echo "Warning: requirements.txt not found"
fi

# Check for OpenAI API key
echo ""
echo "Checking for OpenAI API key..."
if [ -z "$OPENAI_API_KEY" ]; then
    echo "Warning: OPENAI_API_KEY environment variable is not set"
    echo "Please set it with: export OPENAI_API_KEY='your-api-key-here'"
else
    echo "OpenAI API key is set"
fi

# Verify Bandit installation
echo ""
echo "Verifying Bandit installation..."
if command -v bandit &> /dev/null; then
    BANDIT_VERSION=$(bandit --version 2>&1 | head -n1)
    echo "Bandit installed: $BANDIT_VERSION"
else
    echo "Warning: Bandit not found in PATH"
    echo "Installing Bandit..."
    pip install bandit
fi

# Verify other key packages
echo ""
echo "Verifying key packages..."
python3 -c "import pandas, numpy, matplotlib, seaborn, openai; print('All key packages installed!')" 2>/dev/null || {
    echo "Error: Some packages are missing"
    exit 1
}

# Create evaluation_results directory
echo ""
echo "Creating output directories..."
mkdir -p evaluation_results
echo "Output directory created"

# Summary
echo ""
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Set OpenAI API key: export OPENAI_API_KEY='your-key'"
echo "3. Run evaluation: python evaluate_and_visualize.py --max-samples 10"
echo ""
echo "For detailed instructions, see TUTORIAL.md"
echo ""

