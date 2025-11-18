# Reading entire file content
def read_entire_file():
    print("Method 1: Using read()")
    with open("sample.txt", "r") as file:
        content = file.read()
        print("File Content:")
        print(content)
        print("Length:", len(content))

    print("\nMethod 2: Using readlines()")
    with open("sample.txt", "r") as file:
        lines = file.readlines()
        print("File lines:")
        for line in lines:
            print(line.strip())  # strip() removes \n

read_entire_file()