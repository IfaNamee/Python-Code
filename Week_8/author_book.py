"""
Program: Lab5
Author: Ifa Namee
Date: 10/22/2023
purpose: This program is adapted condition user choose such as view authors,
        add authors, edit authors and delete authors using mipo method.
"""


def main():
    try:
        names = {'ROBERT KIYOSAKI': 'RICH DAD POOR DAD',
                 'JAMES CLEAR': 'ATOMIC HABITS',
                 'HELEN KELLER': 'THE STORY OF MY LIFE'}
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
    print('view - View readings')
    print('add - Add a readings')
    print('edit - Edit a readings')
    print('del - Delete a readings')
    print('exit - Exit program')
    print()


def view(names):
    display_names(names)
    username = input('Enter author name to view book: ')
    username = username.upper()
    if username in names:
        fullname = names[username]
        print('Author name: ' + username, "\nBook name: " + fullname + '\n')
    else:
        print('There is no  author name with.\n')


def add(names):
    display_names(names)
    username = input('Enter author name to add: ')
    username = username.upper()
    if username in names:
        fullname = names[username]
        print('Sorry', username, fullname + ' has already taken.\n')
    else:
        fullname = input('Enter a book title: ')
        fullname = fullname.title()
        names[username] = fullname
        print(username, fullname + ' was added.\n')


def edit(names):
    display_names(names)
    username = input('Enter author name to edit: ')
    username = username.upper()
    if username in names:
        fullname = names[username]
        new_fullname = input('Enter author you want to change it: ')
        new_fullname = new_fullname.title()
        names[username] = new_fullname
        print(username, fullname, 'was edited to: ', new_fullname.upper(), fullname + '\n')
    else:
        print('There is no author name with this.\n')


def delete(names):
    display_names(names)
    username = input('Enter author name to delete: ')
    username = username.upper()
    if username in names:
        fullname = names.pop(username)
        print(username, fullname + ' was deleted.\n')
    else:
        print('There is no author name with this name.\n')


def display_names(names):
    usernames = list(names.keys())
    usernames.sort()
    line = 'Author names: '
    for username in usernames:
        line += username + ', '
    print(line)


main()
