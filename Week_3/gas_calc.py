"""
Program: Lab1.2
Author: Ifa Namee
Date: 9/7/2023
purpose: program that calculate gas you used.
"""
# print information and ask user to enter information
mile = int(input('How many miles did you drive?'))
gallons = int(input('How many gallons of gas did you use?'))
per_gallons = float(input('How much was your gas per gallon? '))

# variable and math formula
mpg = mile / gallons
trip_cost = gallons * per_gallons

# print the result of information
print("\t")
print('Here\'s some fun facts about your trip!')
print('MPG'f"{mpg:>21.2f}")
print('Trip Cost'f"{'$':>10}{trip_cost:>5.2f}")

# using formatting method and print result
"""
print('Here\'s some fun facts about your trip!')
print('{:<15} {:>5.2f}'.format('MPG', mile / gallons))
print('{:<15}${:>5.2f}'.format('Trip Cost', gallons * per_gallons))

"""