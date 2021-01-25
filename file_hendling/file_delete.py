import os
try:
    os.remove("files\\my_first_file.txt")
except:
    print("File already deleted.")
