#!/bin/bash

URL="$1"
METHODS=$(curl -sI "$URL" | grep "Allow" | cut -d' ' -f2-)

echo "$METHODS"
