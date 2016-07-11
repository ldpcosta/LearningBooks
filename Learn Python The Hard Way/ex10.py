#exercise 10 - more printing

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print """
These are some escape sequence examples:
\t Backslash \\ a
\t Double-quote \" a
\t Single-quote \' a
\t ASCII bell \a a
\t ASCII backspace \b a
\t ASCII formfeed \f a
\t ASCII linefeed \n a
\t Carriage return \r a
\t horizontal tab \t a
\t ASCII vertical tab \v a
"""

for i in range(30):
	for j in ["/","-","|","\\","|"]:
		print "%s\r" % j
