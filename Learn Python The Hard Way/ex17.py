### Exercise 17

from sys import argv; from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)
indata = open(from_file).read()
print "The input file is %d bytes long\nDoes the output file exist? %r\nReady, hit RETURN to continue, CTRL-C to abort." % (len(indata), exists(to_file))
raw_input()
open(to_file,'w').write(indata)
print "Alright, all done."

