"""
Program: Lab1.2
Author: Ifa Namee
Date: 9/15/2023
purpose: This program is calculate the area of Rectangle.
"""
# ask user to enter pennies and change to dollar and print result.
pennies = int(input('Enter the number of pennies in the jar:'))
if pennies >= 101:
    print('You have more than a dollar.')
elif pennies <= 99:
    print('You have less than a dollar')
elif pennies == 100:
    print('You have exactly a dollar.')
if pennies <= 99:
    print('You have', pennies, 'cent to be exact.\nThat\'s all folks!')
elif pennies >= 101:
    print('You have $', pennies / 100, 'cent to be exact.\nThat\'s all folks!')
