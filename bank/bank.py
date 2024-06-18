#

ans = input("Greeting :")

lower_ans = ans.lower().strip()
if 'hello' in lower_ans :
    print("$0")

elif 'h' == lower_ans[0] :
    print("$20")

else :
    print("$100")
