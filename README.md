# TIC-TAC-TERMINAL

![intro image](images/intro.PNG)

TIC-TAC-TERMINAL is a Python terminal game which runs in the Code Institue mock terminal on Heroku.

The player can try to beat the computer by taking turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a diagonal, horizontal, or vertical row is the winner.

[Click here to view the live project.](https://tictacterminal.herokuapp.com "Heroku App")

## How to play
 
* On your turn you can pick an empty spot on the grid using your num pad.
* The computer will then select an available spot.
* The player who first marks 3 diagonal, horizontal, or vertical spots is the winner.
* If all spots on the board are filled without 3 in a row then the game is a draw.

## Features

### Existing Features

* Random decision on who goes first.
    At the start of each game, the computer randomly decides who goes first using the random module and then announces it. 

![random decider image](images/random.PNG)

* Ability to play against the computer.

![computers turn image](images/computerturn.PNG)

* The grid is drawn and updated during each turn. 

* Askes for user input.

* Validates user input and raises exceptions if not a blank space on the board.

![user validation image](images/exceptions.PNG)

* Option of a rematch once a game is over. 

![random image](images/rematch.PNG)

### Future Features

* Give option for player v player games
* Give different difficulty options for the computer

## Testing

I have tested the code by doing the following:

### User Input Testing

![user testing image](images/userinputtesting.PNG)

* [Passed Python code through the PEP8 checker and confirmed there was no issues.](images/PEP8.PNG)

* Play tested on both the gitpod and Heroku terminal. 

### Bugs

#### Resolved Bugs

* I found that the computers position would not appear on the board sometimes which was due to my error in providing the randint with the range (1, 10). As the second number is inclusive this meant that the computer was to select a position off the board. 

* My Wincheck Def was not updating the winner variable, this was due to my error in not including the global keyword within the function. 

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

### Making a clone or download zip to run locally

1. Log into GitHub account.

2. Select repository.

3. Select TICTACTOEPROJECT.

4. Click on the Code dropdown button next to the green Gitpod button.

5. Click on the clipboard icon to copy the clone URL.

6. Open Git Bash.

7. Change the current working directory to the location where you want the cloned directory.

8. Type "git clone" in the Command Line and then paste the URL copied in step 5.

9. Press enter to create your local clone.

10. Alternately, click on Download ZIP, unpack locally and open with a local code editor.

### Forking the GitHub Repository

1. Log into GitHub.

2. Select repository.

3. Select TICTACTOEPROJECT.

4. At the very top right corner click "fork".

5. You will have a copy of the original repository in your own GitHub account.

## Credits

* Wikipedia for the information on Tic-Tac-Toe.
* Code institute for the deployment terminal.
* My mentor, Daisy McGirr for her guidance on this project. 