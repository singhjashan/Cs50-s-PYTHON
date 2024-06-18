#

def main():
    fr = input("Fraction: ")
    fr_con = convert(fr)
    output = gauge(fr_con)
    print(output)

def convert(fr):
    while True:
        try:
            num, den = fr.split("/")
            new_num = int(num)
            new_den = int(den)

            f = new_num / new_den

            if f <= 1 :
                p = int(f * 100)
                return p
            else:
                fr = input("Fraction: ")
                pass

        except(ValueError, ZeroDivisionError):
            raise


def gauge(percent):
    if percent <= 1 :
        return "E"
    elif percent >= 99 :
        return "F"
    else :
        return str(percent) + "%"


if __name__ == "__main__":
    main()
