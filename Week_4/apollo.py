"""
Program: Lab1.2
Author: Ifa Namee
Date: 9/15/2023
purpose: This program is ask user to enter a year apollo 11 land on moon.
"""
year = int(input('What year did Apollo 11 land on the moon? '))
if year == 1969:
    print(f'Correct! {year} is right!')
elif year == 1968:
    print("Wrong, it\'s 1969. But you were close!.")
elif year == 1970:
    print("Wrong, it\'s 1969. But you were close!.")
else:
    print(f"You are wrong!. it's 1969")

    # or below programming is run correly.
""""
# print the question and ask user to enter.
year = int(input('What year did Apollo 11 land on the moon? '))
# if and elif statement to print the answer.
if year == 1969:
    print(f'Correct! {year} is right!')
else:
    score = int(year)
    if score == 1968:
        print(f"Wrong, it\'s 1969. But you were close!.")
    elif score == 1970:
        print("Wrong, it\'s 1969. But you were close!.")
    elif score <= 1967:
        print("Wrong, You were to low. it\'s 1969.")
    elif score >= 1971:
        print('Wrong, You were to high. it\'s 1969.')
"""