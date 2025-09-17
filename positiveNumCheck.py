# 5. Positive Number Checker

try:
    num = int(input("Enter the number: "))

    print(f"Entered number is: {num}")

    if num < 0:
        raise ValueError
    print("Valid Positive Number")

except ValueError:
    print(" You have  entered negetive number , Please enter the positive number")