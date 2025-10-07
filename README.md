# Harary’s Animal Tic-Tac-Toe

## Program Structure

This Python program implements **Harary’s Animal Tic-Tac-Toe**, a generalized version of the traditional Tic-Tac-Toe game where players aim to reproduce a predefined **polyomino shape** (called an “animal”) instead of forming a simple line.

The game is played on an `n × n` grid by two players who alternate turns, marking empty cells with their respective symbols (`1` and `-1`). The first player to form the target polyomino pattern anywhere on the board wins.

### Core Components

- **`AnimalTicTacToe` class** — Manages all game logic, including board creation, turn handling and winner detection.  
- **NumPy arrays** — Used to represent both the board (`self.board`) and the polyomino shape (`self.animal_shape`).  
- **Gameplay flow** — Players define the target shape, take turns placing their marks and after each move, the game checks whether the target pattern appears in any rotation or reflection.

---

## Polyomino Search Algorithm

The main algorithm determines whether a player’s marks form the target polyomino on the board. It relies on systematic transformation generation and a local matching process.

### 1. Generating Shape Transformations  
The function `generate_transformations(shape)` creates all **unique rotations** (0°, 90°, 180°, 270°) and **horizontal reflections** of the polyomino.  
This ensures the pattern can be detected regardless of its orientation or symmetry on the board.

### 2. Sliding Search Over the Board  
The function `check_shape_on_board(board, shape, player_mark)` performs a **windowed search** across the board:
- The polyomino is "slid" across all possible positions.  
- For each position, the function checks if every `1` in the shape aligns with the player’s mark (`player_mark`) on the board.  
- If all required cells match, the function returns `True`.

### 3. Winner Detection  
The method `check_winner(board, animal_shape, player_mark)` iterates through all rotations and reflections generated earlier.  
If any transformation of the polyomino matches the player’s marks on the board, that player is declared the winner.

### 4. Game Loop and Turn Handling  
Within `play_game()`:
- The player defines the board size and the coordinates of the polyomino’s cells.  
- The board is initialized and players alternate turns, placing marks in empty cells.  
- After every move, the algorithm checks for a win or a tie.  
- The game ends as soon as a winner is found or the board is completely filled.

---
