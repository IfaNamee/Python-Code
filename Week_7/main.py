print('This program summarizes a book list.')  # print intro


def main():
    try:
        num_books, book_data = inputs()
        total, average = processing(book_data)
        outputs(num_books, book_data, total, average)
        restart = input('Need more books? Enter y or n: ')
        if restart.lower() == 'y':
            print("OK, let's create a new list.")
            main()
        else:
            print('Thanks for using the program.')
    except Exception as err:
        print(err)


def inputs():
    num_books = get_pos_int("Enter the number of books that you need: ")
    book_list = []
    for index in range(num_books):
        book_name = input(f"Enter the name of book #{index + 1}: ")
        book_cost = get_pos_int(f"Enter the cost of {book_name}, to the nearest dollar: ")
        book_list.append((book_name, book_cost))
    return num_books, book_list


def get_pos_int(prompt):
    pos_int = input(prompt)
    if pos_int.isnumeric() or int(pos_int) == 0:
        pos_int = input('Please enter a whole number: ')
    else:
        pos_int = input('Enter a number greater than 0: ')
    return int(pos_int)


def processing(book_data):
    total = sum(cost for name, cost in book_data)
    average = round(total / len(book_data), 2)
    return total, average


def outputs(num_books, book_list, total, average):
    print(f'Info on {num_books} Books Needed')
    print(f'{"Book Name":<20}{"Price":>10}')
    for book_name, price in book_list:
        print(f'{book_name:<20}${price:>10.2f}')
    print(f'{"Total":<20}${total:>10.2f}')
    print(f'{"Average":<20}${average:>10.2f}')


main()
