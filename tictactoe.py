from random import choice

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
moves = {"X": [], "O":[]}
coords = {1: [0, 0],
          2: [0, 1],
          3: [0, 2],
          4: [1, 0],
          5: [1, 1],
          6: [1, 2],
          7: [2, 0],
          8: [2, 1],
          9: [2, 2]}

def display_board():
    """
    prints the board in it's current condition.
    @board -- 2d 3x3 list
    """
    d_row = "+---+---+---+"
    in_row = "|   |   |   |"
    num_row = lambda a, b, c: f"| {a} | {b} | {c} |"
    print(d_row)
    for row in board:
        print(in_row, num_row(*row), in_row, d_row, sep="\n")

def enter_move():
    """make human move (human is O)"""
    valid_move = False
    while not valid_move:
        try:
            move = int(input("Enter a move: "))
            while move not in make_list_of_free_fields():
                move = int(input(f"Invalid move {move}, choose from {make_list_of_free_fields()}: "))
            valid_move = True
        except ValueError:
            print("Input Error! Enter an integer only.")

    moves["O"].append(move)
    board[coords[move][0]][coords[move][1]] = "O"
    display_board()

def make_list_of_free_fields():
    """list of free fields"""
    return [n for n in range(1, 10) if n not in moves["X"] and n not in moves["O"]]

def victory():
    """declare victory returning False or X or O"""
    for sign in ['X', 'O']:
        for row in board:
            if [sign] * 3 == row:
                return sign
        for c_index in range(0, 3):
            signs = 0
            for row in board:
                if row[c_index] == sign:
                    signs += 1
            if signs == 3:
                return sign
        if board[1][1] == sign \
        and (board[0][0] == sign \
            and board[2][2] == sign \
            or \
            board[0][2] == sign \
            and board[2][0] == sign):
            return sign
    return False

def draw_move():
    """make computer move"""
    if len(moves["X"]) == 0:
        moves["X"].append(5)
        board[1][1] = "X"
    else:
        move = choice(make_list_of_free_fields())
        print(f"Computer chose {move}")
        moves["X"].append(move)
        board[coords[move][0]][coords[move][1]] = "X"
    display_board()

display_board()
game_winner = False
while not game_winner:
    for move in [draw_move, enter_move]:
        move()
        game_winner = victory()
        if game_winner or len(make_list_of_free_fields()) == 0:
            if game_winner:
                print(f"{game_winner} wins!")
            else:
                print("Nobody Won!")
                game_winner = True # to prevent looping more
            break
    