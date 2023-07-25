# JavaScript Web Scraping Tasks

This repository contains JavaScript scripts for various web scraping tasks. Below is a brief description of each task along with instructions on how to run the scripts.

## [Task 0 - Readme](./0-readme.js)

**Description:**
This script reads and prints the content of a file. It takes the file path as the first argument and reads the content in utf-8 format. If any error occurs during reading, it will print the error object.

**Usage:**
```bash
$ ./0-readme.js <file_path>
```

## [Task 1 - Write me](./1-writeme.js)

**Description:**
This script writes a string to a file. It takes the file path as the first argument and the string to write as the second argument. The content is written in utf-8 format. If any error occurs during writing, it will print the error object.

**Usage:**
```bash
$ ./1-writeme.js <file_path> "<string_to_write>"
```

## [Task 2 - Status code](./2-statuscode.js)

**Description:**
This script displays the status code of a GET request to the provided URL. It uses the `request` module to perform the request.

**Usage:**
```bash
$ ./2-statuscode.js <URL>
```

## [Task 3 - Star wars movie title](./3-starwars_title.js)

**Description:**
This script prints the title of a Star Wars movie based on the provided movie ID. It uses the Star wars API with the endpoint `https://swapi-api.alx-tools.com/api/films/:id` and the `request` module.

**Usage:**
```bash
$ ./3-starwars_title.js <movie_ID>
```

## [Task 4 - Star wars Wedge Antilles](./4-starwars_count.js)

**Description:**
This script prints the number of movies where the character "Wedge Antilles" is present. It uses the Star wars API with the provided API URL (`https://swapi-api.alx-tools.com/api/films/`) and filters the result based on the character ID.

**Usage:**
```bash
$ ./4-starwars_count.js <API_URL>
```

## [Task 5 - Loripsum](./5-request_store.js)

**Description:**
This script gets the contents of a webpage and stores it in a file. It takes the URL to request as the first argument and the file path to store the body response as the second argument. The file will be UTF-8 encoded. It uses the `request` module.

**Usage:**
```bash
$ ./5-request_store.js <URL> <file_path>
```

## [Task 6 - How many completed?](./6-completed_tasks.js)

**Description:**
This script computes the number of tasks completed by user id. It takes the API URL (`https://jsonplaceholder.typicode.com/todos`) as the first argument and only prints users with completed tasks. It uses the `request` module.

**Usage:**
```bash
$ ./6-completed_tasks.js <API_URL>
```

## [Task 7 - Who was playing in this movie?](./100-starwars_characters.js)

**Description:**
This is an advanced script that prints all characters of a Star Wars movie based on the provided Movie ID. It uses the Star wars API and the `request` module.

**Usage:**
```bash
$ ./100-starwars_characters.js <movie_ID>
```

## [Task 8 - Right order](./101-starwars_characters.js)

**Description:**
This is an advanced script that prints all characters of a Star Wars movie based on the provided Movie ID in the same order as the list "characters" in the /films/ response. It uses the Star wars API and the `request` module.

**Usage:**
```bash
$ ./101-starwars_characters.js <movie_ID>
```
