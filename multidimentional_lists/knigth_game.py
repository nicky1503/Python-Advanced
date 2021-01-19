def kill_knights(board, row, column):
    kills = 0
    #right reach
    try:
        row_reach = row-1
        column_reach = column + 2
        if not row_reach < 0 and not column_reach < 0:
            if board[row_reach][column_reach] == 'K':
                kills += 1
    except IndexError:
        pass
    try:
        row_reach = row + 1
        column_reach = column + 2
        if not row_reach < 0 and not column_reach < 0:
            if board[row_reach][column_reach] == 'K':
                kills += 1
    except IndexError:
        pass
    #left reach
    try:
        row_reach = row-1
        column_reach = column - 2
        if not row_reach < 0 and not column_reach < 0:
            if board[row_reach][column_reach] == 'K':
                kills += 1
    except IndexError:
        pass
    try:
        row_reach = row + 1
        column_reach = column - 2
        if not row_reach < 0 and not column_reach < 0:
            if board[row_reach][column_reach] == 'K':
                kills += 1
    except IndexError:
        pass
    #reach down
    try:
        row_reach = row-2
        column_reach = column + 1
        if not row_reach < 0 and not column_reach < 0:
            if board[row_reach][column_reach] == 'K':
                kills += 1
    except IndexError:
        pass
    try:
        row_reach = row - 2
        column_reach = column - 1
        if not row_reach < 0 and not column_reach < 0:
            if board[row_reach][column_reach] == 'K':
                kills += 1
    except IndexError:
        pass

    #reach up

    try:
        row_reach = row + 2
        column_reach = column + 1
        if not row_reach < 0 and not column_reach < 0:
            if board[row_reach][column_reach] == 'K':
                kills += 1
    except IndexError:
        pass
    try:
        row_reach = row + 2
        column_reach = column - 1
        if not row_reach < 0 and not column_reach < 0:
            if board[row_reach][column_reach] == 'K':
                kills += 1
    except IndexError:
        pass
    return kills


n = int(input())
game_board = []
for _ in range(n):
    data = input()
    game_board.append([data[x] for x in range(n)])
max_kills = 0
num_of_removed_knights = 0
if n <= 2:
    pass
else:
    while True:
        for row in range(n):
            for column in range(n):
                if game_board[row][column] == "K":
                    number_of_kills = kill_knights(game_board, row, column)
                    if number_of_kills > max_kills:
                        max_kills = number_of_kills
                        row_of_max_kill = row
                        column_of_max_kill = column

        if max_kills == 0:
            break
        else:
            game_board[row_of_max_kill][column_of_max_kill] = "0"
            num_of_removed_knights += 1
        max_kills = 0
print(num_of_removed_knights)


