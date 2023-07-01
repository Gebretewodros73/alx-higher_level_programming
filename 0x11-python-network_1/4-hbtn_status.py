#!/usr/bin/python3
"""
Fetches a URL and displays the body of the response.
Uses the requests package.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    body = response.text

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
