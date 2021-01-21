n = int(input())
matrix = [[int(x) for x in input().split(', ')] for row in range(n)]
print([el for row in matrix for el in row])