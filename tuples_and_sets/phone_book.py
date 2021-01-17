data = input()
phonebook = {}
while not data.isdigit():
    name, number = data.split('-')
    phonebook[name] = number
    data = input()
for _ in range(int(data)):
    searched_name = input()
    if searched_name in phonebook:
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")