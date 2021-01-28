from tic_tac_toe import check_for_winner

def get_players_info():
    global player_one_name
    global player_two_name
    player_one_name = input("Player one name: ")
    player_two_name = input("Player two name: ")
    signs_to_play = ["X", "O"]
    global player_one_sign
    player_one_sign = input(f"{player_one_name} would you like  to play with 'X' or 'O'?: ")
    signs_to_play.remove(player_one_sign)
    global player_two_sign
    player_two_sign = signs_to_play[0]


def print_board_numeration():
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    print(f"{player_one_name} starts first!")


def drew_main_board(board):
    for row in board:
        print("| ", end="")
        print(" | ".join([x for x in row]), end="")
        print(" |", end="")
        print()


def add_players_mark_to_board(mark_position, board, player):
    n = int(mark_position) - 1
    row = n // 3
    el = n % 3
    if player == player_one_name:
        board[row][el] = player_one_sign
    else:
        board[row][el] = player_two_sign
    return board


def get_players_turn(player):
    mark_position = input(f"{player} choose a free position [1-9]: ")
    return mark_position

def play_game():
    get_players_info()
    print_board_numeration()
    game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    current_payer = player_one_name
    next_player = player_two_name
    while True:
        game_board = add_players_mark_to_board(get_players_turn(current_payer), game_board, current_payer)
        drew_main_board(game_board)
        if check_for_winner(game_board):
            print(f"{current_payer} won!!!")
            break
        current_payer, next_player = next_player, current_payer


play_game()
