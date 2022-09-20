import copy
import random

# the user must set before the game.
SIZE = 6  # The length of a winning sequence
RANGE = 3  # the range of the numbers on the board

# game parameters
VIC = 10 ** 20  # The value of a winning board (for max)
LOSS = -VIC  # The value of a losing board (for max)
TIE = 0  # The value of a tie
VOID_VALUE = RANGE + 10
COMPUTER = 0  # Marks the computer's cells on the board
HUMAN = 1  # Marks the human's cells on the board

# presentation parameters:
VOID_REPLACEMENT = '*'
SPACES_IN_TABLE = 4


def create():
    """
    creates the initial state of the game.
    the state in made of 6 parts:
    0: the board, contains the board numbers.
    1: the human score, the sum of all the points the human collected by now.
    2: the computer score, the sum of all the points the automatic player collected by now.
    3: how's turn is it.
    4, 5: the place on the board.
    :return: the initial state.
    """
    # Returns an empty board. The human plays first.
    board = []
    for i in range(SIZE):
        board = board + [[random.randint(-RANGE, RANGE) for j in range(SIZE)]]
    return [board, 0, 0, HUMAN, random.randint(0, SIZE - 1), random.randint(0, SIZE - 1)]


def value(s):
    """
    :param s: the state
    :return: the heuristic value.
    """
    return s[2] - s[1]


def printState(s):
    """
    prints the state.
    :param s: the state.
    """
    print("\n\ncurrent location: " + str(s[4]) + " , " + str(s[5]) + ", Human Score: " + str(s[1]) + ", Comp score: " +
          str(s[2]) + "\n")

    print((SPACES_IN_TABLE - 2) * ' ', end="")
    for i in range(SIZE):
        print(str(i) + (SPACES_IN_TABLE - len(str(i))) * ' ', end="")
    print("<- for the input")

    # Prints the board. The empty cells are printed as ' '
    # If the game ended prints who won.
    for r in range(len(s[0])):
        for c in range(len(s[0][0])):
            if r == s[4]:
                print('\x1b[6;30;42m' + (
                    (SPACES_IN_TABLE - len(str(s[0][r][c]))) * " " if c != 0 else "->" + (
                            SPACES_IN_TABLE - 2 - len(str(s[0][r][c]))) * " ") + (
                          str(s[0][r][c]) if s[0][r][c] != VOID_VALUE else VOID_REPLACEMENT * len(
                              str(VOID_VALUE))) + '\x1b[0m', end="")
            else:
                print((4 - len(str(s[0][r][c]))) * " " + (
                    str(s[0][r][c]) if s[0][r][c] != VOID_VALUE else VOID_REPLACEMENT * len(str(VOID_VALUE))), end="")
        print()

    if isFinished(s):
        if s[1] > s[2]:
            print("\nYOU WIN!!")
        elif s[1] < s[2]:
            print("\nYOU LOSE!!")
        else:
            print("\nIT'S A TIE")


def isFinished(s):
    """
    true if the game is finished, means there are no more options to play.
    :param s:
    :return:
    """
    flag = True

    if s[3] == HUMAN:
        for i in range(SIZE):
            if s[0][s[4]][i] != VOID_VALUE:
                flag = False
        return flag
    else:
        for i in range(SIZE):
            if s[0][i][s[5]] != VOID_VALUE:
                flag = False
        return flag


def isHumTurn(s):
    """
    :param s: the state
    :return: true is this is the human turn to play.
    """
    return s[3] == HUMAN


def whoIsFirst(s):
    """
    finds out how is the first player according to the player preference.
    :param s: the initial state.
    """
    if int(input("Who plays first? 1-me / anything else-you. : ")) == 1:
        s[3] = COMPUTER
    else:
        s[3] = HUMAN


def makeMove(s, r, c):
    """
    update the state with the correct data after making a move.
    :param s: the state.
    :param r: the coordinates that the move is to, assumes the move is legal.
    :param c:
    """
    if s[3] == HUMAN:
        s[1] += s[0][r][c]
    else:
        s[2] += s[0][r][c]

    s[3] = COMPUTER + HUMAN - s[3]  # switches turns

    s[4] = r  # upsates the location on the board.
    s[5] = c

    s[0][r][c] = VOID_VALUE  # marks the board taken value to the VOID_VALUE.


def inputMove(s):
    """
    asking the player to enter a move in his turn.
    the function also makes sure that the move inserted by the player is legal.
    :param s: the state the player is asked to insert to.
    """
    printState(s)
    flag = True
    while flag:
        move = int(input("Enter your column number: "))
        c = move
        if c < 0 or c >= SIZE or s[0][s[4]][c] == VOID_VALUE:
            print("Illegal move.")
        else:
            flag = False
            makeMove(s, s[4], c)


def getNext(s):
    """
    returns a list with all the next places available for the player.
    :param s: the state
    :return: the list with all the available options for the player to do.
    """
    ns = []

    if s[3] == COMPUTER:
        for i in range(SIZE):
            # if this is the computers turn we look for the options on the column of the current state.
            if s[0][i][s[5]] != VOID_VALUE:
                tmp = copy.deepcopy(s)
                makeMove(tmp, i, s[5])
                ns += [tmp]
    else:
        for i in range(SIZE):
            # if this is the human turn we look for the options on the row of the current state.
            if s[0][s[4]][i] != VOID_VALUE:
                tmp = copy.deepcopy(s)
                makeMove(tmp, s[4], i)
                ns += [tmp]

    return ns
