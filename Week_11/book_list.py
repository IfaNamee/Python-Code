"""
Program: Lab8
Author: Ifa Namee
Date: 11/12/2023
purpose: This program is calculate total amount of books and average.
         using mipo method and import pyinputplus as pyip
"""

# Import the pyinputplus library for input validation
import pyinputplus as pyip

print('This program summarizes a book list.')  # Print introduction


def main():
    try:  # bad input handler
        book_info = inputs()  # Collect book information
        total, average = processing(book_info)  # Process book information
        outputs(book_info, total, average)  # Display book information

        restart = pyip.inputYesNo('Need more books? Enter yes or no: ')  # Ask user to stop and continue.
        if restart == 'yes':
            print("OK, let's create a new list.")  # print prompt
            main()
        else:
            print('Thanks for using the program.')
    except Exception as wrong:  # bad input handler
        print(wrong)  # display bad input user entered


def inputs():
    # Ask user to enter positive integer greater than Zero
    num_books = pyip.inputInt('Enter the number of books that you need: ', min=1)
    book_list = []  # Initialize an empty list to store book information

    for index in range(num_books):
        # Ask user to enter book name that accept a string input
        book_name = pyip.inputStr(f"Enter the name of book #{index + 1}: ")
        # Ask user to enter positive integer less than 100
        book_cost = pyip.inputNum(f'Enter cost of book {book_name}, max $100: ', lessThan=100)
        # Append book information to the list
        book_list.append((book_name, book_cost))

    return book_list  # return value back


def processing(book_info):
    total = sum(book_cost for _, book_cost in book_info)  # Calculate the total cost of all books
    average = round(total / len(book_info), 2)  # # Calculate the average cost per book
    return total, average  # return value back


def outputs(book_list, total, average):
    print(f'Info on {len(book_list)} Books Needed')  # display number of the list
    print(f'{"Book Name":<20}{"Price":>10}')  # display information title

    for book_name, book_cost in book_list:
        print(f'{book_name:<20}${book_cost:>10.2f}')  # display list of items and amount

    print(f'{"Total":<20}${total:>10.2f}')  # Display total cost
    print(f'{"Average":<20}${average:>10.2f}')  # Display average of total cost


main()
