import numpy as np
import multiprocessing as mp

def worker_snaky(move, board, shape, max_ply, radius):
    r,c = move
    local_board = board.copy()
    local_board[r,c] = 1
    memo = {}
    ok = can_force_win(local_board, shape, target_player=1,
                       current_player=-1, ply=1, max_ply=max_ply, memo=memo, radius=radius)
    return (move, ok)

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

    def generate_transformations(self, shape):
        import numpy as np
        transformations = []
        for k in range(4):
            rotated = np.rot90(shape, k)
            transformations.append(rotated)
            transformations.append(np.fliplr(rotated))
        unique = []
        for t in transformations:
            t_tuple = tuple(map(tuple, t))
            if t_tuple not in unique:
                unique.append(t_tuple)
        return [np.array(u) for u in unique]

    def check_shape_on_board(self, board, shape, player_mark):
        rows, cols = board.shape
        s_rows, s_cols = shape.shape
        for i in range(rows - s_rows + 1):
            for j in range(cols - s_cols + 1):
                match = True
                for r in range(s_rows):
                    for c in range(s_cols):
                        if shape[r, c] == 1 and board[i+r, j+c] != player_mark:
                            match = False
                            break
                    if not match:
                        break
                if match:
                    return True
        return False

    def check_winner(self, board, animal_shape, player_mark):
        for transformed_shape in self.generate_transformations(animal_shape):
            if self.check_shape_on_board(board, transformed_shape, player_mark):
                return True
        return False
    
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

#game = AnimalTicTacToe()
#game.play_game()