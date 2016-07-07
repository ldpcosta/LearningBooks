###
# Lists
###

### First : As raw as possible

def split_raw(ls):
    s = ""
    for i in range(len(ls)):
        if i == (len(ls)-1):
            s += "and " +str(ls[i])
        else:
            s += str(ls[i])+", "
    print s

### code golfing it

def split(ls): print str(", ").join(ls[:-1])+", and "+str(ls[-1])
    


#test
##

spam = ['apples', 'bananas', 'tofu', 'cats']
split_raw(spam) == split(spam)

