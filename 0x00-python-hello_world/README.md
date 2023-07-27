# 0x00. Python - Hello, World

## Description
This directory contains a collection of Python scripts that explore various programming concepts and challenges. Each script is designed to solve a specific problem or demonstrate a particular concept in Python programming.

## Table of Contents
* [Task 0: Run Python file](#task-0-run-python-file)
* [Task 1: Run inline](#task-1-run-inline)
* [Task 2: Hello, print](#task-2-hello-print)
* [Task 3: Print integer](#task-3-print-integer)
* [Task 4: Print float](#task-4-print-float)
* [Task 5: Print string](#task-5-print-string)
* [Task 6: Play with strings](#task-6-play-with-strings)
* [Task 7: Copy - Cut - Paste](#task-7-copy-cut-paste)
* [Task 8: Create a new sentence](#task-8-create-a-new-sentence)
* [Task 9: Easter Egg](#task-9-easter-egg)
* [Task 10: Linked list cycle](#task-10-linked-list-cycle)
* [Task 11: Hello, write](#task-11-hello-write)
* [Task 12: Compile](#task-12-compile)
* [Task 13: ByteCode -> Python #1](#task-13-bytecode-python-1)

## Task 0: Run Python file
* Description: This script is a Shell script that runs a Python script.
* Environment variable `$PYFILE` contains the Python file name.
* The Python script prints "Best School".
* File: [0-run](./0-run)

## Task 1: Run inline
* Description: This script is a Shell script that runs Python code.
* Environment variable `$PYCODE` contains the Python code.
* The Python code prints "Best School: {88+10}".
* File: [1-run_inline](./1-run_inline)

## Task 2: Hello, print
* Description: This Python script prints "Programming is like building a multilingual puzzle" followed by a new line.
* File: [2-print.py](./2-print.py)

## Task 3: Print integer
* Description: This Python script prints the integer stored in the variable `number`, followed by "Battery street", and a new line.
* The script uses f-strings and must be 3 lines long.
* File: [3-print_number.py](./3-print_number.py)

## Task 4: Print float
* Description: This Python script prints the float stored in the variable `number` with a precision of 2 digits.
* The script uses f-strings and must be 3 lines long.
* File: [4-print_float.py](./4-print_float.py)

## Task 5: Print string
* Description: This Python script prints the value of the variable `str` three times on the same line, followed by a new line, and then the first 9 characters of `str` on the next line.
* The script does not use any loops or conditional statements and must be maximum 5 lines long.
* File: [5-print_string.py](./5-print_string.py)

## Task 6: Play with strings
* Description: This Python script prints "Welcome to Holberton School!".
* The script uses the variables `str1` and `str2` in the new line of code and must be exactly 5 lines long.
* File: [6-concat.py](./6-concat.py)

## Task 7: Copy - Cut - Paste
* Description: This Python script copies the first 3 letters of the variable `word` into `word_first_3`, cuts the last 2 letters of `word` and stores them in `word_last_2`, and copies the value of `word` without the first and last letters into `middle_word`.
* The script must not use any loops or conditional statements and must be exactly 8 lines long.
* File: [7-edges.py](./7-edges.py)

## Task 8: Create a new sentence
* Description: This Python script prints "object-oriented programming with Python" followed by a new line.
* The script must be exactly 5 lines long and not use any loops or conditional statements.
* File: [8-concat_edges.py](./8-concat_edges.py)

## Task 9: Easter Egg
* Description: This Python script prints "The Zen of Python" by Tim Peters, followed by a new line.
* File: [9-easter_egg.py](./9-easter_egg.py)

## Task 10: Linked list cycle
* Description: This C function checks if a singly linked list has a cycle in it.
* Prototype: `int check_cycle(listint_t *list);`
* Return: 0 if there is no cycle, 1 if there is a cycle.
* The implementation must not use any functions other than those specified in the provided header file `lists.h`.
* File: [10-check_cycle.c](./10-check_cycle.c)

## Task 11: Hello, write
* Description: This Python script prints "and that piece of art is useful - Dora Korpar, 2015-10-19" to stderr and exits with the status code 1.
* The script uses the `write` function from the `sys` module and does not use `print`.
* File: [100-write.py](./100-write.py)

## Task 12: Compile
* Description: This Shell script compiles a Python script file specified by the environment variable `$PYFILE`.
* The output filename is `$PYFILEc`, where `.pyc` is added to the original filename.
* File: [101-compile](./101-compile)

## Task 13: ByteCode -> Python #1
* Description: This Python function `magic_calculation(a, b)` does exactly the same as the given Python bytecode.
* File: [102-magic_calculation.py](./102-magic_calculation.py)

## Conclusion
This directory contains a diverse set of Python and C scripts that demonstrate different programming concepts and problem-solving skills. Each script serves as a valuable learning resource for individuals seeking to enhance their knowledge and skills in high-level programming languages. Feel free to explore the scripts, engage with the challenges, and expand your understanding of Python and C programming concepts. Enjoy your learning experience and happy coding!
