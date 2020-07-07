print(chr(27) + "[2J")
print("Question 1: ")

# Print "Hello, world!" to your terminal
print("Hello, world!")

print("Question 2: ")

# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# YOUR CODE HERE
print(2 ** 2)

print("Question 3:")

"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12

# YOUR CODE HERE
print(x + int(y))

# Write a print statement that combines x + y into the string value 57
print(str(x) + y)

# YOUR CODE HERE

print("Question 4:")

"""
Python provides a number of ways to perform printing. Research
how to print using the 
printf operator, 
the `format` string method str.format()
, and by using f-strings.
"""

import sys
def printf(format, *args):
    sys.stdout.write(format % args)

x = 10
y = 2.24552
z = "I like turtles!"

printf("x is %d, y is %.2f is \"%s\"", x, y, z)

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

# Use the 'format' string method to print the same thing

# Finally, print the same thing using an f-string

print("Question 5")
# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
print(x + y)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE

y.remove(8)
print(x + y)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE

x.append(9)
x.append(99)
x.append(10)
print(x)

# Print the length of list x
# YOUR CODE HERE

print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for val in x:
    print(val * 1000)

print("Question 6")

"""
Python tuples are sort of like lists, except they're immutable and
are usually used to hold heterogenous data, as opposed to lists
which are typically used to hold homogenous data. Tuples use
parens instead of square brackets.

More specifically, tuples are faster than lists. If you're looking
to just define a constant set of values and that set of values
never needs to be mutated, use a tuple instead of a list.

Additionally, your code will be safer if you opt to "write-protect"
data that does not need to be changed. Tuples enforce immutability
automatically.
"""

# Example:

import math

def dist(a, b):
    """Compute the distance between two x,y points."""
    x0, y0 = a  # Destructuring assignment
    x1, y1 = b

    return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

a = (2, 7)   # <-- x,y coordinates stored in tuples
b = (-14, 72)

print(dist(a, b))

# round to the nearest tenth positionn

print("%.1f" % dist(a, b))

"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print(a[slice(1, 2)])

# Output the second-to-last element: 9
print(a[slice(len(a)-2, len(a)-1)])

# Output the last three elements in the array: [7, 9, 6]
print(a[slice(len(a)-3, len(a))])

# Output the two middle elements in the array: [1, 7]
print(a[slice(len(a)-4, len(a)-2)])

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[slice(1, len(a))])

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[slice(0, len(a)-1)])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[slice(7, 12)])

print("Question 8")

"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []

for number in '12345':
    y.append(int(number))

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [num ** 3 for num in range(10)]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [word.upper() for word in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

# x = input("Enter comma-separated numbers: ").split(',')

x = [1,2,3,4,5,6]

# What do you need between the square brackets to make it work?
y = [num for num in x if num % 2 == 0]

print(y)

"""
List Comprehensions
"""
odds = [1, 3, 5, 7, 9]
# like map
print([x+1 for x in odds])

# like filter
print([x for x in odds if 25 % x == 0])

# general form
# [<map expression> for <name> in <sequence expression> if <filter expression>]

"""
Dictionary Comprehensions
"""
print({x: x*x for x in range(3, 6)})


# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard


# Print out "Even!" if the number is even. Otherwise print "Odd"
def is_even():
    num = input("Enter a number: ")
    num = int(num)
    if num % 2 == 0:
        print("Even!")
    else:
        print("Odd")

# YOUR CODE HERE2

is_even()

