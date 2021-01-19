n = int(input())
matrix = []
for m in range(n):
    data = input()
    matrix.append([char for char in data])
special_char = input()
found_special_char = False
for row in range(n):
    for element in range(n):
        if matrix[row][element] == special_char:
            print(f"({row}, {element})")
            found_special_char = True
            break
    if found_special_char:
        break
if not found_special_char and matrix:
    print(f"{special_char} does not occur in the matrix")

