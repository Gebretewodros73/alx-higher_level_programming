# 0x10-python-network_0

## Description
This directory contains Python and Bash scripts related to network programming and HTTP requests. It covers various concepts and tasks related to network protocols, URL handling, cURL, and API interactions.

## Table of Contents
* [Introduction](#introduction)
* [Learning Objectives](#learning-objectives)
* [Tasks](#tasks)
* [Conclusion](#conclusion)

## Introduction
In this project, you will explore the fundamentals of network programming and HTTP using Python and Bash scripts. You will learn about URL structure, HTTP methods, request/response handling, headers, cookies, and more. The tasks will require you to write scripts that interact with web servers, send HTTP requests, and process the responses.

## Learning Objectives
By the end of this project, you should be able to explain the following concepts without the help of Google:
- What a URL is
- What HTTP is
- How to read a URL
- The scheme for an HTTP URL
- What a domain name is
- What a sub-domain is
- How to define a port number in a URL
- What a query string is
- What an HTTP request is
- What an HTTP response is
- What HTTP headers are
- What the HTTP message body is
- What an HTTP request method is
- What an HTTP response status code is
- What an HTTP Cookie is
- How to make a request with cURL
- What happens when you type google.com in your browser (Application level)

## Tasks
The project includes the following tasks:

0. [cURL body size](./0-body_size.sh)
Write a Bash script that takes a URL as input, sends a request to thatURL, and displays the size of the response body in bytes.
1. [cURL to the end](./1-body.sh)
Write a Bash script that takes a URL as input, sends a GET request to that URL, and displays the body of the response. Only the body of a 200 status code response should be displayed.
2. [cURL Method](./2-delete.sh)
Write a Bash script that sends a DELETE request to a given URL and displays the body of the response.
3. [cURL only methods](./3-methods.sh)
Write a Bash script that takes a URL as input and displays all the HTTP methods that the server accepts.
4. [cURL headers](./4-header.sh)
Write a Bash script that takes a URL as input, sends a GET request to that URL with a specific header, and displays the body of the response.
5. [cURL POST parameters](./5-post_params.sh)
Write a Bash script that takes a URL as input, sends a POST request to that URL with specific parameters, and displays the body of the response.
6. [Find a peak](./6-peak.py)
Write a function find_peak in Python that finds a peak in a list of unsorted integers. The function should return one of the peaks. The algorithm should have the lowest complexity possible.
7. [Only status code](./100-status_code.sh)
Write a Bash script that sends a request to a URL and displays only the status code of the response. The script should not use any pipes, redirections, or semicolons.
8. [cURL a JSON file](./101-post_json.sh)
Write a Bash script that sends a JSON POST request to a URL with the contents of a file as the body of the request. The script should display the body of the response.
9. [Catch me if you can!](./102-catch_me.sh)
Write a Bash script that makes a request to a specific URL, causing the server to respond with a message containing "You got me!" in the body of the response. The script should not use echo, cat, or similar commands to display the final result.

Please refer to each task's respective file for more details and instructions.

## Conclusion
This project provides hands-on experience with network programming and HTTP requests using Python and Bash scripts. By completing the tasks, you will gain a solid understanding of various network-related concepts and enhance your skills in interacting with web servers and APIs.

Remember to adhere to the guidelines and requirements mentioned in each task, such as file structure, script execution, documentation, and testing. Good luck with the project!

