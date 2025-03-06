#!/bin/bash

# Step 1: Update package list and install Python if not installed
sudo apt update && sudo apt install -y python3 python3-venv python3-pip

# Step 2: Create a virtual environment if it doesn't exist
if [ ! -d "pdfvenv" ]; then
    python3 -m venv pdfvenv
    echo "Virtual environment 'pdfvenv' created."
fi

# Step 3: Activate the virtual environment
source pdfvenv/bin/activate

# Step 4: Install required Python packages
pip install --upgrade pip
pip install -r requirements.txt

# Step 5: Run the Streamlit app
streamlit run HOME.py
