n = int(input())
matrix = []
for _ in range(n):
    data = input().split()
    matrix.append([int(x) for x in data])
diagonal_sum = 0
diagonal_sum_2 = 0
index = 0
for row in range(len(matrix)):
    index += 1
    diagonal_sum += matrix[row][row]
    diagonal_sum_2 += matrix[row][-index]
print(abs(diagonal_sum-diagonal_sum_2))