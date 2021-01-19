n = int(input())
matrix = []
for _ in range(n):
    data = input().split()
    matrix.append([int(x) for x in data])
diagonal_sum = 0
for row in range(len(matrix)):
    diagonal_sum += matrix[row][row]
print(diagonal_sum)