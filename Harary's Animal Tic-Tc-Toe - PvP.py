import numpy as np

class AnimalTicTacToe:
    def __init__(self):
        self.board = None
        self.board_size = None
        self.animal_shape = None
        self.current_player = 1

    def create_board(self, board_size):
        self.board = np.zeros((board_size, board_size), dtype=int)
        self.board_size = board_size

    def print_board(self):
        for row in self.board:
            print(' | '.join(map(str, row)))
            print('-' * (4 * len(row) - 1))

    def check_winner(self, board, animal_shape, player_mark):
        dlx = DancingLinks()
        def convert(board, animal_shape, player_mark):
            rows, cols = len(board), len(board[0])
            animal_shape_rows, animal_shape_cols = len(animal_shape), len(animal_shape[0])
            matrix = np.zeros([rows, cols])
            for i in range(rows):
                for j in range(cols):
                    if board[i, j] == player_mark:
                        matrix[i, j] = 1
            return matrix
        combined = convert(board, animal_shape, player_mark)
        dlx.create_grid(combined)
        solutions = dlx.solve(combined)
        return len(solutions) > 0
    
    def play_game(self):
        board_size = int(input("Board size: "))
        n = int(input("Polyomino size: "))
        default_config = []
        print(f"Default configuration (0-{n-1}).")
        for i in range(n):
            row, col = map(int, input(f"Enter row and column for cell {i+1}: ").split())
            default_config.append([row, col])

        self.animal_shape = np.zeros((n, n))
        for row, col in default_config:
            self.animal_shape[row][col] = 1

        self.create_board(board_size)
        print("Game begins!")

        while True:
            self.print_board()
            print(f"Player {self.current_player}'s turn")
            row, col = map(int, input(f"Enter row and column (0-{self.board_size - 1}): ").split())

            if 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row, col] == 0:
                self.board[row, col] = self.current_player
                if self.check_winner(self.board, self.animal_shape, self.current_player):
                    self.print_board()
                    print(f"Player {self.current_player} wins!")
                    break
                elif 0 not in self.board:
                    self.print_board()
                    print("It's a tie!")
                    break
                else:
                    self.current_player = -1 if self.current_player == 1 else 1
            else:
                print("Invalid move. Try again.")

            if self.check_winner(self.board, self.animal_shape, self.current_player):
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break
            elif 0  not in self.board:
                self.print_board()
                print("It's a tie!")
                break

class DancingLinks:
    def __init__(self):
        self.header = None
        self.solution = []

    class Node:
        def __init__(self, col_name=None):
            self.left = self
            self.right = self
            self.up = self
            self.down = self
            self.col = None
            self.row = None
            self.col_name = col_name

    def create_grid(self, matrix):
        self.header = self.Node()
        columns = {}

        for j, col_name in enumerate(matrix[0]):
            new_node = self.Node(col_name)
            new_node.right = self.header
            new_node.left = self.header.left
            self.header.left.right = new_node
            self.header.left = new_node
            columns[col_name] = new_node

        for i in range(1, len(matrix)):
            prev = None
            for j, val in enumerate(matrix[i]):
                if val == 1:
                    col_name = matrix[0][j]
                    new_node = self.Node(col_name)
                    new_node.col = columns[col_name]
                    new_node.up = columns[col_name].up
                    new_node.down = columns[col_name]
                    columns[col_name].up.down = new_node
                    columns[col_name].up = new_node
                    if prev is None:
                        prev = new_node
                    else:
                        new_node.left = prev
                        new_node.right = prev.right
                        prev.right.left = new_node
                        prev.right = new_node
                        prev = new_node

    def cover(self, column):
        column.right.left = column.left
        column.left.right = column.right
        node = column.down
        while node != column:
            cur = node.right
            while cur != node:
                cur.down.up = cur.up
                cur.up.down = cur.down
                cur = cur.right
            node = node.down

    def uncover(self, column):
        node = column.up
        while node != column:
            cur = node.left
            while cur != node:
                cur.down.up = cur
                cur.up.down = cur
                cur = cur.left
            node = node.up
        column.right.left = column
        column.left.right = column

    def search(self, k=0):
        if self.header.right == self.header:
            return True
        column = self.header.right
        self.cover(column)
        node = column.down
        while node != column:
            self.solution.append(node)
            cur = node.right
            while cur != node:
                self.cover(cur.col)
                cur = cur.right
            if self.search(k + 1):
                return True
            node = self.solution.pop()
            column = node.col
            cur = node.left
            while cur != node:
                self.uncover(cur.col)
                cur = cur.left
            node = node.down
        self.uncover(column)
        return False

    def solve(self, matrix):
        self.create_grid(matrix)
        self.solution = []
        self.search()
        
        solutions = []
        for solution in self.solution:
            columns = []
            node = solution
            while True:
                columns.append(node.col_name)
                node = node.right
                if node == solution:
                    break
            solutions.append(columns)
        
        return solutions

game = AnimalTicTacToe()
game.play_game()