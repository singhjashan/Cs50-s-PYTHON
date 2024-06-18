#

import sys

def main():
    check_command_line_arg()

    try:
        file = open(sys.argv[1],"r")
        lines = file.readlines()
        # print(lines)


    except FileNotFoundError:
        sys.exit("File does not exist")

    cnt = 0
    for l in lines:
        if chk_line(l) == False:
            cnt+=1
    print(cnt)




def check_command_line_arg():
    if len(sys.argv) < 2 :
        sys.exit("Too few command-line arguments")

    if len(sys.argv) >2:
        sys.exit("Too many command-line arguments")

    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

def chk_line(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False





if __name__ == "__main__":
    main()
