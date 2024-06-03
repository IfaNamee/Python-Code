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


def view_contacts():
    with open('contacts1.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print("{:<20} {:<30} {:<15}".format(row[0], row[1], row[2]))


def add_contacts():
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")

    if not name or not email or not phone:
        print("Error: Name, Email and phone are required.")
        return add_contacts()

    with open('contacts1.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone])


main()
