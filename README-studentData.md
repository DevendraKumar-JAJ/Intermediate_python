### Student Management System  📚

## Overview
This is a simple student management system implemented in Python. It allows users to create student objects, store them in a list, and search for students based on their name or roll number.

## Features
- Create student objects with name and roll number 📝
- Store student objects in a list 📚
- Search for students based on name or roll number 🔍
- Display student information 📄

## Classes and Methods
### - Greet class:
    - __init__: Constructor to initialize name and age
    - greetMe: Method to print a greeting message 👋
### - Student class (inherits from Greet):
    - __init__: Constructor to initialize name and roll number
    - greetMe: Method to print a greeting message with roll number 👋
    - aboutMe: Method to print student information 📄
    - changeData: Method to update student information 📝

## Access Modifiers
- Private members: Not inherited or used by other classes or outside the class 🔒
- Protected members: Inherited by other classes but not used outside the class or inherited class 🔒
- Public members: Default access modifier, can be used anywhere in the program 🌐

## Usage
1. Run the script and enter the number of student records you want to create 📊
2. Enter student name and roll number for each record 📝
3. Choose to search for students based on name or roll number 🔍
4. Enter the search query and view the results 📄

## Example Use Case

Enter number of records you want : 2
Obj 1 Enter Name : John
Roll : 101
Obj 2 Enter Name : Jane
Roll : 102
Do you want to search data [y/n] : y
Based on [1 _ Name | 2 _ Roll ] 1
Enter name to search : John
Name : John, and Roll : 101


### Author - 
  * Devendra Kumar