"""
Program: Lab 6
Author: Ifa Namee
Date: 10/29/2023
purpose: This program collect feedback and prints out separate by index on new line.
"""


def main():
    feedback_list = inputs()  # Store the feedback list returned by inputs
    processing(feedback_list)
    output(feedback_list)
    rerun()


def inputs():
    print("Welcome to the feedback generator.")
    print("Please enter multiple feedback phrases, each ending with a '!'")
    feedback = input("Enter as many words as you like. You don't have to capitalize: ")

    phrases = feedback.split('!')
    feedback_list = []

    for phrase in phrases:
        phrase = phrase.strip()
        if phrase:
            words = phrase.split()
            phrase_list = []

            for word in words:
                lowercase_words = [""]  # Words to keep in lowercase
                if word.lower() in lowercase_words:
                    phrase_list.append(word.lower())
                else:
                    phrase_list.append(word.capitalize())

            feedback_list.append(' '.join(phrase_list))

    return feedback_list


def processing(feedback_list):
    for i, phrase in enumerate(feedback_list):
        words = phrase.split(' ')
        capitalized_words = [word.capitalize() for word in words]
        feedback_list[i] = ' '.join(capitalized_words)


def output(feedback_list):
    print("Here are your feedback phrases:")
    for index, phrase in enumerate(feedback_list):
        print(f'{index + 1}: {phrase.strip()}!')


def rerun():
    again = input("Would you like to try again? Enter 'y' or 'n': ")
    if again == 'n':
        print("Thanks for using the program!")
    elif again == 'y':
        main()  # Call the main function to start over
    else:
        print("Invalid input. Please enter 'y' or 'n.")
        rerun()


main()
