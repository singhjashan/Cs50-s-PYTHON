#


while True :
    fuel = input("Fraction:")

    try :
        nume ,deno = fuel.split("/")

        new_nume = int(nume)
        new_deno = int(deno)

        n = new_nume / new_deno

        if n <= 1 :
            break

    except (ValueError, ZeroDivisionError):
        pass

per = int(n *100)

if per <= 1 :
    print("E")

elif per >= 99 :
    print("F")

else :
    print(f"{per}%")

