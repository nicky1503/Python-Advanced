rows, columns = input().split(', ')
matrix = []
for r in range(int(rows)):
    data = input().split(', ')
    matrix.append([int(x) for x in data])
sum_matrix = 0
for c in matrix:
    sum_matrix += sum(c)
print(sum_matrix)
print(matrix)
