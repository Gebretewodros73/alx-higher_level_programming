#!/bin/bash
# Usage: ./0-body_size.sh <URL> Send a GET request to the provided URL of the response headers
curl -s "$1" | wc -c
