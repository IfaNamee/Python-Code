"""
Program: Lab1.2
Author: Ifa Namee
Date: 9/15/2023
purpose: This program count coins type and print result in total amount in dollar.
"""
# input statement for coins
quarters = int(input("How many quarters do you have? Enter whole number: "))
dimes = int(input("How many dimes do you have? Enter whole number: "))
nickles = int(input("How many nickles do you have? Enter whole number: "))
pennies = int(input("How many pennies do you have? Enter whole number: "))

# variables and formula that change coins to dollar.
Value_quarters = quarters * 25 / 100
value_dimes = dimes * 10 / 100
value_nickles = nickles * 5 / 100
value_pennies = pennies * 1 / 100
total_number = quarters + dimes + nickles + pennies
total_value = Value_quarters + value_dimes + value_nickles + value_pennies

# Prompt that coins under 10 dollars or above.
if total_value <= 9.99:
    print("\nKeep saving! You have less than $ 10,")
    print( total_value, "$ is\'s money you saved.")
elif total_value >= 10.01:
    print("\nKeep saving! You have more than $ 10,")
    print(total_value, "$ is\'s money you saved.")

# print the result using table form.
print("\nTotal value of you coins")
print(f"{'Coin Type': <14}{'Number':<16}{'Value': <14}")
print(f"{'Quarters': <16}{quarters: <12}{'$': <4}{Value_quarters: >2.2f}")
print(f"{'Dimes': <16}{dimes: <12}{'$': <4}{value_dimes: >2.2f}")
print(f"{'Nickles': <16}{nickles: <12}{'$': <4}{value_nickles: >2.2f}")
print(f"{'Pennies': <16}{pennies: <12}{'$': <4}{value_pennies: >2.2f}")
print(f"{'Total': <16}{total_number: <12}{'$': <4}{total_value : >2.2f}")
