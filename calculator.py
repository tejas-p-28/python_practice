first = input("enter your first number")
operator = input("Input your operator (+,-,*,/,%):")
second = input("enter your second number :")

first = int(first)
second = int(second)

if operator == "+":
    print(int(first) + int(second))
elif operator == "-":
    print(int(first) - int(second))
elif operator == "*":
    print(int(first) * int(second))
elif operator == "/":
    print(int(first) / int(second))
elif operator == "%":
    print(int(first) % int(second))

else:
    print("error occur please check the operation")