import sys
import itertools as IT

"""Method which determines whether a player has won horizontally. Uses the connectZ board, now
filled in with the game as each turn is made. Also uses turns_taken to save running the 
for loop in cases where a game could not possibly have been won yet"""


def horizontal_winner(connect_board, winning_target):
    height = len(connect_board) - 1
    width = len(connect_board[0])
    for row in range(height, 0, -1):
        horizontal_array = []
        for col in range(width):
            if horizontal_array.__len__() == 0:
                horizontal_array.append(connect_board[row][col])
            elif connect_board[row][col] == connect_board[row][col - 1]:
                # print('col + col-1: ', connect_board[row][col], connect_board[row][col - 1], connect_board[row])
                horizontal_array.append(connect_board[row][col])
                # print('horizontal array: ', horizontal_array)
                # print('array element count: ', horizontal_array.count(1))
                if horizontal_array.count(1) == winning_target or horizontal_array.count(2) == winning_target:
                    # print('horizontal winner found')
                    return True
            else:
                horizontal_array = [connect_board[row][col]]
                # print('horizontal array cleared: ', horizontal_array)


"""Method which determines whether a player has won vertically. Uses the connectZ board, now
filled in with the game as each turn is made. Also uses turns_taken to save running the 
for loop in cases where a game could not possibly have been won yet"""


def vertical_winner(connect_board, winning_target):
    height = len(connect_board)
    width = len(connect_board[0]) - 1
    for row in range(height):
        vertical_array = []
        for col in range(width - 1, -1, -1):

            if col < height and connect_board[col][row] != 0:
                if connect_board[col][row] == connect_board[col + 1][row]:
                    vertical_array.append(connect_board[col][row])
                    # print('vertical array: ', vertical_array, 'winning target: ', winning_target)
                    if vertical_array.count(1) == winning_target or vertical_array.count(2) == winning_target:
                        # print('vertical array: ', vertical_array, 'winning target: ', winning_target)
                        # print('vertical winner found')
                        return True
                else:
                    vertical_array = [connect_board[col][row]]


"""Method which determines whether a player has won diagonally. Uses the connectZ board, now
filled in with the game as each turn is made. Method uses the iterator to check every element
in the matrix and its diagonal partner for equality, winner is found if there are equal numbers
 of diagonal matches to the winning target"""


def diagonal_winner(connect_board, winning_target):
    height = len(connect_board)
    d = dict()
    for i, j in IT.product(range(height), repeat=2):
        d.setdefault(j - i, []).append((i, j))

    diagonal_array = [[connect_board[i][j] for i, j in d[k]] for k in range(-height + 1, height)]
    print(diagonal_array)
    for i in range(len(diagonal_array)):
        if diagonal_array[i].count(1) == winning_target or diagonal_array[i].count(2) == winning_target:
            print(diagonal_array[i])
            print('Diagonal Winner found')
            return True

    # [[7], [4, 8], [1, 5, 9], [2, 6], [3]]
    # height = len(connect_board) - 1
    # width = len(connect_board[0])
    # vertical = height
    # horizontal = 0
    # all_elements = height * width
    # count = 0
    # while count < all_elements+1:
    #     vertical = height
    #     diag_array = []
    #     for hoz in range(width):
    #         print(connect_board[vertical][hoz])
    #         le = len(diag_array)
    #         if len(diag_array) != width + 1:
    #             diag_array.append(connect_board[vertical][hoz])
    #         else:
    #             diag_array = connect_board[vertical][hoz]
    #
    #         print(diag_array)
    #
    #         vertical -= 1
    #     count += 1

    # for vertical in range(height, 0, -1):
    #
    #     for horizontal in range(width):
    #         height_remainder = vertical - height
    #         width_remainder = width - horizontal

    # diagonal_array_left = [connect_board[i][i] for i in range(height), connect_board[j][j] for j in range(width)]
    # print('diagonal left: ', diagonal_array_left)
    # diagonal_array_right = [connect_board[i][height - 1 - i] for i in range(height)]
    # print('diagonal right: ', diagonal_array_right)
    # if (diagonal_array_left.count(1) == winning_target or diagonal_array_left.count(2) == winning_target) or (
    #         diagonal_array_right.count(1) == winning_target or diagonal_array_right.count(2) == winning_target):
    #     print('diagonal winner found')
    #     return True


"""Method checks if there has been a winner bu calling the vertical, horizontal and diagonal win methods. It only does this
when there have been enough turs for there to be a winner in order to improve efficiency."""


def winner(connect_board, game_dimensions, turns_taken):
    if turns_taken >= game_dimensions[2]:
        if vertical_winner(connect_board, game_dimensions[2]):
            return True
        if horizontal_winner(connect_board, game_dimensions[2]):
            return True
        if diagonal_winner(connect_board, game_dimensions[2]):
            return True
        else:
            return False


"""Simple declare winner method depending on whether player1 is true or false."""


