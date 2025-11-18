# Basic Pattern
with open("filename", "mode") as file:
    # operations

# Modes:
# 'r' - Read, 'w' - Write, 'a' - Append
# 'r+' - Read/Write, 'w+' - Write/Read, 'a+' - Append/Read

# Key Methods:
# file.read()      - Read entire content
# file.readline()  - Read one line
# file.readlines() - Read all lines as list
# file.write()     - Write string
# file.writelines()- Write list of strings
# file.seek()      - Move file pointer
# file.tell()      - Get current position

# Always use with statement for automatic closing!