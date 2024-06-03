"""
Program: Lab1.2
Author: Ifa Namee
Date: 9/7/2023
purpose: program that calculate gas you used.
"""
# ask information to enter about coffee
cups_coffee_sold = int(input('How many cups of coffee sold? '))
price_coffee = float(input('price of coffee? '))
total_coffee = cups_coffee_sold * price_coffee

# ask information to enter about tea
cups_tea_sold = int(input('How many cups of tea sold? '))
price_tea = float(input('price of tea? '))
total_tea = cups_tea_sold * price_tea

# ask information to enter about cappuccino
cups_cappuccino_sold = int(input('How many cups of cappuccino sold? '))
price_cappuccino = float(input('price of cappuccino? '))
total_cappuccino = cups_cappuccino_sold * price_cappuccino

# variable and math calculation about total information
total_cups = cups_coffee_sold + cups_tea_sold + cups_cappuccino_sold
total_price = total_coffee + total_tea + total_cappuccino

# result about total amount
print("\t")
print('Drink sales for the reporting period.')
print(f"{'Drink Type': <14}{'Cup sold':<15}{'price':<15}{'Total':>2}")

print('Coffee'f"{cups_coffee_sold:>22}{'$':>11} {price_coffee:>4.2f}{'$':>11}"
      f" {total_coffee:>4.2f}")

print('Tea'f"{cups_tea_sold:>25}{'$':>11} {price_tea:>04.2f}{'$':>11}"
      f" {total_tea:>4.2f}")

print('Cappuccino'f"{cups_cappuccino_sold:>18}{'$':>11}"
      f" {price_cappuccino:>4.2f}{'$':>11} {total_cappuccino:<4.2f}")

print('Total'f"{total_cups:>23}{'$':>27} {total_price:<4.2f}")
