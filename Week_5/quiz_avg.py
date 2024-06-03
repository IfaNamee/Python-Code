"""
Program: Lab1.2
Author: Ifa Namee
Date: 9/22/2023
purpose: This program calculate the quizzer .
"""
# prompt enter and print out
student = int(input("How many students are in the the group?"))
quizzes = int(input("How many quizzes do they take? "))
# for statement range the number based on entered.
for j in range(0, student):
    print(f"Quiz info for student # {j+1} ")
    subtotal = 0
    for i in range(0, quizzes):
        quiz = int(input(f"        Enter score for quiz # {i+1}: "))
        subtotal += quiz                # calculates total point
        average = subtotal / quizzes    # calculate total average
    # print out total point and average
    print(f"Total quiz points for student # {j +1} = {subtotal}")
    print(f"Student # Quiz Average = {average:.2f}")
print("Thanks for using the program")