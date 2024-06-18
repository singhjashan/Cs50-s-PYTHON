#

file = input("File name :")

modi_name = file.lower()

# conditions

if '.gif' in modi_name:
    print ("image/gif")

elif '.png' in modi_name:
    print("image/png")

elif '.jpeg' in modi_name:
    print("image/jpeg")

elif '.jpg' in modi_name:
    print("image/jpeg")

elif '.pdf' in modi_name:
    print("application/pdf")

elif '.zip' in modi_name:
    print("application/zip")

elif '.txt' in modi_name:
    print("text/plain")

else :
    print("application/octet-stream")

