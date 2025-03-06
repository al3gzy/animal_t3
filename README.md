# Animal Tic-Tac-Toe

## 📌 Overview

This project introduces a variation of the classic **Tic-Tac-Toe** game, called **Animal Tic-Tac-Toe**, where players aim to match a custom **animal shape** (polyomino) on the board. The game uses the **Dancing Links** algorithm to detect winning configurations, where players place their marks (1 or -1) and attempt to form the given animal shape on the board. The shape can be customized by the user, adding a dynamic element to the game, and the game terminates when a player successfully matches the shape or the board is full.

## Key Concepts

### **Polyomino Shapes**

In this version of Tic-Tac-Toe, the winning condition is not based on a simple straight line but on forming a specific **polyomino shape**. The user provides the shape as a set of coordinates, and the game checks if the pattern is formed using the player's marks.

### **Dancing Links Algorithm**

The **Dancing Links** algorithm is used to efficiently solve the problem of determining if a player has successfully formed the animal shape on the board. This algorithm is applied through **exact cover problems**, where the goal is to cover all constraints (in this case, placing the polyomino shape) while ensuring that no constraints are violated.

### **Game Flow**

- Players take turns placing their marks on a grid.
- The board size and the animal shape are customizable.
- The game checks for a winner by applying the **Dancing Links** algorithm to detect if the animal shape has been formed.
- The game ends when a player successfully matches the shape or the board is filled (resulting in a tie).

## Objectives

1. **Polyomino Configuration**: Allow players to define the shape they wish to form on the board. The shape is made up of a set of coordinates that the players need to match.
2. **Exact Cover Problem**: Use the **Dancing Links** algorithm to solve the exact cover problem, checking if the polyomino shape is formed on the board after each move.
3. **Game Play**: Provide an interactive game where two players alternate placing their marks on the board and trying to form the specified animal shape.
4. **Dynamic Winning Condition**: Unlike traditional Tic-Tac-Toe, the winning condition is dynamic and depends on forming the user-defined shape, making the game more flexible and strategic.

## Features

- **Customizable Animal Shape**: Players can define their own shape by selecting coordinates for the animal shape's cells.
- **Dancing Links for Solution Detection**: The **Dancing Links** algorithm is used to detect whether the player has successfully created the animal shape.
- **Interactive Play**: Players input their moves by specifying the row and column on the board. The game ensures that players only place marks on empty cells.
- **Game Over Detection**: The game automatically detects a winner or tie based on the player actions and the polyomino formation.
