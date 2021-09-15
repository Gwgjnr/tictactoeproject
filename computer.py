'''
    # Horizontal checks
    if(board[1] == 'X' and board[2] == 'X' and board[3] == ' '):
        board[3] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    elif(board[1] == 'X' and board[3] == 'X' and board[2] == ' '):
        board[2] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    elif(board[2] == 'X' and board[3] == 'X' and board[1] == ' '):
        board[1] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    elif(board[4] == 'X' and board[5] == 'X' and board[6] == ' '):
        board[6] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    elif(board[4] == 'X' and board[6] == 'X' and board[5] == ' '):
        board[5] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    elif(board[5] == 'X' and board[6] == 'X' and board[4] == ' '):
        board[4] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    elif(board[7] == 'X' and board[8] == 'X' and board[9] == ' '):
        board[9] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    elif(board[7] == 'X' and board[9] == 'X' and board[8] == ' '):
        board[8] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    elif(board[8] == 'X' and board[9] == 'X' and board[7] == ' '):
        board[7] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    # Vertical checks
    elif(board[1] == 'X' and board[4] == 'X' and board[7] == ' '):
        board[7] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    elif(board[1] == 'X' and board[7] == 'X' and board[4] == ' '):
        board[4] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    elif(board[4] == 'X' and board[7] == 'X' and board[1] == ' '):
        board[1] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    elif(board[2] == 'X' and board[5] == 'X' and board[8] == ' '):
        board[8] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    elif(board[2] == 'X' and board[8] == 'X' and board[5] == ' '):
        board[5] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    elif(board[5] == 'X' and board[8] == 'X' and board[2] == ' '):
        board[2] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    elif(board[3] == 'X' and board[6] == 'X' and board[9] == ' '):
        board[9] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    elif(board[3] == 'X' and board[9] == 'X' and board[6] == ' '):
        board[6] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    elif(board[6] == 'X' and board[9] == 'X' and board[3] == ' '):
        board[3] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    # Diagonal checks
    elif(board[1] == 'X' and board[5] == 'X' and board[9] == ' '):
        board[9] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    elif(board[1] == 'X' and board[9] == 'X' and board[5] == ' '):
        board[5] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    elif(board[5] == 'X' and board[9] == 'X' and board[1] == ' '):
        board[1] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    elif(board[7] == 'X' and board[5] == 'X' and board[3] == ' '):
        board[3] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    elif(board[7] == 'X' and board[3] == 'X' and board[5] == ' '):
        board[5] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
    elif(board[5] == 'X' and board[3] == 'X' and board[7] == ' '):
        board[7] == 'Y'
        drawBoard()
        checkWin()
        rematch()
        playerTurn()
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
