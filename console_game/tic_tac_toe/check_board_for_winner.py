def check_for_winner(board):
    for rows in board:
        if " " not in rows:
            check_rows = [rows[el] == rows[el + 1] for el in range(len(rows) - 1)]
            if all(check_rows):
                return True
    diagonal = [board[index][index] for index in range(len(board))]
    diagonal2 = [board[index-1][-index] for index in range(1, len(board)+1)]
    if " " not in diagonal:
        if all([diagonal[el] == diagonal[el+1] for el in range(len(diagonal) -1)]):
            return True
    if " " not in diagonal2:
        if all([diagonal2[el] == diagonal2[el+1] for el in range(len(diagonal2) - 1)]):
            return True
    for index in range(len(board)):
        column = [board[i][index] for i in range(len(board))]
        if " " not in column:
            if all([column[el] == column[el + 1] for el in range(len(column) - 1)]):
                return True