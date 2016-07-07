####
# Dictionaries
####

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(stuff):
    s=0
    for k in stuff.keys():
        print str(stuff[k])+" "+k
        s+=stuff[k]
    print "Total number of items "+str(s)

displayInventory(stuff)

def addToInventory(ls,inv):
    for i in ls:
        if i in inv.keys():
            inv[i]+=1
        else:
            inv[i]=1
    displayInventory(inv)


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(dragonLoot,stuff)
