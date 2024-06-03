"""
Program: Lab1.2
Author: Ifa Namee
Date: 9/7/2023
purpose: This program is calculate the area of Rectangle.
"""
# print and ask user to enter the measurement
print("Welcome to rectangle Area calculator!")
unit = str(input('What is your measurement unit. (in., ft., cm., etc)? '))
length = float(input('What is the length of the rectangle in ' + unit + '? '))
width = float(input('What the width of the rectangle in ' + unit + '? '))

# variable formula and print result
area = float(length) * float(width)
print('Your rectangle is', area, 'square ' + unit)
