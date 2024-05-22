#!/bin/bash

echo "Installing required programs. Please wait..."

pip install -r requirements.txt > /dev/null

if [ $? -eq 0 ]
then
    echo "Installation completed successfully"
else
    echo "Installation failed"
    exit 1
fi

python main.py
