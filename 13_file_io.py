"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""



# Open up the "foo.txt" file (which already exists) for reading
with open('/Lambda/git/Intro-Python-I/src/foo.txt', 'r+') as f:
    read_data = f.read()
# Print all the contents of the file, then close the file
    print(read_data)

# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

f = open('/Lambda/git/Intro-Python-I/src/bar.txt', 'w')
f.write('this is line 1\n')
f.write('this is line 2\n')

with open('/Lambda/git/Intro-Python-I/src/bar.txt', 'r+') as f:
    read_data = f.read()
    print(read_data)

# YOUR CODE HERE