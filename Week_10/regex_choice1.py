"""
Program: Lab 7
Author: Ifa Namee
Date: 11/05/2023
purpose: This program is hide full number on display last four numbers.
"""

import re

# Prompt and ask the user to enter a number
num = input('Enter your phone number: ex. xxx-xxx-xxxx')

# Define a specific regex pattern with capturing groups
match = re.compile(r'(\d{3}-\d{3}-\d{4})')

# Search for a match in the input
matches = match.search(num)

# Print the result
if matches:
    full_number = matches.group()
    hidden_number = '###-###-' + full_number[-4:]
    print(f'Here is your last four phone number: {hidden_number}')
else:
    print('There is no matching number in the data.')

employee_name = 'N/A'

def get_name():
    global employee_name
    name = input('Enter employee name:')
    employee_name = name

get_name()
print(f'Employee name: {employee_name}')

for i in range(11):
    if i == 6:
        continue
    else:
       print(i, end=' ')

def swap(input_list):
    if len(input_list) < 2:
        return input_list  # Nothing to swap if the list has 0 or 1 elements.

    input_list[0], input_list[-1] = input_list[-1], input_list[0]
    return input_list

# Sample input
my_list = ['all', 'good', 'things', 'must', 'end', 'here']

# Call the swap function with the sample input
result = swap(my_list)
print(result)
