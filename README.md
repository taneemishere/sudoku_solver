
# Sudoku Solver
Sudoku Solve is the 9 x 9, Sudoku Board solver that do solves it by using the backtracking technique. 
## Requirment
Install [Python](http://www.python.org/) - and boom you be get to go.
## The Flow
- At first we initliaze the Sudoku 9x9 board. 
```def print_board(board)``` 
This method is used to print the whole board in a way that after every three row it draws a line and same after every three column it draws a vertical line.

- ```def find_empty(board):```  
This method does find the empty spaces in the board that is represented by 0s in the program.

- ```def valid(board, number, position):```
This method is the main backtracking technique algorithm that checks, if the number inserted is valid or not according to the empty spaces, that we represented as 0. The inserted value is checked with the values inserted previously and if the value is placed correctly it passes and if not it backtracks and return false.

- ```def solve(board):``` 
This method is making sure that if the number is valid from the valid() method, it places that number in correct position and if it finds that the place is not valid, from the valid() or say the number is places incorrectly it'll replaces that specific position with zero, which again means that the space or position is empty.
