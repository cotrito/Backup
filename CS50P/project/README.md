# Project Waitress annotate order helper

## Introduction
My name its Vicente Cotroneo, I'm a 34 year old industrial engineer from Chile,
and this is my final project made for the CS50P course 2022 version.
This program was designed to help the waitress with taking an order for food service.

### About CS50P course
It's a Harvard’s Introduction course to programing with Python

## Description
The program has a main function that  lets you choose which function you like to execute.

1.Show menu
2.New table order
3.Close table
4.Show payments
5.Exit

### Show menu
This function will show in a grid every item in the menu listed in a file named menu.csv, this considers an id for the item , its name and price.
its look like this:

### New table order
the first thing this function will do its to request a table number, and it will search for the table and if it doesn't exist it will pop up again using the function chose_table that loop while input is invalid using the function table_exist, if the table exist the function continues showing every item in the menu and asking for the item that is been ordered by that particular table, if the item exist it will ask for the quantity of that particular item after that considering that every input is correct the order will be written in the file tables.json inside the orders of that table. This function can also be used to add any items after the initial order.

### Close table
When the moment of paying the order comes, there is a function Close table that calculate the total amount ordered by the table delivered as an input  and expect an input if the account was paid or not, if the account is paid all the orders are erased from the file table.json and the total with the current time is kept in a file named payments.csv, also if the total amount of the table it's cero the payment is declined and showing that the total amount does not need to be paid.

### Show payments
To see all the payments realized it's possible to access by the fourth option that shows every payment in the file payments.csv, this option shows the total amount paid by table and the date and time of it.
its look like this:

### Exit
This simple exit the program by the command sys.exit

### Additional considerations
In its current estate the program comes with only three tables but it's possible to add as much as possible, also there is a quantity maximum allowed of 10 for every item order , but you can make as many order of the same items as you want, and the last thing to consider in some steps it's possible to exit the menu by input cero.

## Files directory
The program contains multiple files :

### project.py
The main file is project.py where all the functions are listed.

### tes_proyect.pyt
It's a  file that tests some of its functions.

### menu.csv
A file containing all the menu items with its ids and prices, it's possible to change ids, names and prices and also adding more items but always respecting the structure.

### Tables.json
file containing the details of each table with its orders , this is written in json and has this structure: first a dictionary containing all the tables , this open to the table name and inside the table number and all the orders, this is the structure for three tables:

{"Tables": {"table1": {"Table_number": 1, "orders": []}, "table2": {"Table_number": 2, "orders": []}, "table3": {"Table_number": 3, "orders": []}}}

### payments.csv
This file has the table number , the total amount paid and also the date and time of the order. In the end I decided only to include the total amount and not the item detail here.

### requirements.txt
This list all the additional libraries needed to install for the program to run

#### Video Demo:  https://youtu.be/xepXfhVdbMk
