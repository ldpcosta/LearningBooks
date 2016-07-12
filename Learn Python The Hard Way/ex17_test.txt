###exercise 16 study drill

from sys import argv


script, filename = argv

print "Now I'm going to read the file you just created:\n"
txt = open(filename)
print txt.read()

