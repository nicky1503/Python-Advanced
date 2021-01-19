n = [int(x) for x in input().split(', ')]
matrix = []
for row in range(n[0]):
    data = input().split(', ')
    matrix.append([int(x) for x in data])
max_sum = -9999999
for row in range(len(matrix)-1):
    for element in range(len(matrix[row])-1):
        sum_square = matrix[row][element] + matrix[row][element+1] + matrix[row+1][element] + matrix[row+1][element+1]
        if sum_square > max_sum:
            max_sum = sum_square
            index_1 = matrix[row][element]
            index_2 = matrix[row][element+1]
            index_3 = matrix[row+1][element]
            index_4 = matrix[row+1][element+1]


print(index_1, index_2)
print(index_3, index_4)
print(max_sum)