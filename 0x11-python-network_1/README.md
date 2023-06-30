# 0x11. Python - Network #1

This repository contains Python scripts for performing network-related tasks using the urllib and requests packages.

## Table of Contents

* [General Info](#general-info)
* [Tasks](#tasks)
* [Conclusion](#conclusion)

## General Info

In this project, expected to learn how to fetch internet resources, make HTTP requests, handle errors, and manipulate data from external services using Python. The tasks in this project are designed to help you gain familiarity with the urllib and requests packages and develop your skills in working with network-related operations.

## Tasks

### 0. What's my status? #0
- File: [0-hbtn_status.py](./0-hbtn_status.py)
- Write a Python script that fetches `https://alx-intranet.hbtn.io/status` using `urllib`.
- The body of the response must be displayed as shown in the example.

### 1. Response header value #0
- File: [1-hbtn_header.py](.1-hbtn_header.py)
- Write a Python script that takes in a URL and sends a request to the URL.
- Display the value of the `X-Request-Id` variable found in the header of the response.

### 2. POST an email #0
- File: [2-post_email.py](./2-post_email.py)
- Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8).

### 3. Error code #0
- File: [3-error_code.py](./3-error_code.py)
- Write a Python script that takes in a URL, sends a request to the URL, and displays the body of the response.
- Handle HTTP errors using `urllib.error.HTTPError` exceptions.

### 4. What's my status? #1
- File: [4-hbtn_status.py](./4-hbtn_status.py)
- Write a Python script that fetches `https://alx-intranet.hbtn.io/status` using the `requests` package.
- The body of the response must be displayed as shown in the example.

### 5. Response header value #1
- File: [5-hbtn_header.py](./5-hbtn_header.py)
- Write a Python script that takes in a URL and sends a request to the URL.
- Display the value of the variable `X-Request-Id` in the response header.

### 6. POST an email #1
- File: [6-post_email.py](./6-post_email.py)
- Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response.

### 7. Error code #1
- File: [7-error_code.py](./7-error_code.py)
- Write a Python script that takes in a URL, sends a request to the URL, and displays the body of the response.
- If the HTTP status code is greater than or equal to 400, print "Error code:" followed by the value of the HTTP status code.

### 8. Search API
- File: [8-json_api.py](./8-json_api.py)
- Write a Python script that takes in a letter and sends a POST request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.
- Display the JSON response as described in the task.

### 9. My GitHub!
- File: [10-my_github.py](./10-my_github.py)
- Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id.

### 10. Time for an interview!
- File: [100-github_commits.py](./100-github_commits.py)
- Write a Python script that takes in 2 arguments and retrieves the most recent 10 commits from the repository "rails" by the user "rails" using the GitHub API.

## Conclusion

This project provides hands-on experience in working with network requests and APIs using Python. By completing the tasks, you will become familiar with fetching internet resources, making HTTP requests, handling errors, and extracting data from responses. These skills are essential for back-end development and interacting with external services. Enjoy coding!
