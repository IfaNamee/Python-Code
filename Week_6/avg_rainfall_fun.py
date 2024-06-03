"""
Program: Lab2.2
Author: Ifa Namee
Date: 10/03/2023
purpose: This program calculate average of rainfall in a year by using
         Mipo method main, inputs, processing, outputs and counting.
"""


def main(): # call for some input data
    rain_fall = inputs()
    total, avg_year = processing(rain_fall)
    outputs(total, avg_year)
    counting()


def inputs(): # add data validation as necessary to prevent bad inputs and print
    rain_fall = input("How many year are in rainfall sample? ")
    if rain_fall.isnumeric() is False:
        rain_fall = int(input("How many year are in rainfall sample? "))
    else:
        rain_fall = int(rain_fall)
        if rain_fall < 0:
            rain_fall = int(input("How many year are in rainfall sample? "))
    return rain_fall # send result back


def processing(rain_fall): # do any necessary calculations
    total = 0
    for i in range(rain_fall):
        print(f"Rainfall info for year #{i + 1}:")
        subtotal = 0
        for j in range(1, 13):
            month = input(f"        Enter rain for month {j}")
            if month.isnumeric() is False:
                month = float(input(f"        Enter rain for month {j}"))
            else:
                month = float(month)
            if month >= 0:
                subtotal += month
        year_total = subtotal
        year_avg = subtotal / 12
        print(f"Total rainfall for year # {i + 1}: {year_total} inches")
        print(f"Average yearly rainfall for year # {i + 1}: {year_avg} inches")

        total += subtotal
    avg_year = total / (rain_fall * 12)
    return total, avg_year # send result back


def outputs(total, avg_year): # print out result
    print(f"\nTotal rainfall for all years: {total} inches")
    print(f"Average yearly rainfall: {avg_year} inches")


def counting():  # statement that ask user to use program again.
    again = input("Continue? Enter y or n")
    if again == 'n':
        print("Thanks for using the program! ")
        print(end='')
    elif again == 'y':
        return main() # send result back


main()
