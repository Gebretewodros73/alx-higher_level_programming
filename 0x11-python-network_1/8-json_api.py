#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter.
If the response body is properly JSON formatted and not
empty, displays the id and name.
Otherwise, displays an appropriate error message.
Uses the requests and sys packages.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    payload = {"q": letter}
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
