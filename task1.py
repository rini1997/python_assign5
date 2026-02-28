"""
Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
"""
from warnings import catch_warnings

dic1 = {
    'arjun':'589',
    'javed':'480',
    'simran':'582',
    'rani':'307'
}

input_name = input("Enter the student's name: ")
input_name1 = input_name.lower()
try:
    if input_name1 in dic1:
        print(f"The marks of {input_name} is {dic1[input_name1]}")
    else:
        print(f"Student {input_name} not found")
except:
    print("Invalid input")