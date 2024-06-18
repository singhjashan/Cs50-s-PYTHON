#

import random

while True :
    try:
        lvl = int(input("Level: "))
        if lvl > 0 :
            break

    except:
        pass

rndm_nu = random.randint(1, lvl)

while True:
    try:
        gss = int(input("Guess: "))
        if gss > 0:
            if gss < rndm_nu :
                print("Too Small!")

            elif gss > rndm_nu :
                print("Too large!")

            else :
                print("Just right!")

    except:
        
        pass
