# The 9 by 9 sudoku board
sudoku_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_board(board):
    """
    This will print the whole sudoku board
    :param board: The actual board
    :return: print the board
    """

    # len(board) = 9
    # this prints the horizontal line after every three rows
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        # this prints the vertical line after every three columns
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            # from 0 to 8 total is 9
            # here we actually print the numbers in board
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# print_board(board)

def find_empty(board):
    """
    This function finds the empty spaces, which we represented with 0
    :param board: The actual sudoku board
    :return: the empty spaces
    """

    # starting from [0][0], finds the place where the number is zero
    for i in range(len(board)):
        # b[0] means the length of each row
        for j in range(len(board[0])):
            if board[i][j] == 0:
                # this is the position for the next valid() method
                return i, j  # row and col,
    return None


def valid(board, number, position):
    """
    This function checks, if the number inserted is valid or not
    according to the empty spaces, that we represented as 0.
    Actually this is the main algorithm that uses the backtracking
    technique, which is, when it places a number and go forward and it
    check that if the next is not corrected it checks it again with
    the number it places lastly.
    :param board: the sudoku board
    :param number: the inserted inserted
    :param position: the empty space's position we've returned from find_empty() method
    :return: Whether the position for the number is valid or not
    """

    # check row, i is representing the rows
    for i in range(len(board)):
        # if the board at this place equals the number
        # which comes from the solve method
        if board[position[0]][i] == number and position[1] != i:
            return False

    # check columns, j is representing the columns
    for j in range(len(board)):
        # if the board at this place equals the number
        # which comes from the solve method
        if board[j][position[1]] == number and position[0] != j:
            return False

    # check the box now
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    return True


def solve(board):
    """
    This function makes sure that if the number is valid,
    it will place that number in correct position and if
    it finds that the place is not valid or say the number is
    places incorrectly it'll make that place again to zero.
    :param board: the sudoku board
    :return: the board with the numbers it places which
    is the i of the loop or make it again zero if it
    finds that the number is not valid
    """
    # print(board)
    find = find_empty(board=board)
    if not find:
        # if there is no empty spaces return true
        return True
    else:
        row, col = find

    # from 1 to 10 total range is 9
    for i in range(1, 10):
        if valid(board=board, number=i, position=(row, col)):
            board[row][col] = i

            if solve(board=board):
                return True

            board[row][col] = 0

    return False


print_board(board=sudoku_board)
solve(board=sudoku_board)

print("\n-----After Solving-----")

print_board(board=sudoku_board)
