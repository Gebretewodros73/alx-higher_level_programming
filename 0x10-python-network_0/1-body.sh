#!/bin/bash
# sends a GET request to the URL using curl, and displays the body of the response only if the response status code is 200:
curl -s "$1"
