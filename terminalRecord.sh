#!/bin/bash

# This code is used to record your terminal session

echo "Starting terminal recording..."
echo "Please enter the filename to save the recording (default: terminal_recording.txt):"
read filename

if [[ -z "$filename"]]; then
    echo "No filename provided. Using default: terminal_recording.txt"
    filename="terminal_recording.txt"
fi

script -a "$filename"

echo "Recording saved to: ${filename}"
