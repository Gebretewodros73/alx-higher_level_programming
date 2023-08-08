# Python Input/Output Practice

This repository contains a set of Python scripts that demonstrate various input/output operations. Each script corresponds to a specific task and showcases different aspects of file handling, JSON serialization, and object representation.

## Tasks

### Task 0: Read File

- File: [0-read_file.py](./0-read_file.py)
- Prototype: `def read_file(filename="")`
- Description: This function reads a text file (UTF8) and prints its content to the standard output (stdout). It uses the `with` statement and doesn't require file permission or file existence exception handling.

### Task 1: Write to a File

- File: [1-write_file.py](./1-write_file.py)
- Prototype: `def write_file(filename="", text="")`
- Description: This function writes a string to a text file (UTF8) and returns the number of characters written. It uses the `with` statement, creates the file if it doesn't exist, and overwrites its content if it already exists.

### Task 2: Append to a File

- File: [2-append_write.py](./2-append_write.py)
- Prototype: `def append_write(filename="", text="")`
- Description: This function appends a string at the end of a text file (UTF8) and returns the number of characters added. If the file doesn't exist, it is created. It uses the `with` statement.

### Task 3: To JSON String

- File: [3-to_json_string.py](./3-to_json_string.py)
- Prototype: `def to_json_string(my_obj)`
- Description: This function returns the JSON representation of an object (string). It doesn't handle exceptions if the object can't be serialized.

### Task 4: From JSON String to Object

- File: [4-from_json_string.p](./4-from_json_string.py)
- Prototype: `def from_json_string(my_str)`
- Description: This function returns an object (Python data structure) represented by a JSON string. It doesn't handle exceptions if the JSON string doesn't represent an object.

### Task 5: Save Object to a File

- File: [5-save_to_json_file.py](./5-save_to_json_file.py)
- Prototype: `def save_to_json_file(my_obj, filename)`
- Description: This function writes an object to a text file using a JSON representation. It uses the `with` statement and doesn't handle file permission exceptions.

### Task 6: Create Object from a JSON File

- File: [6-load_from_json_file.py](./6-load_from_json_file.py)
- Prototype: `def load_from_json_file(filename)`
- Description: This function creates an object from a JSON file. It uses the `with` statement and assumes the JSON string represents an object.

### Task 7: Load, Add, Save

- File: [7-add_item.py](./7-add_item.py)
- Description: This script adds all command-line arguments to a Python list and saves them to a file in JSON representation. The file is named `add_item.json`.

### Task 8: Class to JSON

- File: [8-class_to_json.py](./8-class_to_json.py)
- Description: This function demonstrates how to create a dictionary representation of a class instance for JSON serialization. It works with attributes like list, dictionary, string, integer, and boolean.

### Task 9: Student to JSON

- File: [9-student.py](./9-student.py)
- Description: This class defines a student by first name, last name, and age. It provides a method to retrieve a dictionary representation of a student instance.

### Task 10: Student to JSON with Filter

- File: [10-student.py](./10-student.py)
- Description: This class extends the previous student class by allowing filtering attributes for JSON representation.

### Task 11: Student to Disk and Reload

- File: [11-student.py](./11-student.py)
- Description: This class further extends the student class by adding a method to reload attributes from a JSON dictionary representation.

### Task 12: Pascal's Triangle

- File: [12-pascal_triangle.py](./12-pascal_triangle.py)
- Description: This function generates Pascal's triangle up to the specified number of rows and returns it as a list of lists of integers.

## Usage

Each script can be executed individually to see the demonstration of the corresponding task. For example:

```bash
./0-read_file.py
./1-write_file.py
# ... and so on
```
