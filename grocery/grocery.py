#

grsry = {}

while True :
    try :

        itm = input().lower()

        if itm in grsry :
            grsry[itm] += 1

        else :
            grsry[itm] = 1

    except EOFError :

        for key in sorted(grsry.keys()) :
            print(grsry[key], key.upper())

        break


