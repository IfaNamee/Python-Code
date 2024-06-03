# this program is change lowercase to uppercase.
lowercase = input('Enter lower case letter: ')
uppercase = ''

for char in lowercase:
    ifa = ord(char)

    if 97 <= ifa <= 122:  # ifa >= 97 and ifa <= 122:
        ifa = ifa - 32
        new_char = chr(ifa)
        uppercase = uppercase + new_char

    else:
        uppercase = uppercase + char
print('The string in uppercase is', uppercase)

# This program is do both lowercase to uppercase and uppercase to lowercase.

input_string = input('Enter a string: ')
output_string = ''

for char in input_string:
    if 'a' <= char <= 'z':
        # Convert lowercase to uppercase
        output_string += char.upper()
    elif 'A' <= char <= 'Z':
        # Convert uppercase to lowercase
        output_string += char.lower()
    else:
        output_string += char

print('The converted string is:', output_string)


