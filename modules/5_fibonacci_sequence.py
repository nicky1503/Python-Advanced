from modules.create_fibonacci_sequence import calculate_sequence, find_index_of_num

commands = input()
while commands != "Stop":
    commands = commands.split()
    if commands[0] == "Create":
        sequence = calculate_sequence(int(commands[2]))
        print(" ".join([str(n) for n in sequence]))
    else:
        try:
            print(f"The number - {commands[1]} is at index {find_index_of_num(sequence, int(commands[1]))}")
        except:
            print(f"The number {commands[1]} is not in the sequence")
    commands = input()
