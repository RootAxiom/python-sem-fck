# Creating and writing to a file
def create_and_write_file():
    # Method 1: Using open() and close()
    file = open("sample.txt", "w")
    file.write("Hello World!\n")
    file.write("Welcome to Python File Handling.\n")
    file.write("This is line 3.\n")
    file.close()
    print("File created and data written successfully!")

    # Method 2: Using with statement (recommended)
    with open("sample2.txt", "w") as file:
        file.write("Using with statement.\n")
        file.write("File automatically closes.\n")
    print("Second file created using 'with' statement!")

create_and_write_file()