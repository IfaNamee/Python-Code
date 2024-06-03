"""
Program: Lab2.2
Author: Ifa Namee
Date: 10/15/2023
purpose: This program generate random numbers and print sorted of numbers and total of number by using
         Mipo method main, inputs, processing, outputs and rerun.
"""
import random


def main():  # call for some input data
    length = (inputs())
    processing(length)
    outputs(length)
    rerun()


def inputs():  # add data validation as necessary to prevent bad inputs
    print("Welcome to our random number game. ")
    print("How many integers should the computer pick for your list? ")
    length = input("Please enter a whole number: ")
    if length.isnumeric() is False:
        length = int(input("Please enter a whole number 1 or higher: "))
    else:
        length = int(length)
    return length  # send result back


def processing(length):  # do any necessary calculations of total
    random_numbers = [random.randint(0, 9) for i in range(length)]
    print(random_numbers)
    print(f"\nHere is your list of {length} integers - randomly selected & sorted: ")
    numbers = sorted(random_numbers)
    print(numbers)
    print(f"Here is your list - printed with shortcut method: ")
    print(*numbers, sep=", ")
    print(f"Here is your list - printed vip a loop, with total: ")
    total = sum(numbers)
    print(*numbers, sep=" + ", end=f" = {total}")
    minim = min(numbers)
    maxim = max(numbers)
    print(f"\nYour list minimum was {minim} and maximum was {maxim} this time.")


def outputs(length):  # print out result
    print()


def rerun():  # statement that ask user to generate again.
    again = input("would you like pick again? Enter y or n")
    if again == 'n':
        print(end='')
    elif again == 'y':
        return main()  # send result back to main()


main()
