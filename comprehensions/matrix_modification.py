n = int(input())
matrix = [[int(n) for n in input().split()] for row in range(n)]

commands = input().split()
while commands[0] != "END":
    command, row, column, value = commands[0], int(commands[1]), int(commands[2]), int(commands[3])
    if command == "Add" and 0 <= row < n and 0 <= column < n:
        matrix[row][column] += value
    elif command == "Subtract" and 0 <= row < n and 0 <= column < n:
        matrix[row][column] -= value
    else:
        print("Invalid coordinates")
    commands = input().split()

[print(' '.join([str(matrix[row][el]) for el in range(len(matrix))])) for row in range(len(matrix))]