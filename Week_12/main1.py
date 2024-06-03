def create_file():
    with open('directory_file.txt', 'w') as file:
        file.write("mmouse mickeymouse@gmail.com\n")


def view_file():
    with open('directory_file.txt', 'r') as file:
        for line in file:
            print(line.strip())


def add_to_file():
    print("Command: add")
    print("You have chosen to add usernames & emails to the directory.")
    print("Use this format...")
    print("username email@address.com,username email@address.com")
    print("(Separate each new contact's entry with a comma.)")

    data = input().split(',')

    with open('directory_file.txt', 'a') as file:
        for entry in data:
            file.write(entry.strip() + '\n')

    print("Command: view")
    view_file()


def main():
    create_file()
    while True:
        print("\nCOMMAND MENU\n"
              "view - View username/email file\n"
              "add - Add username(s)/email(s) to the file\n"
              "exit - Exit program")
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


main()
