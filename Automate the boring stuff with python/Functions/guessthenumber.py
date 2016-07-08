##
# Guess the number
##

import random as rnd

def GuessTheNumber():
    y = rnd.randint(1,30)
    x = 0
    while int(x) != y:
        x = int(raw_input("Which number? \n"))
        print y
        if int(x)==y:
            break
        elif int(x)>y:
            print "Too high!"
        else:
            print "Too low!"
        
    print "Good Job"


GuessTheNumber()
