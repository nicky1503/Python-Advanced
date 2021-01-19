from collections import deque


def is_it_valid(row, column, n, row_bomb, cul_bomb):
    return 0 <= row+row_bomb < n and 0 <= column + cul_bomb < n


def explode_bomb(board, bomb):
    row_range = [1, 1, 0, -1, -1, -1, 0, 1]
    column_range = [0, 1, 1, 1, 0, -1, -1, -1]
    bomb = bomb.split(',')
    row_bomb = int(bomb[0])
    cul_bomb = int(bomb[1])
    if matrix[row_bomb][cul_bomb] > 0:
        for i in range(len(row_range)):
            if is_it_valid(row_range[i], column_range[i], n, row_bomb, cul_bomb):
                if board[row_bomb+row_range[i]][cul_bomb+column_range[i]] > 0:
                    board[row_bomb+row_range[i]][cul_bomb+column_range[i]] -= board[row_bomb][cul_bomb]
    board[row_bomb][cul_bomb] = 0
    return board


n = int(input())
matrix = []
for row in range(n):
    data = input().split()
    matrix.append([int(data[x]) for x in range(n)])
bomb_coordinates = deque(input().split())
while bomb_coordinates:
    current_bomb = bomb_coordinates.popleft()
    matrix = explode_bomb(matrix, current_bomb)

sum_of_alive_sells = 0
count_of_alive_cells = 0
for row in matrix:
    for el in row:
        if el > 0:
            sum_of_alive_sells += el
            count_of_alive_cells += 1
print(f"Alive cells: {count_of_alive_cells}")
print(f"Sum: {sum_of_alive_sells}")
for row in matrix:
    print(" ".join([str(x) for x in row]))