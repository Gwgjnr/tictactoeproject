import random
import time
import sys

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
winner = False


def startGame():
    print_slow(f'{name} [ X ] <<<--->>> Computer [ O ]\n')
    print(' ')
    drawBoard()
    randomFirstPlayer()


def drawBoard():
    print(f'{board[7]}|{board[8]}|{board[9]}')
    print("-+-+-")
    print(f'{board[4]}|{board[5]}|{board[6]}')
    print("-+-+-")
    print(f'{board[1]}|{board[2]}|{board[3]}\n')


def randomFirstPlayer():
    print_slow('Randomly deciding who goes first...\n')
    firstPlayer = random.randint(1, 2)
    if firstPlayer == 1:
        print(f'\n{name} will go first\n')
        playerTurn()
    elif firstPlayer == 2:
        print('\nThe Computer will go first\n')
        computerTurn()


def playerTurn():
    print(' ')
    pickPosition()


def computerTurn():
    print_slow("Its the computers turn\n")
    print_slow('.....\n')
    print_slow('...\n')
    print(' ')
    computerPosition()


def pickPosition():
    while True:
        try:
            selection = int(input("Please select your spot on your numpad: "))
        except ValueError:
            print("Please select a number and position using your numpad!")
            continue
        if selection not in range(1, 10):
            print("\nThe numbers must be between 1-9!")
            continue
        if board[selection] == "X" or board[selection] == "O":
            print("\nThis position is already taken!\n")
            continue
        else:
            print(' ')
            board[selection] = "X"
            drawBoard()
            checkWin()
            rematch()
            computerTurn()


def computerPosition():
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


def checkWin():
    global winner
    # Horizontal Wins
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        winner = True
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        winner = True
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        winner = True
    # Vertical Wins
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        winner = True
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        winner = True
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        winner = True
    # Diagonal Wins
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        winner = True
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        winner = True
    # Draw Game
    elif(board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and
         board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and
         board[7] != ' ' and board[8] != ' ' and board[9] != ' '):
        print('This game is a draw\n')
        rematch()
    else:
        winner = False


def rematch():
    global board
    if winner:
        print('\nGame over!\n')
        rematch = input('Would you like to play again (y/n)?')
        print(' ')
        if rematch.lower() == 'y':
            board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            randomFirstPlayer()
        if rematch.lower() == 'n':
            print('Thank you for playing my TICTACTOE game!\n')
            print('Closing programme')
            sys.exit()


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


print('welcome to TICTACTOE!\n')
name = input('Please enter your name: ')
print(' ')
print_slow(f'Hello {name}, you can pick your position using your num pad: ')
print(' ')
print(' ')
print('7|8|9')
print('-+-+-')
print('4|5|6')
print('-+-+-')
print('1|2|3\n')
startGame()
