"""
Author: Matt Pettis <matthew.pettis@minneapolis.edu>
Date: 2023-11-14
Description: Lecture notes.
"""

import os

print('Current working directory - compare yours to the example.')
print('Results of running: os.getcwd()')  # for reference
proj_dir = os.getcwd()
print(proj_dir)

# Go to new directory
os.chdir(r'C:\Users\id9707qp\Downloads')
print(os.getcwd())

# Go to project directory
os.chdir(proj_dir)
print(os.getcwd())

# Make a new directory
# Check it out in the file explorer
os.chdir(r'C:\Users\id9707qp\Downloads')
print(f'Current directory: {os.getcwd()}')

new_dir_path = os.getcwd() + r'\aaa_test_dir'
os.makedirs(new_dir_path)

# ;;;; Make new files
os.chdir(r'C:\Users\id9707qp\Downloads')
print(f'Current directory: {os.getcwd()}')

my_file = open('my_file.txt', 'w')  # w is for for write mode
my_file.write('Hello Earth!\n')
my_file.write('Hello Mars!\n')
my_file.close()
print('Done!')

# ;;;; Add some more lines
my_file = open('my_file.txt', 'a')  # 'a' is for append mode
my_file.write('Hello Venus!\n')
my_file.write('Hello Jupiter!\n')
my_file.close()
print('Done again!')

# ;;;; What happens if we use 'w' mode?
my_file = open('my_file.txt', 'w')  # 'w' is for write mode
my_file.write('Hello Mercury!\n')
my_file.write('Hello Neptune!\n')
my_file.close()
print('Done again!')

# ;;;; Read from file and print here:
my_file = open('my_file.txt', 'r')  # r is for read mode
my_data = my_file.read()  # read the entire file into one string
print(my_data)
my_file.close()  # close the file

# ;;;; Read each line into a list
my_file = open('my_file.txt', 'r')  # r for read mode
my_data = my_file.readlines()  # read the entire file into a list
my_file.close()  # close the file

print(my_data)

# ;;;; Read lines one at a time
my_file = open('my_file.txt', 'r')  # r for read mode
my_line = my_file.readline()  # read the first line
print('First line from file: ' + my_line)

# here it's used with a loop
while my_line != '':
    print(my_line, end='')  # end='' overides the default newline
    my_line = my_file.readline()  # loop through a line at a time
my_file.close()  # close the file

# ;;;; More likely version
# See also: https://www.pythonforbeginners.com/files/4-ways-to-read-a-text-file-line-by-line-in-python
with open('my_file.txt', 'r') as my_file:
    for line in my_file:
        print(line.strip())


# ;;;; Writing to a file
all_lines = ['cat', 'bat', 'elephant']
with open('my_file_write.txt', 'a') as my_file:
    for line in all_lines:
        my_file.write(line + '\n')

# What happens if I leave off the \n?
with open('my_file_write.txt', 'a') as my_file:
    for line in all_lines:
        my_file.write(line)




# ;;;; pathlib
from pathlib import Path

# Base, old way
os.getcwd()

# Using Path to get current dir
Path.cwd()
print(Path.cwd())

# Make making new paths easy, using '/' character
print(Path.cwd() / 'my_file.txt')

my_file_path = Path.cwd() / 'my_file.txt'
with open(my_file_path, 'r') as my_file:
    for line in my_file:
        print(line.strip())

