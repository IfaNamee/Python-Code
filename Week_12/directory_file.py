"""
Program: Lab9
Author: Ifa Namee
Date: 11/19/2023
purpose: This program is read a file .txt and ask user to add a data and view.
"""


def main():  # Get user input for the desired command
    display_menu()  # Display the menu
    while True:
        command = input("Command: ").lower()

        if command == 'view':
            view_file()
        elif command == 'add':
            add_to_file()
        elif command == 'exit':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")


def display_menu():  # Print the command menu
    print("\nCOMMAND MENU")
    print("view - View username/email file")
    print("add - Add username(s)/email(s) to the file")
    print("exit - Exit program\n")


def create_file():  # Create the file to write
    file = open('directory_file.txt', 'w')
    file.write("mmouse mickeymouse@gmail.com\n")
    print()


def view_file():  # display the contents of the file for read.
    file = open('directory_file.txt', 'r')
    for line in file:
        print(line.strip())
    print()


def add_to_file():  # print instruction and append to add data.
    print("You have chosen to add usernames & emails to the directory.")
    print("Use this format...")
    print("username email@address.com,username email@address.com")
    print("(Separate each new contact's entry with a comma.)")

    data = input().split(',')  # spilt data line entered.
    file = open('directory_file.txt', 'a')
    for entry in data:
        file.write(entry.strip() + '\n')
        print(entry)  # print data added.


main()