def declare_winner(player1):
    if player1:
        print('PLayer 1 wins!', 1)
    else:
        print('Player 2 wins!', 2)


"""Method which plays out the game, checking for the *completed* game result and whether
either player has made an illegal move - by row or by column - or if they
have continued beyond a winner being crowned"""


def run_game(game_dimensions, game_outcome):
    num_of_columns = game_dimensions[0]
    for column in game_outcome:
        if num_of_columns < column:
            print('Illegal Column')
            print(6)
            return
    num_of_rows = game_dimensions[1]
    connect_board = [[0] * num_of_columns for _ in range(num_of_rows)]
    max_column_height_counter = [0] * num_of_columns
    player1 = True
    turns_taken = 0
    # print('game outcome', game_outcome)
    for turn in game_outcome:
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in connect_board]))
        turns_taken += 1
        num_of_rows = game_dimensions[1]
        turn_index = turn - 1
        row_checker = False
        while not row_checker:
            if connect_board[num_of_rows - 1][turn_index] == 0:
                if player1:
                    connect_board[num_of_rows - 1][turn_index] = 1
                    if turns_taken >= game_dimensions[2] and winner(connect_board, game_dimensions, turns_taken):
                        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in connect_board]))
                        print('Player 1 wins')
                        if len(game_outcome) != turns_taken:
                            print('game outcome: ', len(game_outcome), 'turn index: ', turns_taken)
                            print('Illegal Continue', 4)
                            return 4
                        else:
                            print(1)
                            return 1
                    player1 = False
                else:
                    connect_board[num_of_rows - 1][turn_index] = 2
                    if turns_taken >= game_dimensions[2] and winner(connect_board, game_dimensions, turns_taken):
                        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in connect_board]))
                        print('Player 2 wins')
                        if len(game_outcome) != turn_index:
                            print('Illegal Continue', 4)
                            return 4
                        else:
                            print(2)
                            return 2
                    player1 = True
                row_checker = True
            else:
                max_column_height_counter[turn - 1] = max_column_height_counter[turn - 1] + 1
                # print(game_dimensions[1])
                if max_column_height_counter[turn - 1] > game_dimensions[1]:
                    print('max column height reached', 5)
                    return 5
                num_of_rows = num_of_rows - 1
                row_checker = False
    # print('Max col counter', max_column_height_counter)
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in connect_board]))
    if not winner(connect_board, game_dimensions, turns_taken):
        print('Incomplete Game')
        return 3

"""Method reads the inputted file and extracts the data from it. Uses a try/catch (except in python) to ensure the file does not terminate
the program if not found. Calls the run_game method if it is found and it is both a legal and valid game."""

def read_file(filename):
    try:
        game_file = open(filename, 'r')
        lines = game_file.read().splitlines()
        first_line = lines[0]
        game_outcome = lines[1: lines.__len__()]
        game_dimensions = [first_line[0], first_line[2], first_line[4]]
        if not invalid_file(game_dimensions, game_outcome):
            print('Valid Game')
        else:
            print(8)
            return
        game_dimensions = integer_conversion(game_dimensions)
        game_outcome = integer_conversion(game_outcome)
        if not (illegal_game(game_dimensions)):
            # print('Legal Game')
            run_game(game_dimensions, game_outcome)
        else:
            print('illegal game', 7)
            return
    except FileNotFoundError:
        print(9)


"""To be a valid file, the inputted data must be integers and must be one number per line. This method providdes very basic parsing
of the inputted file in order to check this."""


def invalid_file(first_line_array, game_moves):
    for line in game_moves:
        if line.__contains__(' '):
            return True
        elif not is_number(line):
            return True
        elif int(line) < 0:
            return True
    if first_line_array.__len__() != 3:
        return True
    for index in first_line_array:
        if not is_number(index):
            return True
        elif int(index) < 0:
            return True


"""
 A simple function for determining whether a string is also a number.
"""


def is_number(string):
    if string.isnumeric():
        return True
    else:
        return False


"""
 A simple function for converting every element in an array from a string into
 an array of integers
"""


def integer_conversion(string_array):
    number_array = []
    for char in string_array:
        number_array.append(int(char))
    return number_array


"""
 This method checks whether the game is legal given the game dimensions - any target over the column and row length is not legal.
"""


def illegal_game(game_dimensions):
    if (game_dimensions[2] > game_dimensions[1] and game_dimensions[2] > game_dimensions[0]) or (
            game_dimensions[2] < 1 or game_dimensions[1] < 1 or game_dimensions[0] < 1):
        return True
    else:
        return False;


"""Main method which calls formats  the input parameter correctly in order to grab the filename.txt. Then
the method calls the read_file method which goes through line by line of the played connectZ board."""

if __name__ == "__main__":
    if sys.argv.__len__() == 2:
        filename = sys.argv.__getitem__(1) + '.txt'
        # print(filename)
        read_file(filename)
    else:
        sys.stdout.write('Provide one input file' + '\n')
