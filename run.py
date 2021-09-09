import random
import time
import sys

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
winner = False


def startGame():
    print_slow(f'{name} [X] --- Computer [O]\n')
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
    firstPlayer = random.randint(1, 2)
    if firstPlayer == 1:
        print(f'{name} will go first\n')
        playerTurn()
    elif firstPlayer == 2:
        print('Computer will go first\n')
        computerTurn()


def playerTurn():
    selection = int(input("Please select your position using your numpad: "))
    print(' ')
    board[selection] = "X"
    drawBoard()
    computerTurn()


def computerTurn():
    print_slow("Its the computers turn\n")
    print_slow('.....\n')
    print_slow('...\n')
    print(' ')
    selection = random.randint(0, 8)
    board[selection] = "O"
    drawBoard()
    playerTurn()


def checkWin():
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
    else:
        winner = False


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
# ask for position (add exceptions for invalid input)
# add elif for win conditions
# add def to check if its a draw if board is full
# declare winner and ask if they wany to play again


print('welcome to TICTACTOE!\n')
name = input('Please enter your name: ')
print(' ')
print_slow(f'Welcome {name}, you can pick your position using your num pad: ')
print(' ')
print(' ')
print('7|8|9')
print('-+-+-')
print('4|5|6')
print('-+-+-')
print('1|2|3\n')
startGame()
