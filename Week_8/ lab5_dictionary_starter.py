""" M. Bock 9/26/2019 Dictionary Sample Program – this program is very similar to the lab.
As you adapt it to the new content, you will have to add a new feature "edit" to change an existing entry.
Edit has to be added to the menus, and a function has to be added and called. In addition,
note the program features that change case of strings.
You may have to adapt this code to fit capitalization of your new program. """

def main():
    try:
        countries = {'CA': 'Canada', 'US': 'United States', 'MX': 'Mexico'}
        display_menu()
        while True:
            command = input('Command: ')
            command = command.upper()
            if command == 'view':
                view(countries)
            elif command == 'add':
                add(countries)
            elif command == 'del':
                delete(countries)
            elif command == 'exit':
                print('Bye!')
                break
            else:
                print('Not a valid command. Please try again. \n')
    except KeyError:
        print('Key Error ')


def display_menu():
    print('COMMAND MENU')
    print('view - View country name')
    print('add - Add a country')
    print('del - Delete a country')
    print('exit - Exit program')
    print()


def view(countries):
    display_codes(countries)
    country_code = input('Enter country code to view: ')
    country_code = country_code.upper()
    if country_code in countries:
        country_name = countries[country_code]
        print('Country name: ' + country_name + '.\n')
    else:
        print('There is no country with that code. \n')


def add(countries):
    display_codes(countries)
    country_code = input('Enter new country code to add: ')
    country_code = country_code.upper()
    if country_code in countries:
        country_name = countries[country_code]
        print(country_name + ' is already using this code. \n')
    else:
        country_name = input('Enter country name: ')
        country_name = country_name.title()
        countries[country_code] = country_name
        print (country_name + ' was added. \n')


def delete(countries):
    display_codes(countries)
    country_code = input('Enter country code to delete: ')
    country_code = country_code.upper()
    if country_code in countries:
        country_name = countries.pop(country_code)
        print (country_name + ' was deleted. \n')
    else:
        print ('There is no country with that code. \n')


def display_codes(countries):
    country_codes = list(countries.keys())
    country_codes.sort()
    line = 'Country codes: '
    for country_code in country_codes:
        line += country_code + ' '
    print(line)


if __name__ == '__main__':
    main()