"""
Program: Lab2.2
Author: Ifa Namee
Date: 9/22/2023
purpose: This program counts number.
"""
print("Welcome to our counting program.")
print("It also adds up the digits that you count!.")
one_digit = input("Please enter a small number, 0 or higher: ")
if one_digit.isnumeric() is False:
    one_digit = int(input("Please enter a whole number only: "))
else:
    one_digit = int(one_digit)
large_num = int(input("Now, enter a larger number that you want to count up too: "))
if large_num < one_digit:
    large_num = int(input("Enter a whole number greater than your start number (5):"))
else:
    large_num = int(large_num)
total = 0
for i in range(one_digit, large_num + 1):
    print(i)
    total += i

print("The total of all the numbers you counted is:", total)



