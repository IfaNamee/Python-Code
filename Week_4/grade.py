"""
Program: Lab1.2
Author: Ifa Namee
Date: 9/15/2023
purpose: This program is calculate grade based on score.
"""
# prompt scores and ask user to enter score.
score = input('Enter quiz score – whole number 0-100: ')
# False statement that ask user to reenter.
if score.isnumeric() is False:
    score = int(input('Try the program again; it only takes whole numbers: '))
else:
    score = int(score)
# Statement that give decision based on grade and print result.
if score >= 90:
    print('Grade: A')
elif score >= 80:
    print('Grade: B')
elif score >= 70:
    print('Grade: C')
elif score >= 60:
    print('Grade: D')
else:
    print('Not a passing grade. '
          '\nMaybe try again in future!')
