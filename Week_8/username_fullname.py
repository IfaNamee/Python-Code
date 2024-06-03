"""
Program: Lab 5
Author: Ifa Namee
Date: 10/22/2023
purpose: This program is adapted conditions based on user choose to do such as view names,
        add name, edit name and delete name using mipo method.
"""


def main():
    try:
        names = {'JB': 'JOE BIDEN', 'DT': 'DONALD TRUMP', 'BK': 'BARAK OBAMA'}
        display_menu()
        while True:
            command = input('Command: ')
            command = command.upper()
            if command == 'VIEW':
                view(names)
            elif command == 'ADD':
                add(names)
            elif command == 'EDIT':
                edit(names)
            elif command == 'DEL':
                delete(names)
            elif command == 'EXIT':
                print('Bye!')
                break
            else:
                print('Not a valid command. Please try again.\n')
    except KeyError:
        print('Key Error')


def display_menu():
    print('COMMAND MENU')
    print('view - View User names')
    print('add - Add a user')
    print('edit - Edit a user')
    print('del - Delete a user')
    print('exit - Exit program')
    print()


def view(names):
    display_names(names)
    username = input('Enter first name to view: ')
    username = username.upper()
    if username in names:
        fullname = names[username]
        print('Full name: ', fullname.title() + '\n')
    else:
        print('There is no name with this user.\n')


def add(names):
    display_names(names)
    username = input('Enter User name to add: ')
    username = username.upper()
    if username in names:
        fullname = names[username]
        print('Sorry', username, fullname + ' has already taken.\n')
    else:
        fullname = input('Enter a first and last name: ')
        fullname = fullname.capitalize()
        names[username] = fullname
        print(username, 'user name was added.\n')


def edit(names):
    display_names(names)
    username = input('Enter user name that you want to edit: ')
    username = username.upper()
    if username in names:
        fullname = names[username]
        new_fullname = input('Enter first and last name you want to change it: ')
        new_fullname = new_fullname.capitalize()
        names[username] = new_fullname
        print(fullname, 'was edited to: ', new_fullname.capitalize(), '\n')
    else:
        print('There is no user with this name.\n')


def delete(names):
    display_names(names)
    username = input('Enter user name to delete: ')
    username = username.upper()
    if username in names:
        deleted_name = names.pop(username)
        print(username + ' was deleted.\n')
    else:
        print('There is no user with this name.\n')


def display_names(names):
    usernames = list(names.keys())
    usernames.sort()
    line = 'User names: '
    for username in usernames:
        line += username + ' '
    print(line)


main()

