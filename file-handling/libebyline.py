# Reading file line by line
def read_line_by_line():
    print("Method 1: Using readline() in loop")
    with open("sample.txt", "r") as file:
        line = file.readline()
        line_count = 1
        while line:
            print(f"Line {line_count}: {line.strip()}")
            line = file.readline()
            line_count += 1

    print("\nMethod 2: Using for loop (recommended)")
    with open("sample.txt", "r") as file:
        for line_num, line in enumerate(file, 1):
            print(f"Line {line_num}: {line.strip()}")

read_line_by_line()