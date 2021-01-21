matrix = [[int(n) for n in input().split(', ')] for row in range(int(input()))]

diagonal_1 = [matrix[row][row] for row in range(len(matrix))]
diagonal_2 = [matrix[row][-(row+1)] for row in range(len(matrix))]
print(f"First diagonal: {', '.join([str(n) for n in diagonal_1])}. Sum: {sum(diagonal_1)}")
print(f"Second diagonal: {', '.join([str(n) for n in diagonal_2])}. Sum: {sum(diagonal_2)}")