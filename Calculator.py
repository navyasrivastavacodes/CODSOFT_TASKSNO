print("=" * 40)
print("      SIMPLE CALCULATOR")
print("=" * 40)

while True:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    z = input("Enter an operator (+, -, *, /): ")

    if z == "+":
        print("Addition =", x + y)

    elif z == "-":
        print("Subtraction =", x - y)

    elif z == "*":
        print("Multiplication =", x * y)

    elif z == "/":
        if y == 0:
            print("Cannot divide by zero")
        else:
            print("Division =", x / y)

    else:
        print("Invalid operator")

    p = input("Do you want another calculation? (yes/no): ")

    if p == "no":
        print("Thank you for using the calculator!")
        break