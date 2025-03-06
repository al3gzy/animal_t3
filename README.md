# Harary's Generalised Tic-Tac-Toe / Code breakdown

This Python code defines a game of **Animal Tic-Tac-Toe**, which is a variant of the traditional Tic-Tac-Toe game, incorporating the concept of polyominoes (shapes made of connected cells, representing animals). The game is played on a square grid, where two players take turns marking cells with their respective symbols (1 and -1), and the objective is to form a specified "animal shape" (a set of cells) on the board.

The game also uses a technique from **Dancing Links** to efficiently solve for winning configurations. Below is a breakdown of the key components:

## AnimalTicTacToe Class
   - **`__init__()`**: Initializes the game, setting up the board and defining the current player.
   - **`create_board(board_size)`**: Creates an empty board of the given size using `numpy`.
   - **`print_board()`**: Prints the current state of the board in a user-friendly format.
   - **`check_winner(board, animal_shape, player_mark)`**: Checks if the current player has won by matching the given animal shape on the board using **Dancing Links** to solve the polyomino placement.
   - **`play_game()`**: Main game loop where players input their moves. The game alternates between two players (player 1 and player -1) and checks if there's a winner or a tie after every move.

## DancingLinks Class
   This class implements the **Dancing Links** algorithm, which is a highly efficient way to solve exact cover problems (like the polyomino placement problem here). The algorithm is based on a matrix representation of the problem and uses a structure of **linked nodes** to represent the rows and columns of the matrix.

   - **`Node` class**: Represents a node in the doubly linked list used in the Dancing Links algorithm. Each node contains links to its left, right, up, and down neighbors, as well as its column name and row.
   - **`create_grid(matrix)`**: Creates the grid from the matrix, setting up the linked list structure for the Dancing Links algorithm.
   - **`cover(column)`**: Temporarily removes a column and its corresponding rows from the grid to simulate the "covering" of a column during the search.
   - **`uncover(column)`**: Restores a previously covered column and its rows, effectively undoing the covering.
   - **`search(k=0)`**: The main search function of the Dancing Links algorithm. It recursively searches for a solution by covering columns and rows, exploring possible solutions.
   - **`solve(matrix)`**: Solves the exact cover problem using the Dancing Links algorithm and returns the solutions found (the configurations of the "animal" on the board).

## Game Flow:
1. **Setup**: The game asks the user for the size of the board and the configuration of the polyomino shape (animal shape).
2. **Player Moves**: Players take turns entering the row and column numbers to place their mark on the board.
3. **Winner Check**: After each move, the game checks if the current player has successfully placed an "animal" shape on the board, indicating a win.
4. **Tie Check**: The game checks if the board is full and declares a tie if no player wins.
5. **End of Game**: The game ends when a player wins or when a tie is declared.
