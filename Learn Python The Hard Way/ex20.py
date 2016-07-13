### exercise 20

# Import argv from sys library
from sys import argv

# Take the input_file from shell arguments
script, input_file = argv

#define funciton print_all, which prints the whole document to the screen
def print_all(f):
	print f.read()

#define function rewind, which sets the "cursor"
# to the start of the file
def rewind(f):
	f.seek(0)


#print the next line in the file, in order, relative to the last one
def print_a_line(line_count,f):
	print line_count, f.readline()



# Opening the file, numbering the lines and other stuff.
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(f)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line,current_file)
current_line+=1
print_a_line(current_line,current_file)
current_line+=1
print_a_line(current_line,current_file)