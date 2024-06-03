print('This program summarizes a book list.')  # Print intro

def main():
    num_books, book_list = inputs()
    total, average = processing(book_list)
    outputs(num_books, book_list, total, average)

def inputs():
    num_books = get_pos_int('Enter the number of books that you need: ')
    book_list = []
    for index in range(num_books):
        book_name = input(f"Enter the name of book #{index + 1}: ")
        book_cost = get_pos_int(f"Enter the cost of book {book_name}, to the nearest dollar: ")
        book_list.append((book_name, book_cost))
    return num_books, book_list

def get_pos_int(prompt):
    while True:
        pos_int = input(prompt)
        if pos_int.isnumeric() and int(pos_int) > 0:
            return int(pos_int)
        else:
            print('Please enter a valid whole number greater than 0.')

def processing(book_list):
    total = sum(book[1] for book in book_list)
    average = round(total / len(book_list), 2)
    return total, average

def outputs(num_books, book_list, total, average):
    print(f'Info on {num_books} Books Needed')
    print(f'{"Book Name":<20}{"Price":>10}')
    for book in book_list:
        print(f'{book[0]:<20} ${book[1]:>8.2f}')
    print(f'{"Total":<20} ${total:>8.2f}')
    print(f'{"Average":<20} ${average:>8.2f}')

main()
