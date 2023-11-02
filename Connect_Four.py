import numpy as np

class ConnectFour:
    def __init__(self):
        while True:
            try:
                self.rows = int(input("Please enter the number of rows (default is 7): ") or 7)
                self.cols = int(input("Please enter the number of columns (default is 6): ") or 6)
                if self.rows < 4 or self.cols < 4:
                    print("Rows and columns must be at least 4!")
                    continue
                break
            except ValueError:
                print("Please enter a valid number!")
        self.board = np.zeros((self.rows, self.cols))
        self.next_open_row = {i:-1 for i in range(self.cols)}
        self.game_over = False
        self.current_player = 1

    def reset(self):
        self.board = np.zeros((self.rows, self.cols))
        self.next_open_row = {i:-1 for i in range(self.cols)}
        self.game_over = False

    def is_valid_location(self, col):
        return col>=0 and col<self.cols and self.board[self.rows - 1][col] == 0

    def get_next_open_row(self, col):
        return self.next_open_row[col] + 1

    def print_board(self):
        print(np.flip(self.board, 0))

    def check_sequence(self, row, col, row_delta, col_delta, piece):
        count = 0
        for i in range(-3, 4):
            r, c = row + i * row_delta, col + i * col_delta
            if 0 <= r < len(self.board) and 0 <= c < len(self.board[0]) and self.board[r][c] == piece:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        return False

    def check_win(self, row, col, piece):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        return any(self.check_sequence(row, col, d[0], d[1], piece) for d in directions)

    def make_move(self, col):
        if not self.is_valid_location(col):
            print("Invalid Location!")
            return False

        row = self.get_next_open_row(col)
        self.board[row][col] = self.current_player
        self.next_open_row[col] = row

        if self.check_win(row, col, self.current_player):
            print(f'Player{self.current_player} wins')
            self.game_over = True
            return True

        self.print_board()
        self.switch_player()
        return True

    def switch_player(self):
        self.current_player = 3 - self.current_player  # Switch between 1 and 2

    def play(self):
        self.reset()
        choice = input("Who goes first? Player 1 or Player 2: ")
        self.current_player = int(choice)

        while not self.game_over:
            col = int(input(f'Player{self.current_player} make selection(0-6):'))
            self.make_move(col)


game = ConnectFour()
game.play()
