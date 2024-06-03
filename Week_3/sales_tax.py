"""
Program: Lab1.2
Author: Ifa Namee
Date: 9/7/2023
purpose: program that calculate tax.
"""
# ask user to enter amount
total = float(input('What is the total price of your purchase orders? '))

# variable and formula
state = total * 0.05
country = total * 0.025
total_cost = total + state + country

# print the result grand amount
print("\t")
print('Custom Delivery sales receipt')
print('PO Amount:'f"{'$':>12}{total:>12.2f}")
print('State Tax:'f"{'$':>12}{state:>12.2f}")
print('Country Tax:'f"{'$':>10}{country:>12.2f}")
print('Total Cost:'f"{'$':>11}{total_cost:>12.2f}")


