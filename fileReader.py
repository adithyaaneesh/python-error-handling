# File Reader
# Task:
#  Ask the user for a filename and try to open it.
# If the file doesn’t exist → handle FileNotFoundError
# If it exists → print its content
# :memo: Hint: Use open(filename, "r")

try:
    input_file = input("Enter the filename: ")

    x = open(input_file,"r")

    content = x.read()
    print("File content:\n")
    print(content)
    x.close()
except FileNotFoundError:
    print("file doesn’t exist")