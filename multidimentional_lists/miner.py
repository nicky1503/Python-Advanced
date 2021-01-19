from collections import deque

n = int(input())
directions = deque(input().split())
matrix = []
for row in range(n):
    data = input().split()
    matrix.append([data[x] for x in range(n)])

all_coals = 0
for row in range(n):
    for column in range(n):
        if matrix[row][column] == "c":
            all_coals += 1
        elif matrix[row][column] == "s":
            current_row = row
            current_column = column
no_more_coal = False
program_ended = False
while directions:
    direction = directions.popleft()

    if direction == "right" and current_column + 1 < n:
        current_column += 1
        if matrix[current_row][current_column] == "e":
            print(f"Game over! ({current_row}, {current_column})")
            program_ended = True
            break
        elif matrix[current_row][current_column] == "c":
            all_coals -= 1
            matrix[current_row][current_column] = '*'
    elif direction == "left" and current_column - 1 >= 0:
        current_column -= 1
        if matrix[current_row][current_column] == "e":
            print(f"Game over! ({current_row}, {current_column})")
            program_ended = True
            break
        elif matrix[current_row][current_column] == "c":
            all_coals -= 1
            matrix[current_row][current_column] = '*'
    elif direction == "up" and current_row - 1 >= 0:
        current_row -= 1
        if matrix[current_row][current_column] == "e":
            print(f"Game over! ({current_row}, {current_column})")
            program_ended = True
            break
        elif matrix[current_row][current_column] == "c":
            all_coals -= 1
            matrix[current_row][current_column] = '*'
    elif direction == "down" and current_row + 1 < n:
        current_row += 1
        if matrix[current_row][current_column] == "e":
            print(f"Game over! ({current_row}, {current_column})")
            program_ended = True
            break
        elif matrix[current_row][current_column] == "c":
            matrix[current_row][current_column] = '*'
            all_coals -= 1
    if all_coals == 0:
        program_ended = True
        no_more_coal = True
        print(f"You collected all coals! ({current_row}, {current_column})")
        break
if not program_ended:
    print(f"{all_coals} coals left. ({current_row}, {current_column})")


