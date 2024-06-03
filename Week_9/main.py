"""
Author: Matt Pettis <matthew.pettis@minneapolis.edu>
Date: 2022-10-24 - File created
Description:
    Class lecture notes for strings.
"""

# String functions vs methods

# Here, 'int()' is a function
print(int("21"))
print(str(int("21") + 10))
print(str("21" + 10))

# Here, 'isnumeric()' is a method.
print("21".isnumeric())

# sidebar, like apollo program
myYear = input("Enter year")
if (not myYear.isnumeric()):
    print("Why can't you follow simple directions?")

# A method takes the thing before the '.' and makes it the first argument
# to the method, under the covers
#
# "21".isnumeric()
# becomes:
# isnumeric("21")
#
# You just have to treat methods differently, like in the first line.
# If this seems weird, and not make sense, you are right!  With what we know,
# this is a crazy way to do this.  But if you stick with the language, you will
# find this "method" approach helps with other things.
#
# For now, you have to accept there are two different ways, and just stick with
# examples as to how to do which.


# Strings are actually lists of characters
hello_str = "Hello World!"
print(list(hello_str))

# ... being lists, you can index them and get their individual characters.
for index in range(len(hello_str)):
    print(f"index: {index}, character: {hello_str[index]}")

# You can search for parts of a string easily
print(".edu" in "http://minneapolis.edu/")
print(".com" in "http://minneapolis.edu/")

if ".edu" in "http://minneapolis.edu/":
    print("Its educational!")
else:
    print("Its something else")

if ".edu" in "http://minneapolis.edu/":
    print("Its educational!")
else:
    print("Its something else")

# Stripping unwanted spaces
stuff = "This has leading and trailing space. "
print(f"untouched   : '{stuff}'")
print(f"stripped    : '{stuff.strip()}'")
print(f"right strip : '{stuff.rstrip()}'")
print(f"left strip  : '{stuff.lstrip()}'")
print(f"untouched   : '{stuff}'")

# Sometimes, methods change the variable, sometimes not:
# Unchanged
stuff = "  This has leading and trailing space. "
print(f"before      : '{stuff}'")
print(f"stripped    : '{stuff.strip()}'")
print(f"after       : '{stuff}'")

# Changed
# Not ready to explain, just know that some methods change the variable,
# some do not.
num_list = [2, 3, 1]
print(f"before      : '{num_list}'")
print(f"sorted      : '{num_list.sort()}'")  # Get 'None'... hard to explain.
print(f"after       : '{num_list}'")


# Check methods on a string
def stringMethodChecks(mystr):
    print("-----")
    print(f"Argument: {mystr}")
    print(f".islower()? {mystr.islower()}")
    print(f".isupper()? {mystr.isupper()}")
    print(f".isnumeric()? {mystr.isnumeric()}")
    print(f".isalpha()? {mystr.isalpha()}")
    print(f".isalnum()? {mystr.isalnum()}")
    print(f".isspace()? {mystr.isspace()}")
    print(f".istitle()? {mystr.istitle()}")


stringMethodChecks("Hello,!")
stringMethodChecks("hello")
stringMethodChecks("Hello")
stringMethodChecks("Hello There")
stringMethodChecks("HELLO")
stringMethodChecks("123")
stringMethodChecks("123.456")
stringMethodChecks("\t \n")
stringMethodChecks("a1")
