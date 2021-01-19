n = [int(c) for c in input().split()]
matrix = []
for row in range(n[0]):
    data = input().split()
    matrix.append([data[el] for el in range(n[1])])

commands = input().split()
while commands[0] != "END":
    swap = commands[0]

    if swap == "swap":
        row_1 = int(commands[1])
        element_1 = int(commands[2])
        row_2 = int(commands[3])
        element_2 = int(commands[4])
        if row_1 < n[0] and row_2 < n[0] and element_1 < n[1] and element_2 < n[1]:
            matrix[row_1][element_1], matrix[row_2][element_2] = matrix[row_2][element_2], matrix[row_1][element_1]
            for row in range(len(matrix)):
                for el in matrix[row]:
                    print(el, end=' ')
                print()
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    commands = input().split()