# Different write methods
def demonstrate_write_methods():
    print("=== Using write() ===")
    with open("write_demo.txt", "w") as file:
        file.write("This is written using write() method.\n")
        file.write("Second line with write().\n")
        file.write("Third line with write().\n")

    print("=== Using writelines() ===")
    lines_to_write = [
        "First line with writelines()\n",
        "Second line with writelines()\n",
        "Third line with writelines()\n"
    ]
    with open("writelines_demo.txt", "w") as file:
        file.writelines(lines_to_write)

    # Verify content
    with open("write_demo.txt", "r") as file:
        print("write() method output:")
        print(file.read())

    with open("writelines_demo.txt", "r") as file:
        print("writelines() method output:")
        print(file.read())

demonstrate_write_methods()