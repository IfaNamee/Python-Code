"""
Program: Lab2.2
Author: Ifa Namee
Date: 10/03/2023
purpose: This program counts number  by using
         Mipo method main, inputs, processing, outputs and counting.
"""


def main():  # call for some input data
    one_digit, large_num = (inputs())
    subtotal = processing(one_digit, large_num)
    outputs(subtotal)
    counting()


def inputs():  # add data validation as necessary to prevent bad inputs and print
    one_digit = input("Please enter a small number, 0 or higher: ")
    if one_digit.isnumeric() is False:
        one_digit = int(input("Please enter a whole number only: "))
    else:
        one_digit = int(one_digit)

    large_num = input("Now, enter a larger number that you want to count up too: ")
    if large_num.isnumeric() is False:
        large_num = int(input(f"Enter a whole number greater than your start number ({one_digit}):"))
    else:
        large_num = int(large_num)
    if large_num < one_digit:
        large_num = int(input(f"Enter a whole number greater than your start number ({one_digit}):"))

    return one_digit, large_num  # send result back


def processing(one_digit, large_num):  # do any necessary print statement
    total = 0
    for i in range(one_digit, large_num + 1):
        print(i)
        total += i
    return total  # send result back


def outputs(subtotal):  # print out result
    print(f"The total of all the numbers you counted is: {subtotal}")
    return


def counting():  # statement that ask user to calculate again.
    again = input("Continue? Enter y or n")
    if again == 'n':
        print("Thanks for using the program! ")
        print(end='')
    elif again == 'y':
        return main()  # send result back


main()
