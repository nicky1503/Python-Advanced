n = [int(x) for x in input().split(' ')]
matrix = []
for row in range(n[0]):
    data = input().split(' ')
    matrix.append([x for x in data])
count = 0
equal_cell = False
for row in range(len(matrix)-1):
    for element in range(n[1]-1):
        index_1 = matrix[row][element]
        index_2 = matrix[row][element+1]
        index_3 = matrix[row+1][element]
        index_4 = matrix[row+1][element+1]
        if index_1 == index_2 and index_1 == index_3 and index_1 == index_4:
            count += 1
            equal_cell = True

print(count)
