#

dic = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

totl_amnt = 0

while True :
    try :
        itm = input("Item: ").title()

        if itm in dic :
            totl_amnt += dic[itm]

            print("Total: $", end="")
            print("{:.2f}".format(totl_amnt))

    except :
        print()
        break
