#### Exercise 33

i = 0

numbers = []

while i<6:
	print "At the top i is %d" % (i)
	numbers.append(i)

	i+=1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % (i)

print "The numbers: "

for num in numbers:
	print num

#### Pt 2 : Recursively

def number(numb2, numb=0, listx=None):
	#################################
	#  number(numb2, numb=0, listx=[]) 
	#  this doesn't work. Why? ;)
	if listx == None:
		listx = []
	##################################
	
	print "At the top i is %d" % (numb)

	if numb == numb2-1:

		listx.append(numb)
		print "Numbers now: ", listx
		
		print "The numbers: "

		for num in listx:
			print num
		
		return None
		
	elif numb < numb2:
		listx.append(numb)
		print "Numbers now: ", listx

		numb+=1
		print "At the bottom i is %d" % (numb)
		number(numb2,numb,listx)
	
	return None
	
