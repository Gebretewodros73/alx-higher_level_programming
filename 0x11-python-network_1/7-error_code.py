#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
If the HTTP status code is >= 400, prints "Error code:"
followed by the status code.
Uses the requests and sys packages.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
