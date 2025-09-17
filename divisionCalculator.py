# 1. Division Calculator

try:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    result = num1 / num2

    print(f"{num1} / {num2} = {result}")

except ZeroDivisionError:
    print("Can't divide by Zero")

except ValueError:
    print("Enter valid input")