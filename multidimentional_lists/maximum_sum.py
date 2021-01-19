n = [int(x) for x in input().split(' ')]
matrix = []
for row in range(n[0]):
    data = input().split(' ')
    matrix.append([int(data[x]) for x in range(n[1])])
max_sum = -9999999
found = False
for row in range(len(matrix)-2):
    for element in range(n[1]-2):
        sum_square = matrix[row][element] + matrix[row][element+1] + matrix[row+1][element] + matrix[row+1][element+1] \
                     + matrix[row][element+2] + matrix[row+1][element+2] + matrix[row+2][element] + \
                     matrix[row+2][element+1] + matrix[row+2][element+2]
        if sum_square > max_sum:
            max_sum = sum_square
            index_1 = matrix[row][element]
            index_2 = matrix[row][element+1]
            index_3 = matrix[row][element+2]
            index_4 = matrix[row+1][element]
            index_5 = matrix[row+1][element+1]
            index_6 = matrix[row+1][element+2]
            index_7 = matrix[row+2][element]
            index_8 = matrix[row+2][element+1]
            index_9 = matrix[row+2][element+2]
            found = True

print(f"Sum = {max_sum}")
if found:
    print(index_1, index_2, index_3)
    print(index_4, index_5, index_6)
    print(index_7, index_8, index_9)
