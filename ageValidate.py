#2. Age Validator

try:

    age = int(input("Enter your age: "))
    print(f"Your age is {age}")

    if age < 0:
        raise ValueError("Age cannot be negative.")
    
except ValueError:
    print("Enter valid input")