# interpreter

num = input("Expression :")

x, y, z = num.split()

x1 = float(x)
# y1 = float(y)
z1 = float(z)

if y == "+" :
    result = x1 + z1

if y == "-" :
    result = x1 - z1

if y == "*" :
    result = x1 * z1

if y == "/" :
    result = x1 / z1

print(round(result, 1))

