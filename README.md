# TIC-TAC-TERMINAL

![intro image](images/intro.PNG)

TIC-TAC-TERMINAL is a Python terminal game which runs in the Code Institue mock terminal on Heroku.

The player can try to beat the computer by taking turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a diagonal, horizontal, or vertical row is the winner.

[Click here to view the live project.](https://tictacterminal.herokuapp.com "Heroku App")

## How to play
 
* On your turn you can pick an empty spot on the grid using your num pad.
* The computer will then select a spot.
* The player who first marks 3 diagonal, horizontal, or vertical spots is the winner.
* If all spots on the board are filled then the game is a draw.

## Features

### Existing Features

* Random decision on how goes first.
    At the start of each game, the computer randomly decides who goes first and then announces it. 

![random decider image](images/random.PNG)

* Ability to play against the computer.

![computers turn image](images/computerturn.PNG)

* The grid is drawn and updated during each turn. 

* Askes for user input

* Validates user input and raises exceptions if not a blank space on the board.

![user validation image](images/exceptions.PNG)

* Option of a rematch once a game is over. 

![random image](images/rematch.PNG)

### Future Features

* Give option for player v player games
* Give different difficulty options for the computer

## Testing

I have tested the code by doing the following:

* Manually entered invalid values when asked for an input to check exceptions.
* Passed Python code through the PEP8 checker and confirmed there was no issues.
* Play tested on both the gitpod and Heroku terminal. 

### Bugs

#### Resolved Bugs

* I found that the computers position would not appear on the board sometimes which was due to me providing the randint with the range (1, 10). As the second number is inclusive this meant that the computer was to select a position off the board. 

* My Wincheck Def was not updating the winner variable, this was due to me forgetting to include global keyword within the def. 

#### Remaining Bugs

* There are no remaining bugs.

#### Validator Testing

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

* Steps for deployment:
  - Fork or clone this repository.
  - Create a new Heroku app.
  - Set the buildbacks to Python and NodeJS in that order.
  - Link the Heroku App to the repository.
  - Click on Deploy.

## Credits

* Code institute for the deployment terminal.
* My mentor, Daisy McGirr for her guidance on this project. 