def new_board():
    return [
    [None, None, None],
    [None, None, None],
    [None, None, None],
] 

def render(board):
    print('   0 1 2')
    print('  +------+')
    for idx, row in enumerate(board):
        print(idx,'|', end='')
        for cell in row:
            if cell is None:
                print('  ',end='')
            else:
                print(cell + ' ', end='')
        print('|')
    print('  +------+')

def is_valid_move(board, coord):
    if any(n > 2 for n in coord):
        return False
    elif len(coord)!= 2:
        return False
    return board[coord[0]][coord[1]] is None

def get_move():
    user_input = input("What is your moves X and Y coordinates? (Space separated)\n")
    coord = tuple(int(x) for x in user_input.split(' '))
    return coord

def get_valid_move(board):
    while True:
        coord = get_move()
        if is_valid_move(board, coord):
            return coord
        else:
            print("Invalid move, try again") 

def make_move(board, coord, player):
    if board[coord[0]][coord[1]] is not None:
        raise ValueError("Square is already taken!")
    else:
        board[coord[0]][coord[1]] = player
    return board

def get_winner(board):
    all_horizontal_lines = board
    all_vertical_lines = [[x[col] for x in all_horizontal_lines] for col in range(3)]
    left_diagonal_line = [all_horizontal_lines[i][i] for i in range(3)]
    right_diagonal_line = [all_horizontal_lines[i][i] for i in range(-1,-4,-1)]
    print(list(range(-1,-4,-1)))
    print(left_diagonal_line)
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return None

def play_game():
    players = ['X', 'O']
    turn_number = 0
    board = new_board()
    while True:
        current_player = players[(turn_number+1)%2]
        render(board)
        print('Player ', current_player, ' turn to play.')
        coord = get_valid_move(board)
        print(current_player)
        board = make_move(board, coord, player=current_player)
        turn_number += 1
        

board_1 = [
  ['X', 'X', 'O'],
  ['O', 'X', None],
  ['O', 'O', 'X']
]
get_winner(board_1)
#play_game()