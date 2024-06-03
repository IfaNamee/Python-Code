"""
Program: Lab4
Author: Ifa Namee
Date: 10/22/2023
purpose: This program is calculate total amount of books and average. using mipo method.
"""
print('This program summarizes a book list.')  # print intro


def main():
    try:
        book_info = inputs()
        total, average = processing(book_info)
        outputs(book_info, total, average)
        restart = input('Need more books? Enter y or n: ')
        if restart.lower() == 'y':
            print('OK, let\'s create a new list.')
            main()
        else:
            print('Thanks for using the program.')
    except Exception as err:
        print(err)


def inputs():
    num_books = input('Enter the number of books that you need: ')
    if num_books.isnumeric() is False or int(num_books) == 0:
        num_books = get_pos_int()
    else:
        num_books = int(num_books)
        while num_books <= 0:
            num_books = get_pos_int()

    book_list = []
    for index in range(num_books):
        book_name = input(f"Enter the name of book #{index + 1}: ")
        book_cost = int(input(f'Enter cost of book {book_name}, to the nearest dollar: '))
        while book_cost <= 0:
            book_cost = get_pos_int()
        book_list.append((book_name, book_cost))

    return book_list


def get_pos_int():
    pos_int = input('Please enter a whole number: ')
    while not pos_int.isnumeric() or int(pos_int) == 0:
        pos_int = input('Enter a number greater than 0: ')
    return int(pos_int)


def processing(book_info):
    total = sum(book_cost for _, book_cost in book_info)
    average = round(total / len(book_info), 2)
    return total, average


def outputs(book_list, total, average):
    print(f'Info on {len(book_list)} Books Needed')
    print(f'{"Book Name":<20}{"Price":>10}')
    for book_name, book_cost in book_list:
        print(f'{book_name:<20}${book_cost:>10.2f}')
    print(f'{"Total":<20}${total:>10.2f}')
    print(f'{"Average":<20}${average:>10.2f}')


main()
