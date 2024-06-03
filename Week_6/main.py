"""
Program: Lab2.2
Author: Ifa Namee
Date: 10/03/2023
Purpose: This program calculates the average yearly rainfall.
"""

def main():
    rain_fall = inputs()
    total, avg_year, yearly_data = processing(rain_fall)
    outputs(total, avg_year, yearly_data)

def inputs():
    rain_fall = input("How many years are in the rainfall sample? ")
    if rain_fall.isnumeric() is False:
        rain_fall = int(input("How many years are in rainfall sample? "))
    else:
        rain_fall = int(rain_fall)
        if rain_fall < 0:
            rain_fall = int(input("How many years are in rainfall sample? "))
    return rain_fall

def processing(rain_fall):
    total = 0
    yearly_data = []
    for i in range(rain_fall):
        print(f"Rainfall info for year #{i + 1}:")
        subtotal = 0
        for j in range(1, 13):
            month = float(input(f"        Enter rain for month {j}: "))
            if month >= 0:
                subtotal += month
        year_total = subtotal
        year_avg = subtotal / 12
        yearly_data.append((year_total, year_avg))
        total += subtotal
    avg_year = total / (rain_fall * 12)
    return total, avg_year, yearly_data

def outputs(total, avg_year, yearly_data):
    print("\nYearly Rainfall Data:")
    for i, (year_total, year_avg) in enumerate(yearly_data, start=1):
        print(f"Year #{i}: Total rainfall: {year_total} inches, Average yearly rainfall: {year_avg} inches")
    print(f"\nTotal rainfall for all years: {total} inches")
    print(f"Average yearly rainfall: {avg_year} inches")

main()
