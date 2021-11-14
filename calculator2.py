num1 = float(input("enter your number: "))
operator = input("enter your operator: ")
num2 = float(input("enter your second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("Invalid operator")

    


