# JavaScript Warm Up

This repository contains a collection of JavaScript scripts that serve as warm-up exercises. Each script performs a specific task and is designed to help you practice and improve your JavaScript skills.

## Tasks

### 0. First constant, first print

**Mandatory**

Write a script that prints "JavaScript is amazing".

- You must create a constant variable called `myVar` with the value "JavaScript is amazing".
- You must use `console.log(...)` to print the output.
- You are not allowed to use `var`.

**Usage:**
$ ./0-javascript_is_amazing.js
    
JavaScript is amazing


**File:** [0-javascript_is_amazing.js](./0-javascript_is_amazing.js)

### 1. 3 languages

**Mandatory**

Write a script that prints 3 lines:

- The first line: "C is fun"
- The second line: "Python is cool"
- The third line: "JavaScript is amazing"

You must use `console.log(...)` to print the output.
You are not allowed to use `var`.

**Usage:**
./1-multi_languages.js

C is fun

Python is cool

JavaScript is amazing


**File:** [1-multi_languages.js](./1-multi_languages.js)

### 2. Arguments

**Mandatory**

Write a script that prints a message depending on the number of arguments passed:

- If no arguments are passed to the script, print "No argument".
- If only one argument is passed to the script, print "Argument found".
- Otherwise, print "Arguments found".

You must use `console.log(...)` to print the output.
You are not allowed to use `var`.
You can use the `process.argv` array to access the script arguments.

**Usage:**
$./2-arguments.js

No argument

$./2-arguments.js Best

Argument found

$./2-arguments.js Best School

Arguments found
