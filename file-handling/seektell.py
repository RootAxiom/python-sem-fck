# seek() and tell() demonstration
def demonstrate_seek_tell():
    # Create a sample file
    with open("seek_demo.txt", "w") as file:
        file.write("0123456789ABCDEFGHIJ\n")
        file.write("Second line of text\n")
        file.write("Third line of text\n")

    print("=== tell() - Get current position ===")
    with open("seek_demo.txt", "r") as file:
        print("Initial position:", file.tell())
        content = file.read(5)  # Read 5 characters
        print("After reading 5 chars, position:", file.tell())
        print("Content read:", content)

    print("\n=== seek() - Change current position ===")
    with open("seek_demo.txt", "r") as file:
        print("Start position:", file.tell())
        
        # Move to position 10
        file.seek(10)
        print("After seek(10), position:", file.tell())
        print("Content from position 10:", file.read(5))
        
        # Move to beginning
        file.seek(0)
        print("After seek(0), position:", file.tell())
        print("First 5 chars:", file.read(5))
        
        # Move relative to current position
        file.seek(5, 1)  # 1 means relative to current position
        print("After seek(5, 1), position:", file.tell())
        print("Content:", file.read(5))
        
        # Move to end
        file.seek(0, 2)  # 2 means relative to end
        print("After seek(0, 2), position:", file.tell())
        print("At end of file")

    print("\n=== Practical use: Read last line ===")
    with open("seek_demo.txt", "r") as file:
        file.seek(0, 2)  # Go to end
        end_position = file.tell()
        
        # Read backwards to find last newline
        buffer_size = 100
        file.seek(max(0, end_position - buffer_size), 0)
        lines = file.readlines()
        if lines:
            last_line = lines[-1]
            print("Last line:", last_line.strip())

demonstrate_seek_tell()