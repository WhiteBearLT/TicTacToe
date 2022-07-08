import random


def draw_board(board):
    """Drawing a game field"""
    print(board[6], '|', board[7], '|', board[8])
    print('——+———+——')
    print(board[3], '|', board[4], '|', board[5])
    print('——+———+——')
    print(board[0], '|', board[1], '|', board[2])


def input_player_letter():
    """Player chose his later"""
    letter = None

    while not (letter == 'X' or letter == 'O'):
        letter = input('Choose X or O? ').upper()

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
    return (  # !!!
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
    get_move = True
    while get_move:
        move = int(input('Make your move (0 - 8) '))
        if is_space_free(board, move):  # and move in '0 1 2 3 4 5 6 7 8'. split():
            if move in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                get_move = False
                return move
            else:
                get_move = True
        else:
            get_move = True

    # move = ' '
    # while move not in '0 1 2 3 4 5 6 7 8'.split() or not is_space_free(board, move):
    #     move = int(input('Make your move (0 - 8) '))
    #     return move


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


def get_machine_move(board, machine_letter, player_letter):
    """computer moves"""
    for i in range(9):
        board_copy = get_copy_board(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, machine_letter, i)
            if is_winner(board_copy, machine_letter):
                return i

    for i in range(9):
        board_copy = get_copy_board(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, player_letter, i)
            if is_winner(board_copy, player_letter):
                return i

    """try claim corner"""
    move = chose_random_move(board, [0, 2, 6, 8])
    if move is not None:
        return move

    """try claim center"""
    if is_space_free(board, 4):
        return 4

    """try make move by side"""
    return chose_random_move(board, [1, 3, 5, 7])


def is_board_full(board):
    """return True, if field full"""
    for i in range(1, 10):
        if is_space_free(board, i):
            return False


if __name__ == '__main__':
    print('Game: "TicTacToe"')

    game_is_playing = True
    while game_is_playing:
        """restart game field"""
        the_board = [' '] * 9
        player_letter, machine_letter = input_player_letter()
        turn = who_starts_first()
        print(turn, 'start first.')

        while game_is_playing:
            if turn == 'Human':
                """players turn"""
                draw_board(the_board)
                player_move = get_player_move(the_board)
                make_move(the_board, player_letter, player_move)

                if is_winner(the_board, player_letter):
                    draw_board(the_board)
                    print('You win!')
                    game_is_playing = False
                else:
                    if is_board_full(the_board):
                        draw_board(the_board)
                        print('Draw!')
                        game_is_playing = False
                    else:
                        turn = 'Machine'
            else:
                """computers turn"""
                move = get_machine_move(the_board, machine_letter, player_letter)
                make_move(the_board, machine_letter, move)

                if is_winner(the_board, machine_letter):
                    draw_board(the_board)
                    print('Machine is win! You lost!')
                    game_is_playing = False
                else:
                    if is_board_full(the_board):
                        draw_board(the_board)
                        print('Draw!')
                        game_is_playing = False
                    else:
                        turn = 'Human'

        if not input('Play again? (yes or no) ').lower().startswith('y'):
            print('Bye!')
            game_is_playing = False
