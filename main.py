import random


def board(board):
    """Drawing a game field"""
    print(board[7], '|', board[8], '|', board[9])
    print('-+-+-')
    print(board[4], '|', board[5], '|', board[6])
    print('-+-+-')
    print(board[1], '|', board[2], '|', board[3])


def input_player_letter():
    """Player chose his later"""
    letter = None

    while not(letter == 'X' or letter == 'O'):
        letter = input('Choose X or O?').upper()

    if letter == 'X':
        human = 'X'
        machine = 'O'
    else:
        human = 'O'
        machine = 'X'

    return human, machine


def who_starts_first():
    """Random choose, who starts first"""
    if random.randint(0, 1) == 0:
        return 'Human'
    else:
        return 'Machine'


def make_move(board, letter, move):
    """Make a move"""
    board[move] = letter


def is_winner(board, letter):
    """Checking, player win or not?"""
    return (
        (board[6] == letter and board[7] == letter and board[8] == letter) or
        (board[3] == letter and board[4] == letter and board[5] == letter) or
        (board[0] == letter and board[1] == letter and board[2] == letter) or
        (board[0] == letter and board[3] == letter and board[6] == letter) or
        (board[1] == letter and board[4] == letter and board[7] == letter) or
        (board[2] == letter and board[5] == letter and board[8] == letter) or
        (board[0] == letter and board[4] == letter and board[8] == letter) or
        (board[2] == letter and board[4] == letter and board[6] == letter)
    )


def get_copy_board(board):
    """Create board copy"""
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy


def is_space_free(board, move):
    """Return True, if space free"""
    return board[move] == ' '


def get_player_move(board):
    """Player moves"""
    move = None
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, move):
        move = int(input('Make your move (1 - 9)'))


def chose_random_move(board, moves_list):
    """Return move"""
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None
