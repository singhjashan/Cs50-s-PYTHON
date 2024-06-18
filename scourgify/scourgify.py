##

import sys
import csv


def main():
    check_command_line_arg()

    data= []
    try:
        with open(sys.argv[1],"r") as file :
            rdr = csv.DictReader(file)
            for row in rdr :
                # print(row)
                splt_name = row["name"].split(",")
                # print(splt_name)
                data.append({"first":splt_name[1].strip(), "last":splt_name[0].strip(), "house": row["house"]})


    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    # print(data)

    with open(sys.argv[2],"w") as after :
        wrtr = csv.DictWriter(after, fieldnames=["first","last","house"])
        wrtr.writerow({"first":"first", "last":"last", "house":"house"})
        for row in data :
            wrtr.writerow({"first":row["first"], "last":row["last"], "house":row["house"]})




def check_command_line_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
