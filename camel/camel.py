#

camal_case = input("Camelcase :")

print("snake_case :", end="")

# for loop

for l in camal_case :

    if l.isupper():
        print("_"+ l.lower(), end="")

    else :
        print(l, end="")

print()
