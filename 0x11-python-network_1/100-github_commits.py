#!/usr/bin/python3
"""
Retrieves the 10 most recent commits from a GitHub
repository and prints the commit SHA and author name.
Uses the GitHub API and the requests package.
"""

import requests
import sys

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(url)

    try:
        data = response.json()
        commits = data[:10]  # Get the 10 most recent commits

        for commit in commits:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")
    except ValueError:
        print("Error: Invalid JSON response")

