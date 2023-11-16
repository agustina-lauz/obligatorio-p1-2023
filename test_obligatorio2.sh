#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <main_menu.py> <prueba.txt>"
    exit 1
fi

# Assign the arguments to variables
python_script="$1"
input_file="$2"

# Check if the Python script exists
if [ ! -f "$python_script" ]; then
    echo "Error: Python script '$python_script' not found."
    exit 1
fi

# Check if the input file exists
if [ ! -f "$input_file" ]; then
    echo "Error: Input file '$input_file' not found."
    exit 1
fi

# Run the Python script with input redirected from the file
(cat "$input_file"; echo "6") | python3 "$python_script"
