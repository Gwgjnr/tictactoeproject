'''
    # Horizontal checks
    if(board[1] == 'X' and board[2] == 'X' and board[3] == ' '):
        board[3] == 'Y'
    elif(board[1] == 'X' and board[3] == 'X' and board[2] == ' '):
        board[2] == 'Y'
    elif(board[2] == 'X' and board[3] == 'X' and board[1] == ' '):
        board[1] == 'Y'
    elif(board[4] == 'X' and board[5] == 'X' and board[6] == ' '):
        board[6] == 'Y'
    elif(board[4] == 'X' and board[6] == 'X' and board[5] == ' '):
        board[5] == 'Y'
    elif(board[5] == 'X' and board[6] == 'X' and board[4] == ' '):
        board[4] == 'Y'
    elif(board[7] == 'X' and board[8] == 'X' and board[9] == ' '):
        board[9] == 'Y'
    elif(board[7] == 'X' and board[9] == 'X' and board[8] == ' '):
        board[8] == 'Y'
    elif(board[8] == 'X' and board[9] == 'X' and board[7] == ' '):
        board[7] == 'Y'
    # Vertical checks
    elif(board[1] == 'X' and board[4] == 'X' and board[7] == ' '):
        board[7] == 'Y'
    elif(board[1] == 'X' and board[7] == 'X' and board[4] == ' '):
        board[4] == 'Y'
    elif(board[4] == 'X' and board[7] == 'X' and board[1] == ' '):
        board[1] == 'Y'
    elif(board[2] == 'X' and board[5] == 'X' and board[8] == ' '):
        board[8] == 'Y'
    elif(board[2] == 'X' and board[8] == 'X' and board[5] == ' '):
        board[5] == 'Y'
    elif(board[5] == 'X' and board[8] == 'X' and board[2] == ' '):
        board[2] == 'Y'
    elif(board[3] == 'X' and board[6] == 'X' and board[9] == ' '):
        board[9] == 'Y'
    elif(board[3] == 'X' and board[9] == 'X' and board[6] == ' '):
        board[6] == 'Y'
    elif(board[6] == 'X' and board[9] == 'X' and board[3] == ' '):
        board[3] == 'Y'
    # Diagonal checks
    elif(board[1] == 'X' and board[5] == 'X' and board[9] == ' '):
        board[9] == 'Y'
    elif(board[1] == 'X' and board[9] == 'X' and board[5] == ' '):
        board[5] == 'Y'
    elif(board[5] == 'X' and board[9] == 'X' and board[1] == ' '):
        board[1] == 'Y'
    elif(board[7] == 'X' and board[5] == 'X' and board[3] == ' '):
        board[3] == 'Y'
    elif(board[7] == 'X' and board[3] == 'X' and board[5] == ' '):
        board[5] == 'Y'
    elif(board[5] == 'X' and board[3] == 'X' and board[7] == ' '):
        board[7] == 'Y'
    else:
        while True:
            selection = random.randint(1, 9)
            if board[selection] == "X" or board[selection] == "O":
                continue
            else:
                print(' ')
                board[selection] = "O"
                drawBoard()
                checkWin()
                rematch()
                playerTurn()
'''
