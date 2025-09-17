# 3. List Index Finder

try:
    numbers = [10,20,30,40]

    idx_num = int(input("Enter an index number: "))

    print(f"{numbers[idx_num]}")

except IndexError:
    print("index is out of range")
except ValueError:
    print("input is not an integer")