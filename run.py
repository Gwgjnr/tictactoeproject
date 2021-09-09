import random
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def startGame():
    print(f'{name} [X] --- Computer [O]\n')
    drawBoard()
    randomFirstPlayer()


def drawBoard():
    print(f'{board[7]}|{board[8]}|{board[9]}')
    print("-+-+-")
    print(f'{board[4]}|{board[5]}|{board[6]}')
    print("-+-+-")
    print(f'{board[1]}|{board[2]}|{board[3]}\n')


def randomFirstPlayer():
    firstPlayer = random.randint(1, 2)
    if firstPlayer == 1:
        print(f'{name} will go first\n')
        playerTurn()
    elif firstPlayer == 2:
        print('Computer will go first\n')
        computerTurn()


def playerTurn():
    selection = int(input("Please select your position using your numpad: "))
    board[selection] = "X"
    drawBoard()
    computerTurn()


def computerTurn():
    print('Computers turn...\n')
    print('.....\n')
    print('...\n')
    selection = random.randint(0, 8)
    board[selection] = "O"
    drawBoard()
    playerTurn()

# ask for position (add exceptions for invalid input)
# add elif for win conditions
# add def to check if its a draw if board is full
# declare winner and ask if they wany to play again


print('welcome to TICTACTOE!\n')
name = input('Please enter your name: \n')
print(f'Welcome {name}, you can pick your position using your number pad\n')
print('7|8|9')
print('-+-+-')
print('4|5|6')
print('-+-+-')
print('1|2|3\n')
startGame()
