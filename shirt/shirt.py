#

import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_command_line_arg()

    try:
        imgfile = Image.open(sys.argv[1])


    except FileNotFoundError:
        sys.exit("Input does not exist")

    shrt_file= Image.open("shirt.png")

    syz = shrt_file.size

    mppt = ImageOps.fit(imgfile, syz)

    mppt.paste(shrt_file, shrt_file)

    mppt.save(sys.argv[2])






def check_command_line_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    if chk_extension(file1[1]) == False:
        sys.exit("Invalid output")

    if chk_extension(file2[1]) == False:
        sys.exit("Invalid output")

    if file1[1].lower() != file1[1].lower():
        sys.exit("Input and output have different extensions")






def chk_extension(file):
    if file in [".jpg",".png",".jepg"]:
        return True
    return False




if __name__ == "__main__":
    main()
