"""
Program: Lab 7
Author: Ifa Namee
Date: 11/05/2023
purpose: This program is search match in
"""
import re

# Ask the user to enter
name_source = input('Enter Your full name: first middle last: ')

# Regex pattern to match full names
regex_pattern = re.compile(r'\b[a-z A-Z\']+([. -][a-z A-Z\']+)\b')

# Find all matches in the input checks
match = regex_pattern.search(name_source)

if match:
    print(f"Here is the name: ", match.group())
else:
    print('This doesn\'t look like a name.')

