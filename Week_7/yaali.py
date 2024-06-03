print('This program summarizes a book list.')  # print intro


def main():
    try:
        num_books, price_list = inputs()
        total, average = processing(price_list)
        outputs(num_books, price_list, total, average)
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
    if num_books.isnumeric() is False or int(num_books) == 0: # call validation function to collect int > 0
        num_books = get_pos_int()
    else:
        num_books = get_pos_int()
    while num_books <= 0:
        num_books = get_pos_int()
    price_list = []
    for index in range(num_books):
        book_name = input(f"Enter the name of book #{index + 1}: ")
        book_cost = int(input(f'Enter cost of book {book_name}, to the nearest dollar: '))
        while book_cost <= 0:
            book_cost = get_pos_int()
        price_list.append(book_cost)
    return num_books, price_list


def get_pos_int():  # collect and validate an int > 0
    pos_int = input('Please enter a whole number: ')
    while pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Enter a number greater than 0: ')
    pos_int = int(pos_int)
    return pos_int


def processing(price_list):
    total = sum(price_list)
    average = round(total / len(price_list), 2)
    return total, average


def outputs(num_books, price_list, total, average):
    print(f'Info on {num_books} Books Needed')
    print(f'{"Book #":<10}{"Price":>10}')
    for book_name, book in range(len(price_list)):
        print(f'{price_list[book_name]:>2d}\t\t   ${price_list[book]:>8.2f}')
    print(f'{"Total":<10} ${total:>8.2f}')
    print(f'{"Average":<10} ${average:>8.2f}')


main()
