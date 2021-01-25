import os
path = input() #"C:/Users/USER/PycharmProjects/ToDoAppPython"
files_info = {}
current_dict = path.count("\\")
for root, dirs, files in os.walk(path):
    if root.count("\\") == current_dict:
        for file in files:
            file_extensions = file.split(".")[-1]
            if file_extensions not in files_info:
                files_info[file_extensions] = []
                files_info[file_extensions].append(file)
            else:
                files_info[file_extensions].append(file)
files_info = {k: v for k, v in sorted(files_info.items(), key=lambda item: (item[0], item[1]))}
with open("C:/Users/USER/Desktop/report.txt", "w") as output_file:
    for key, value in files_info.items():
        output_file.write(f".{key}\n")
        for file in value:
            output_file.write(f"- - - {file}\n")






