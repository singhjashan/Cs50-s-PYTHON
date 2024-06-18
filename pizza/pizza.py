#

import csv
import sys
from tabulate import tabulate

def main():
    check_command_line_arg()

    data = []
    try:

        with open(sys.argv[1],"r") as csvfile :
            rdr = csv.reader(csvfile)
            for row in rdr:
                # print(row)
                data.append(row)

        # print(data)
        print(tabulate(data[1:],headers=data[0],tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")



def check_command_line_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")


    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")



if __name__ == "__main__":
    main()
