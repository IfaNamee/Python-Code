"""
Author: Ifa Namee
Date: 12/3/2023
Description: View and add on csv file.
"""
import csv


def main():  # Get user input for the desired command
    display_menu()  # Display the menu
    while True:
        command = input("Command: ").lower()

        if command == 'view':
            view_contacts()
        elif command == 'add':
            add_contacts()
        elif command == 'exit':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")


def display_menu():  # Print the command menu
    print("\nCOMMAND MENU")
    print("view - View contact file")
    print("add - Add contact to the file")
    print("exit - Exit program\n")


def view_contacts():  # Write in file.
    with open('contacts.csv', 'r') as file:
        reader = csv.reader(file)
        print("{:<20} {:<30} {:<15}".format("Name", "Email", "Phone"))  # print header.
        for row in reader:
            print("{:<20} {:<30} {:<15}".format(row[0], row[1], row[2]))  # print rows.


def add_contacts():
    name = input("Enter name: ")  # Ask user to enter name.
    email = input("Enter email: ")  # Ask user to enter email.
    phone = input("Enter phone number: ")  # Ask user to enter phone number.

    if not name or not email or not phone:  # invalid enter or forget to enter.
        print("Error: Name, Email and phone are required.")
        return add_contacts()

    with open('contacts.csv', 'a', newline='') as file:  # add contact file to write.
        writer = csv.writer(file)  # variable
        writer.writerow([name, email, phone])  # store the rows.


main()
