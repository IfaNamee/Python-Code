"""
Program: Lab2.2
Author: Ifa Namee
Date: 9/22/2023
purpose: This program is print out numbers based on instruction.
"""
# print out numbers 0 to 5
print("These are the numbers from 0 through 5.")
for i in range(0, 6):
    print(i)
# print out numbers 1 t0 20
print("These are the numbers from 1 through 20. ")
for i in range(0,21): # or for i in range(0,21,2):
    print(i)
# print out numbers even 0 and between 0 and 24
print("These are the all of even numbers from 0 through 24. ")
for i in range(0, 25):
    if i % 2 == 0:
        print(i)
# print out numbers odd 37 amd between 37 and 53
print("These are the all of odd numbers from 37 through 53. ")
for i in range(37, 54): # or for i in range(37, 54,2)
    if i % 2 != 0:
        print(i)
# print out numbers two digit end with 0 between 0 and 60
print("This counts 10 though 60 by 10s. ")
for i in range(10, 70): # or for i in range(10, 70,10)
    if i % 10 == 0:
        print(i)
