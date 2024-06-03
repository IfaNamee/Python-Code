"""
Program: Lab2.2
Author: Ifa Namee
Date: 9/22/2023
purpose: This program calculate average of rainfall in a year.
"""
# prompt and ask user years to enter.
rain_fall = int(input("How many year are in rainfall sample? "))
# for statement to range a year based and print out
for i in range(0, rain_fall):
    print(f"Rainfall info for year # {i+1}:")
    subtotal = 0
    # for statement to enter rainfall in a month
    for j in range(1, 13):
        month = int(input(f"        Enter rain for month {j}"))
        subtotal += month         # Calculate total rainfall in a year
        Avg_year = subtotal / 12  # calculate total average in a year
    # print out result
    print(f"Total rain in inches for year # {i+1} = {subtotal:.1f}")
    print(f"Year #{i+1} Monthly Avg Rainfall = {subtotal / 12:.2f}")

