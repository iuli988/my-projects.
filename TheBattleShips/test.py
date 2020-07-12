import random


def get_board(size):
    board = []
    # if size > 5 and size < 10:
    for i in range(size):
        board.append([])
        for j in range(size):
            board[i].append('0')
    # elif size > 10 or size < 5:
    #     print('Sorry you must enter a size between 5 and 10')
    return board


def random_row(board):
    return random.randint(0, len(board)-1)


def random_col(board):
    return random.randint(0, len(board[0])-1)


board = get_board(5)
x = (random_row(board), random_col(board))
y = tuple(x)

if board[[y[0]][y[1]]] == '0':
    board[[y[0]][y[1]]] = 'X'
print(board)
