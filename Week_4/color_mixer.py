"""
Program: Lab1.2
Author: Ifa Namee
Date: 9/15/2023
purpose: This program mix a color base on user choose.
"""
# prompt the program and print out.
print('What happens when you mix 2 different primary color? ')

# ask user to enter first color and print result
first_color = input("Enter a primary color - red, yellow or blue: ")
while first_color not in {'yellow', 'red', 'blue'}:
    first_color = input("Please enter the word red, yellow or blue only: ")

# ask user to enter second color and print result.
second_color = input("Enter a 2nd primary color, not the same as first: ")
while second_color == first_color or second_color not in {'yellow', 'red', 'blue'}:
    second_color = input("select different primary color for the color 2: ")

# compare the color and make decision and print out result.
if (first_color == 'yellow' and second_color == 'blue'
) or (first_color == 'blue' and second_color == 'yellow'):
    print("\nNice! Yellow and Blue make Green!")

# compare the color and make decision and print out result.
elif (first_color == 'yellow' and second_color == 'red'
) or (first_color == 'red' and second_color == 'yellow'):
    print("\nNice! Yellow and Red make orange!")

# compare the color and make decision and print out result.
elif (first_color == 'red' and second_color == 'blue'
) or (first_color == 'blue' and second_color == 'red'):
    print("\nNice! Red and Blue make purple!")

print("Thank for using the program.")
