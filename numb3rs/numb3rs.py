##

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        lst_num = ip.split(".")
        print(lst_num)

        for n in lst_num:
            if int(n) < 0 or int(n) > 255:
                return False
        return True

    else:
        return False



if __name__ == "__main__":
    main()
