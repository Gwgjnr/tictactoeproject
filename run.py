import random
import time
import sys
from colorama import Fore, Style, init
init(autoreset=True)

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
winner = False


def getName():
    """
    Checks that name inputted is valid and not empty by ensuring
    all characters are alphabetic.
    """
    global name
    while True:
        name = input("Please enter your name:\n")
        if name.isalpha():
            break
        else:
            print("Please enter a valid name.\n")
            continue


def startGame():
    """
    Shows the player what mark they will be using and calls the
    randomFirstPlayer function.
    """
    print_slow(f'{name} [ X ] <<<--->>> Computer [ O ]\n')
    print(' ')
    drawBoard()
    randomFirstPlayer()


def drawBoard():
    """
    Creates the board layout and can be called during turns to
    display updated positions.
    """
    print(f' {board[7]}|{board[8]}|{board[9]}')
    print(" -+-+-")
    print(f' {board[4]}|{board[5]}|{board[6]}')
    print(" -+-+-")
    print(f' {board[1]}|{board[2]}|{board[3]}\n')


def randomFirstPlayer():
    """
    Uses the random module to decide which player will go first
    at the start of each game and then calls that player's turn
    """
    print_slow('Randomly deciding who goes first...\n')
    firstPlayer = random.randint(1, 2)
    if firstPlayer == 1:
        print(f'\n{name} will go first\n')
        playerTurn()
    elif firstPlayer == 2:
        print('\nThe Computer will go first\n')
        computerTurn()


def playerTurn():
    """
    Allows player to select a valid position on the board by passing input
    through exception and validation. Then calls for the board to be displayed,
    checks for win/draw and passes back to computer if false.
    """
    print(f"Its {name}'s turn\n")
    while True:
        try:
            selection = int(input("Please select your spot on the numpad:\n"))
        except ValueError:
            print("\nPlease select a number and position using your numpad\n")
            continue
        if selection not in range(1, 10):
            print("\nThe number must be between 1-9\n")
            continue
        if board[selection] == "X" or board[selection] == "O":
            print("\nThis position is already taken\n")
            continue
        else:
            print(' ')
            board[selection] = "X"
            drawBoard()
            checkWin()
            rematch()
            computerTurn()


def computerTurn():
    """
    Announced the computers turn before selecting an empty spot using
    the random module. Then calls for the board to be displayed, checks for
    win/draw and passes back to player if false.
    """
    print_slow("Its the computers turn\n")
    print_slow('.....\n')
    print_slow('...\n')
    print(' ')
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
    """
    Checks the position of the marks on the board after each player selects
    a position to check if there is a winner. Changes the value of the
    global variable to True if a condition is met.
    """
    global winner
    # Horizontal Wins
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        winner = True
        if board[1] == 'X':
            print('Congratulations, you won!\n')
        else:
            print('Hard luck, you lost.')
        board[1] = Fore.RED + board[1] + Style.RESET_ALL
        board[2] = Fore.RED + board[2] + Style.RESET_ALL
        board[3] = Fore.RED + board[3] + Style.RESET_ALL
        drawBoard()
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        winner = True

        if board[4] == 'X':
            print('Congratulations, you won!\n')
        else:
            print('Hard luck, you lost.\n')
        board[4] = Fore.RED + board[4] + Style.RESET_ALL
        board[5] = Fore.RED + board[5] + Style.RESET_ALL
        board[6] = Fore.RED + board[6] + Style.RESET_ALL
        drawBoard()
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        winner = True
        if board[7] == 'X':
            print('Congratulations, you won!\n')
        else:
            print('Hard luck, you lost.\n')
        board[7] = Fore.RED + board[7] + Style.RESET_ALL
        board[8] = Fore.RED + board[8] + Style.RESET_ALL
        board[9] = Fore.RED + board[9] + Style.RESET_ALL
        drawBoard()
    # Vertical Wins
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        winner = True
        if board[1] == 'X':
            print('Congratulations, you won!\n')
        else:
            print('Hard luck, you lost.\n')
        board[1] = Fore.RED + board[1] + Style.RESET_ALL
        board[4] = Fore.RED + board[4] + Style.RESET_ALL
        board[7] = Fore.RED + board[7] + Style.RESET_ALL
        drawBoard()
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        winner = True
        if board[2] == 'X':
            print('Congratulations, you won!\n')
        else:
            print('Hard luck, you lost.\n')
        board[2] = Fore.RED + board[2] + Style.RESET_ALL
        board[5] = Fore.RED + board[5] + Style.RESET_ALL
        board[8] = Fore.RED + board[8] + Style.RESET_ALL
        drawBoard()
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        winner = True
        if board[3] == 'X':
            print('Congratulations, you won!\n')
        else:
            print('Hard luck, you lost.\n')
        board[3] = Fore.RED + board[3] + Style.RESET_ALL
        board[6] = Fore.RED + board[6] + Style.RESET_ALL
        board[9] = Fore.RED + board[9] + Style.RESET_ALL
        drawBoard()
    # Diagonal Wins
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        winner = True
        if board[1] == 'X':
            print('Congratulations, you won!\n')
        else:
            print('Hard luck, you lost.\n')
        board[1] = Fore.RED + board[1] + Style.RESET_ALL
        board[5] = Fore.RED + board[5] + Style.RESET_ALL
        board[9] = Fore.RED + board[9] + Style.RESET_ALL
        drawBoard()
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        winner = True
        if board[3] == 'X':
            print('Congratulations, you won!\n')
        else:
            print('Hard luck, you lost.\n')
        board[3] = Fore.RED + board[3] + Style.RESET_ALL
        board[5] = Fore.RED + board[5] + Style.RESET_ALL
        board[7] = Fore.RED + board[7] + Style.RESET_ALL
        drawBoard()
    # Draw Game
    elif(board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and
         board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and
         board[7] != ' ' and board[8] != ' ' and board[9] != ' '):
        print('This game is a draw\n')
        rematch()
    else:
        winner = False


def rematch():
    """
    Checks each turn if the variable winner has been updated to True and then
    offers a new game. Validates to ensure input is either y or n.
    """
    global board
    if winner:
        replay = input('Would you like to play again (y/n)?\n')
        print(' ')
        while True:
            if replay.lower() == 'y':
                board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                randomFirstPlayer()
            if replay.lower() == 'n':
                print('Thank you for playing my TICTACTOE game!\n')
                print('Closing programme')
                sys.exit()
            else:
                print('Please choose y or n\n')
                rematch()


def print_slow(str):
    """
    Print statements are displayed slowly as though they were being typed.
    This allows the player time to read the instructions. Created from
    example: https://www.codegrepper.com/code-examples/python/python+slow+print
    """
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


print('----------------------------')
print(Fore.GREEN + 'Welcome to TIC-TAC-TERMINAL!')
print('----------------------------\n')
getName()
print(' ')
print_slow(f'Hello {name}, you can pick your position using your num pad: ')
print(' ')
print(' ')
print(' 7|8|9')
print(' -+-+-')
print(' 4|5|6')
print(' -+-+-')
print(' 1|2|3\n')
startGame()
