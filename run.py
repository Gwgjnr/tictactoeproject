# import random function for game
# ask for name
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def startGame():
    print(f'welcome to TICTACTOE!\n')
    name = input("Please enter your name: ")
    print(f'Thanks, {name}\n')
    print(f'{name} [X] --- Computer [O]\n')
    drawBoard()


def drawBoard():
    print(f' {board[0]}| {board[1]}| {board[2]}')
    print("--+--+--")
    print(f' {board[3]}| {board[4]}| {board[5]}')
    print("--+--+--")
    print(f' {board[6]}| {board[7]}| {board[8]}')



# def for deciding who goes first
# ask for position (add exceptions for invalid input)
# draw computor position
# def for drawing grid
# add elif for win conditions
# add def to check if its a draw if board is full
# declare winner and ask if they wany to play again


startGame()
