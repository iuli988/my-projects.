def paralel(board1, board2):
    # return f'{board1}' + ' ' + f'{board2}'
    for i in range(len(board1)):
        line = str(board1[i]) + '---------------' + str(board2[i])
        print(line)


paralel([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
