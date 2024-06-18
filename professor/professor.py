#

import random


def main():
    lvl = get_level()
    scr = simulate_game(lvl)

    print("Score: ",scr)



def get_level():
    while True :
        try:
            lvl = int(input("Level: "))
            if lvl in [1,2,3]:
                break

        except:
            pass
    return lvl



def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)

    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)

    else :
        x = random.randint(100,999)
        y = random.randint(100,999)

    return x,y


def simulate_rnd(x,y):
    tr = 1
    while tr <= 3:
        try :
            ans = int(input(f"{x} + {y} = "))

            if ans == (x+y):
                return True

            else:
                tr += 1
                print("EEE")

        except:
            tr += 1
            print("EEE")

    print(f"{x} + {y} = {x+y}")
    return False


def simulate_game(level):
    cnt_rnd = 1
    score = 0

    while cnt_rnd <= 10 :
        x, y = generate_integer(level)

        rspnce = simulate_rnd(x,y)
        if rspnce == True:
            score += 1

        cnt_rnd += 1
    return score


if __name__ == "__main__":
    main()
