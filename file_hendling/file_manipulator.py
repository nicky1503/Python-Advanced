import os


def create_a_file(file_name):
    with open(f"files/{file_name}", "w") as file:
        file.write("")


def add_content(file_name, content):
    try:
        with open(f"files/{file_name}", "a") as file:
            file.write(f"{content}\n")
    except FileNotFoundError:
        with open(f"files/{file_name}", "w") as file:
            file.write(f"{content}\n")


def replace_content(file_name, old_string, new_string):
    file_content = []
    file_not_found = False
    try:
        with open(f"files/{file_name}", "r") as file:
            file_content = file.read()
    except FileNotFoundError:
        file_not_found = True
        print("An error occurred")
    if not file_not_found:
        file_content = file_content.replace(old_string, new_string)
        with open(f"files/{file_name}", "w") as file:
            file.write(file_content)


def delete_file(file_name):
    if os.path.exists(f"files/{file_name}"):
        os.remove(f"files/{file_name}")
    else:
        print("An error occurred")


commands = input()
while commands != "End":
    commands = commands.split("-")
    command = commands[0]
    if command == "Create":
        create_a_file(commands[1])
    elif command == "Add":
        add_content(commands[1], commands[2])
    elif command == "Replace":
        replace_content(commands[1], commands[2], commands[3])
    elif command == "Delete":
        delete_file(commands[1])

    commands = input()