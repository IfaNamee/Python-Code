import re

# Ask the user to enter the source text
name_source = input('Enter full name in this format – first middle last: ')

# Define a regex pattern to match full names
regex_pattern = r'\b[a-zA-Z\']+(?:[. -][a-zA-Z]+)*\b'

# Find all matches in the input text
matches = re.findall(regex_pattern, name_source)

if matches:
    for match in matches:
        print(f'Here is the name: {match}')
else:
    print('This doesn\'t look like a name.')
