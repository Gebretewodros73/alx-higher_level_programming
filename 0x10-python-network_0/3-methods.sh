#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept
URL="$1"
METHODS=$(curl -sI "$URL" | grep "Allow" | cut -d' ' -f2-)

echo "$METHODS"
