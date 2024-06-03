"""
Author: Ifa Namee
Date: 12/3/2023
Description:
    Read lab16.csv
"""

import csv  # import statement for csv file.

csv_file = open('lab16.csv', 'r')  # open file to read only.
file_reader = csv.reader(csv_file)  # variable to read.
for row in file_reader:  # for loop to row and column.
    print('{:<12} {:<10} {:<15} {:<15} {:<15}'.format(*row))  # print result with position set.
csv_file.close()  # close file.


"""
import csv

def read_csv_file(csv_file_path):
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # row contains column headers
        columns = next(csv_reader)

        # Print column headers
        print("\t\t".join(columns))

        # Print rows in column format
        for row in csv_reader:
            print("\t\t".join(row))


if __name__ == "__main__":
    file_path = 'lab16.csv'
    read_csv_file(file_path)
"""


