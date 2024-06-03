"""
Program: Lab 7
Author: Ifa Namee
Date: 11/05/2023
purpose: This program is only accept number that have minus (-) in first position
         and decimal (.) at the end.
"""
import re

# prompt and ask user to enter
num = input('Enter a number start with minus '
            '(-) and end with decimal (.) number: ')

# Define specific compile
match = re.compile(r'-\d+\.\d+')

# Search match in input enter
matches = match.search(num)

# Print the result
if matches:
    print(f'Here is your number: {matches}')
else:
    print('There is no match number in data.')
