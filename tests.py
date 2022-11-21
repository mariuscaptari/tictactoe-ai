from game import get_winner

if __name__ == '__main__':
    board_1 = [
        ['X', 'X', 'O'],
        ['O', 'X', None],
        ['O', 'O', 'X']
    ]
    tested_winner = get_winner(board_1)
    expected_winner = 'X'
    assert tested_winner == expected_winner, f"Expected {expected_winner} got: {tested_winner}"

    board_2 = [
        ['O', 'X', 'O'],
        ['O', 'X', None],
        ['O', 'O', 'X']
    ]
    tested_winner = get_winner(board_2)
    expected_winner = 'O'
    assert tested_winner == expected_winner, f"Expected {expected_winner} got: {tested_winner}"

    board_3 = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ] 
    tested_winner = get_winner(board_3)
    expected_winner = None
    assert tested_winner == expected_winner, f"Expected {expected_winner} got: {tested_winner}"

    print("All tests passed!")

