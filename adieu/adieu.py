#

import inflect

p = inflect.engine()

txt = ["Adieu","adieu"]

while True :
    try :
        name = input("Name: ")

    except EOFError :
        print()
        break
    txt.append(name)

txt[2] = "to "+ txt[2]

if len(txt) == 3:
    new_txt = p.join(txt, conj='')

elif len(txt) == 4 :
    new_txt = p.join(txt, final_sep='')

else:
    new_txt = p.join(txt)


# new_txt = p.join(text)
print(new_txt)
