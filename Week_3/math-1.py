"""
Program: Lab1.2
Author: Ifa Namee
Date: 9/7/2023
purpose: This program do math functions.
"""
# math import that run math equations
import math

print('Here are some fun facts...')

# Cut off 7.89 to 7
cut_off = 7.89
cut_off = int(cut_off)
print('7.89 with decimal cut off = ', cut_off)
# round 54.345395 to 54.345
number = 54.345395
print('54.345395 to rounded to 3 decimal places = 'f"{number:.3f}")
# calculate the square root of 2
square = math.sqrt(2)
print('The square root of 2 = ',square)
# calculate the sin of 7
result = math.sin(7)
print('The sin of 7 =', result)
# display the value of pi
value = math.pi
print('The value of pi =', value)
# display pi rounded to 3 decimal places
print('The valve of pi rounded to decimal place = 'f"{value:.3f}")