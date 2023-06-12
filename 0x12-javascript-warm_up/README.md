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
- If only one argument is passed to the script, print "Argument found".- Otherwise, print "Arguments found".

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

**File:** [2-arguments.js](./2-arguments.js)

### 3. Value of my argument

**Mandatory**

Write a script that prints the first argument passed to it:

- If no arguments are passed to the script, print "No argument".
- You must use `console.log(...)` to print the output.
- You are not allowed to use `var`.
- You are not allowed to use `length`.

**Usage:**

$ ./3-value_argument.js

No argument

$ ./3-value_argument.js School

School

**File:** [3-value_argument.js](./3-value_argument.js)

### 4. Create a sentence

**Mandatory**

Write a script that prints two arguments passed to it in the following format: "arg1 is arg2".

- You must use `console.log(...)` to print the output.
- You are not allowed to use `var`.

**Usage:**

$ ./4-concat.js c cool

c is cool

$ ./4-concat.js c

c is undefined

$ ./4-concat.js

undefined is undefined

**File:** [4-concat.js](./4-concat.js)

### 5. An Integer

**Mandatory**

Write a script that prints "My number: <first argument converted to an integer>" if the first argument can be converted to an integer.

- If the argument can't be converted to an integer, print "Not a number".
- You must use `console.log(...)` to print the output.
- You are not allowed to use `var`.
- You are not allowed to use `try/catch`.

**Usage:**

$ ./5-to_integer.js

Not a number

$ ./5-to_integer.js 89

My number: 89

$ ./5-to_integer.js "89"

My number: 89

$ ./5-to_integer.js 89.89

My number: 89

$ ./5-to_integer.js School

Not a number

**File:** [5-to_integer.js](./5-to_integer.js)

### 6. Loop to languages

**Mandatory**

Write a script that prints 3 lines: "C is fun", "Python is cool", and "JavaScript is amazing".

- You must use an array of strings and a loop.
- You are not allowed to use `var`.
- You must use `console.log(...)` to print the output.

**Usage:**

$ ./6-multi_languages_loop.js

C is fun

Python is cool

JavaScript is amazing


**File:** [6-multi_languages_loop.js](./6-multi_languages_loop.js)

### 7. I love C

**Mandatory**

Write a script that prints "C is fun" `x` times, where `x` is the first argument passed to the script.

- If the first argument can't be converted to a number, print "Missing number of occurrences".
- You must use a loop (`while`, `for`, etc.).
- You are not allowed to use `var`.
- You must use `console.log(...)` to print the output.

**Usage:**

$ ./7-multi_c.js 2

C is fun

C is fun

$ ./7-multi_c.js

Missing number of occurrences

$ ./7-multi_c.js -3

$


**File:** [7-multi_c.js](./7-multi_c.js)

### 8. Square

**Mandatory**

Write a script that prints a square.

- The first argument is the size of the square.
- If the first argument can't be converted to a number, print "Missing size".
- You must use the character `X` to print the square.
- You must use `console.log(...)` to print each line of the square.
- You are not allowed to use `var`.

**Usage:**

$ ./8-square.js 2

XX

XX

$ ./8-square.js 5

XXXXX

XXXXX

XXXXX

XXXXX

XXXXX

$ ./8-square.js

Missing size


**File:** [8-square.js](./8-square.js)

### 9. Add

**Mandatory**

Write a script that prints the addition of 2 integers.

- The first argument is the first integer.
- The second argument is the second integer.
- You have to define a function with this prototype: `function add(a, b)`.
- You must use `console.log(...)` to print the output.
- You are not allowed to use `var`.

**Usage:**

$ ./9-add.js 1 2

3

$ ./9-add.js 4 5

9

$ ./9-add.js

NaN

**File:** [9-add.js](./9-add.js)

### 10. Factorial

**Mandatory**

Write a script that computes and prints the factorial of a given integer.

- The first argument is the integer used for the computation.
- You have to define a function with this prototype: `function factorial(n)`.
- You must use `console.log(...)` to print the output.
- You are not allowed to use `var`.
- You are not allowed to use `Math`.

**Usage:**

$ ./10-factorial.js 3

6

$ ./10-factorial.js 5

120

$ ./10-factorial.js

1

**File:** [10-factorial.js](./10-factorial.js)

### 11. Second biggest!

**Mandatory**

Write a script that searches the second biggest integer in the list of arguments.

- You can assume all arguments can be converted to integer.
- If no argument passed, print 0.
- If the number of arguments is 1, print 0.
- You must use `console.log(...)` to print the output.
- You are not allowed to use `var`.

**Usage:**

./11-second_biggest.js

0

./11-second_biggest.js 1

0

$ ./11-second_biggest.js 4 2 5 3 0 -3

4


**File:** [11-second_biggest.js](./11-second_biggest.js)

### 12. Object

**Mandatory**

Update this script to replace the value `12` with `89`:

```javascript
const myObject = {
  type: 'object',
  value: 12
};

- You are not allowed to use `var`.

**Usage:**

./12-object.js

{ type: 'object', value: 12 }

{ type: 'object', value: 89 }```

**File:** [12-object.js](./12-object.js)

## Advanced Tasks

