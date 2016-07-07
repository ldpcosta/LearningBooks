###
# Lists
###

### Raw
def split_raw(ls):
    s = ""
    for i in range(len(ls)):
        if i == (len(ls)-1):
            s += "and " +str(ls[i])
        else:
            s += str(ls[i])+", "
    print s

### Code Golfing it
def split(ls): print str(", ").join(ls[:-1])+", and "+str(ls[-1])
    

###Rotate array


def grid(ls):
    s = ""
    i=0
    for j in range(len(ls[i])):
        for i in range(len(ls)):
            s += ls[i][j]
        s+="\n"
    return s


###
#test
###

spam = ['apples', 'bananas', 'tofu', 'cats']
split_raw(spam) == split(spam)

gride = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print grid(gride)
