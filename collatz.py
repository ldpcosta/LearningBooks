### Functions

# Collatz Sequence

def collatz(num):
    if num%2==0:
        print num//2.0
        return num//2.0
    else:
        print 3*num+1
        return 3*num+1

def input_collatz():
    p=False
    while p!=True:
        n = raw_input(" Numero : ")
        try:
            n=int(n)
            p = True
        except ValueError:
            print "Insert an integer"
            
    while n!=1:
        n = collatz(n)
    return n 
