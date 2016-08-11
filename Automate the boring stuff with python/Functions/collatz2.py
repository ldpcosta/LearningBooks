# Collatz

def collatz(number):
	if number%2==0:
		print number//2
		return number//2
	else:
		print number*3 + 1
		return number*3 + 1

def collatzseq(num):
	print num
	while num != 1:
		num = collatz(num)

while True:

	n = raw_input("> ")

	try:
		collatzseq(int(n))
		break
	except ValueError:
		print "Type a number instead"
