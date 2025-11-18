# Different read methods
def demonstrate_read_methods():
    # Create a sample file first
    with open("students.txt", "w") as file:
        file.write("Alice,85,Science\n")
        file.write("Bob,92,Math\n")
        file.write("Charlie,78,History\n")
        file.write("Diana,95,Physics\n")

    print("=== Using read() ===")
    with open("students.txt", "r") as file:
        content = file.read()
        print("Entire content:")
        print(content)

    print("\n=== Using readline() ===")
    with open("students.txt", "r") as file:
        print("First line:", file.readline().strip())
        print("Second line:", file.readline().strip())
        print("Third line:", file.readline().strip())

    print("\n=== Using readlines() ===")
    with open("students.txt", "r") as file:
        lines = file.readlines()
        print("All lines as list:")
        for i, line in enumerate(lines, 1):
            print(f"Line {i}: {line.strip()}")

    print("\n=== Using for loop ===")
    with open("students.txt", "r") as file:
        for line_num, line in enumerate(file, 1):
            name, marks, subject = line.strip().split(',')
            print(f"Student {line_num}: {name} scored {marks} in {subject}")

demonstrate_read_methods()