"""
Program: Lab2.2
Author: Ifa Namee
Date: 10/03/2023
purpose: This program calculates the volume of the box.
"""


def main(): # call for some input data
    length, width, height = (inputs())
    calculate = processing(length, width, height)
    outputs(length, width, height, calculate)
    counting()


def inputs(): # add data validation as necessary to prevent bad inputs
    print("This program calculates the volume of the box. ")
    length = input("what\'s the length of the box? ")
    if length.isnumeric() is False:
        length = int(input("Please enter a whole number greater than 0: "))
    else:
        length = int(length)
    width = input("what\'s the width? ")
    if width.isnumeric() is False:
        width = int(input("Please enter a whole number: "))
    else:
        width = int(width)
    height = input("what\'s the height? ")
    if height.isnumeric() is False:
        height = int(input("Please enter a whole number: "))
    else:
        height = int(height)
    return length, width, height # send result back


def processing(length, width, height): # do any necessary calculations
    cube = length * width * height
    return cube # send result back


def outputs(length, width, height, calculate): # print out result
    print(f"The volume of the object is: {calculate} cubic units.")
    print("Thanks for using the program. ")  # last line printed


def counting(): # statement that ask user to calculate again.
    again = input("Continue? Enter y or n")
    if again == 'n':
        print(end='')
    elif again == 'y':
        return main() # send result back to main()


main()

# Or using while and while not.
"""
def main():
    while True:
        length, width, height = inputs()
        calculate = volume(length, width, height)
        outputs(length, width, height, calculate)
        again = counting()
        if again.lower() != 'y':
            break
    print("Thanks for using the program.")


def inputs():
    print("This program calculates the volume of the box.")
    length = input("What's the length of the box? ")
    while not length.isnumeric():
        length = input("Please enter a whole number for the length: ")
    length = int(length)

    width = input("What's the width? ")
    while not width.isnumeric():
        width = input("Please enter a whole number for the width: ")
    width = int(width)

    height = input("What's the height? ")
    while not height.isnumeric():
        height = input("Please enter a whole number for the height: ")
    height = int(height)

    return length, width, height


def volume(length, width, height):
    cube = length * width * height
    return cube


def outputs(length, width, height, calculate):
    print(f"The volume of the object is: {calculate} cubic units.")


def counting():
    again = input("Continue? Enter 'y' to calculate again or 'n' to exit: ")
    return again


main()

"""