try:
    file = open("files\\File Opener\\text.txt", "r")
    print("File Found")
except FileNotFoundError:
    print("File not found")