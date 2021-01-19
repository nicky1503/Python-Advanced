rows, columns = input().split(', ')
matrix = []
for row in range(int(rows)):
    data = input().split()
    matrix.append([int(n) for n in data])
sum_column = 0
for col in range(int(columns)):
    for row in range(len(matrix)):
        sum_column += matrix[row][col]
    print(sum_column)
    sum_column = 0