"""
Program: Lab1.2
Author: Ifa Namee
Date: 9/22/2023
purpose: This program calculate total amount based on user enters.
"""
# prompt enters using if statement.
textbooks = input("How many textbooks do you have to buy? ")
if textbooks.isnumeric() is False:
    textbooks = int(input("How many textbooks do you have to buy? "))
subtotal = 0
# for statement using in range statement and print result
for i in range(1, textbooks + 1):
    price = float(input(f"\nEnter price of textbook {i}: "))
    subtotal += price
    print(f'Running subtotal = ${subtotal:.2f}')
# print result total amount.
print(f"\nGrand total = {subtotal:.2f}.")

"""
textbooks = int(input("How many textbooks do you have to buy? "))
while not int(textbooks):
    textbooks = int(input("How many textbooks do you have to buy? "))
if textbooks <= 0:
    textbooks = int(input("Enter a whole, positive, no space: "))
subtotal = 0
i = 1
while i <= textbooks:
    price = float(input(f"\nEnter price of textbook {i}: $"))
    subtotal += price
    i += 1
print(f"\nGrand total = {subtotal:.2f}.")
"""



