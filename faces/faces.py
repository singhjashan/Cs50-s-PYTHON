#

def main():
    txt = input("")

    result = cnvrt(txt)

    print(result)


#######################

def cnvrt(txt):

    replaced_txt = txt.replace(":)","🙂")

    replaced_txt2 = replaced_txt.replace(":(","🙁")

    return replaced_txt2


# calling the function
main()
