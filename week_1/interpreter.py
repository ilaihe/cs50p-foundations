expression = input("Expression: ").strip()
#Gets the user input and removes any leading or trailing whitespace

x,y,z = expression.split(" ")
#Splits the expression into three parts: x, y, and z


x = float(x)
z = float(z)
#Make is such that the x and z variables are float numbers

if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)

#Change the possible y values as math operators
