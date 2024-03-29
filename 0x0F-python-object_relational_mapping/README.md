# Python - Object-Relational Mapping

This project focuses on connecting Python with databases using Object-Relational Mapping (ORM). It utilizes modules such as MySQLdb and SQLAlchemy to interact with a MySQL database, execute SQL queries, and perform CRUD operations using Python code instead of writing raw SQL queries.

## Table of contents
1. [Learning Objectives](#learning-objectives)
2. [Requirements](#reqirements)
3. [Installation](#installation)
4. [MySQLdb](#mysqldb)
5. [SQLAlchemy](#sqlalchemy)
6. [Project Structure](#Project-Structure)
7. [Usage](#Usage)
8. [Tasks](#Tasks)
9. [Examples](#Examples)
10. [Conclusion](#Conclusion)

## Learning Objectives

By completing this project, i have  gain knowledge and understanding of the following:

- Python programming and its advantages
- Connecting to a MySQL database from a Python script
- Executing SELECT queries in Python to retrieve data from a MySQL table
- Executing INSERT queries in Python to add data to a MySQL table
- Understanding and utilizing Object-Relational Mapping (ORM)
- Mapping a Python Class to a MySQL table using SQLAlchemy

## Requirements

- Python version: 3.8.5
- MySQLdb version: 2.0.x
- SQLAlchemy version: 1.4.x

### Installation

To install the required modules, follow the instructions below:

#### MySQLdb

1. Make sure MySQL is installed. If not, you can refer to the [MySQL 8.0 installation guide for Ubuntu 20.04](https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/linux-installation.html).

2. Install the necessary dependencies:

   ```bash
   $ sudo apt-get install python3-dev
   $ sudo apt-get install libmysqlclient-dev
   $ sudo apt-get install zlib1g-dev

1. Install MySQLdb:
```
$ sudo pip3 install mysqlclient
```
2. Verify the installation:
```
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info
(2, 0, 3, 'final', 0)
```
#### SQLAlchemy
1. Install SQLAlchemy:
```
$ sudo pip3 install SQLAlchemy
```
2. Verify the installation:
```
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.4.22'
```
## Project Structure
```
The project directory has the following structure:
0x0F-python-object_relational_mapping/
├── 0-select_states.py
├── 1-filter_states.py
├── 2-my_filter_states.py
├── 3-my_safe_filter_states.py
├── 4-cities_by_state.py
├── 5-filter_cities.py
├── model_state.py
├── 7-model_state_fetch_all.py
├── 8-model_state_fetch_first.py
├── 9-model_state_filter_a.py
├── 10-model_state_my_get.py
├── 11-model_state_insert.py
├── 12-model_state_update_id_2.py
├── 13-model_state_delete_a.py
├── 14-model_city_fetch_by_state.py, model_city.py
├── 100-relationship_states_cities.py, relationship_state.py, relationship_city.py
├── 101-relationship_states_cities_list.py
├── 102-relationship_cities_states_list.py
└── README.md
```
* Each Python script corresponds to a specific task and accepts command-line arguments.
* `README.md` file provides an overview of the project, installation instructions, and project structure.
## Usage
To run the scripts, use the following format:
```
$ ./script_name.py mysql_username mysql_password database_name [additional_arguments]
```
Replace `script_name.py` with the name of the desired script and provide the necessary command-line arguments.
## Tasks
The project consists of the following tasks:
1. [0-select_states.py](./0-select_states.py): Lists all states from the database `hbtn_0e_0_usa` using MySQLdb.
2. [1-filter_states.py](./1-filter_states.py): Lists states starting with the letter "N" from the database `hbtn_0e_0_usa` using MySQLdb.
3. [2-my_filter_states.py](./2-my_filter_states.py): Displays states from the database `hbtn_0e_0_usa` that match a given input using MySQLdb.
4. [3-my_safe_filter_states.py](./3-my_safe_filter_states.py): Displays states from the database `hbtn_0e_0_usa` that match a given input using MySQLdb, but with safe from SQL injection.
5. [4-cities_by_state.p](./4-cities_by_state.py): Lists all cities from the database `hbtn_0e_4_usa` using SQLAlchemy.
6. [5-filter_cities.py](./5-filter_cities.py): takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa.
7. [model_state.py](./model_state.py): python file that contains the class definition of a State and an instance Base = declarative_base().
8. [7-model_state_fetch_all.py](./7-model_state_fetch_all.py): lists all State objects from the database hbtn_0e_6_usa.
9. [8-model_state_fetch_first.py](./8-model_state_fetch_first.py): prints the first State object from the database hbtn_0e_6_usa.
10. [9-model_state_filter_a.py](./9-model_state_filter_a.py): lists all State objects that contain the letter a from the database hbtn_0e_6_usa.
11. [10-model_state_my_get.py](./10-model_state_my_get.py): prints the State object with the name passed as argument from the database hbtn_0e_6_usa.
12. [11-model_state_insert.py](./11-model_state_insert.py): adds the State object “Louisiana” to the database hbtn_0e_6_usa.
13. [12-model_state_update_id_2.py](./12-model_state_update_id_2.py): changes the name of a State object from the database hbtn_0e_6_usa.
14. [13-model_state_delete_a.py](./13-model_state_delete_a.py): deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa.
15. [14-model_city_fetch_by_state.py](./14-model_city_fetch_by_state.py): prints all City objects from the database hbtn_0e_14_usa.
16. [100-relationship_states_cities.py](./100-relationship_states_cities.py): creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa.
17. [101-relationship_states_cities_list.py](./101-relationship_states_cities_list.py): that lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa.
18. [102-relationship_cities_states_list.py](./102-relationship_cities_states_list.py): lists all City objects from the database hbtn_0e_101_usa.
## Examples

Here are a few examples demonstrating the usage of the scripts:

1. To list all states:
   ```bash
   $ ./0-select_states.py mysql_username mysql_password database_name

2. To list states starting with the letter "N":
```
$ ./2-my_filter_states.py mysql_username mysql_password database_name Arizona
```
3. To display states that match a given input with safe from SQL injection (e.g., "Arizona"):
```
$ ./3-my_safe_filter_states.py mysql_username mysql_password database_name Arizona
```
4. To list all cities:
```
$ ./4-cities_by_state.py mysql_username mysql_password database_name
```
## Conclusion
This project provides a hands-on experience in working with Python and databases using Object-Relational Mapping (ORM). By completing the tasks and understanding the code, you will enhance your knowledge of connecting Python with databases, executing SQL queries, and leveraging the power of ORM to simplify database interactions.
