import random


class TicTacToe:
    def __init__(self):
        self.board = [['-', 'O', 'X'],
                      ['X', 'O', 'O'],
                      ['-', '-', '-']]  # Initialize an empty board

    def fix_spot(self, row, col, player):
        """
        Fixes the spot on the board with the player's symbol ('X' or 'O').
        """
        self.board[row][col] = player

    def is_player_win(self, player):
        """
        Checks if the specified player has won the game.
        """
        n = len(self.board)
        # Checking rows, columns, and diagonals
        for i in range(n):
            if all(self.board[i][j] == player for j in range(n)) or \
                    all(self.board[j][i] == player for j in range(n)) or \
                    all(self.board[i][i] == player for i in range(n)) or \
                    all(self.board[i][n - i - 1] == player for i in range(n)):
                return True
        return False

    def is_board_filled(self):
        """
        Checks if the board is completely filled with symbols.
        """
        return all(item != '-' for row in self.board for item in row)

    def swap_player_turn(self, player):
        """
        Swaps the player turn between 'X' and 'O'.
        """
        return 'X' if player == 'O' else 'O'

    def minimax(self, depth, is_maximizing):
        """
        Implementation of the minimax algorithm to determine the best move for the computer player.
        """
        if self.is_player_win('O'):
            return 1
        elif self.is_player_win('X'):
            return -1
        elif self.is_board_filled():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '-':
                        self.fix_spot(i, j, 'O')
                        score = self.minimax(depth + 1, False)
                        self.fix_spot(i, j, '-')
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '-':
                        self.fix_spot(i, j, 'X')
                        score = self.minimax(depth + 1, True)
                        self.fix_spot(i, j, '-')
                        best_score = min(best_score, score)
            return best_score

    def best_move(self):
        """
        Determines the best move for the computer player using the minimax algorithm.
        """
        print(f"Computer (O) is thinking...")
        print(f"Heuristic values for all considered states:")
        best_score = float('-inf')
        best_move = None
        empty_spaces = sum(row.count('-') for row in self.board)
        depth = 9 - empty_spaces
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-':
                    self.fix_spot(i, j, 'O')
                    score = self.minimax(depth, False)
                    print(f"({i + 1}, {j + 1}): {score}")
                    self.fix_spot(i, j, '-')
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move, best_score

    def start(self):
        """
        Starts the Tic Tac Toe game.
        """


        player = 'X'
        while True:
            print(f"Player {player} turn")
            self.show_board()

            if player == 'X':
                row, col = list(map(int, input("Enter row and column numbers to fix spot: ").split()))
                self.fix_spot(row - 1, col - 1, player)
            else:
                # Computer's turn
                best_move, best_score = self.best_move()
                print(f"Determination of the best move against: {best_move} with heuristic value: {best_score}")
                self.fix_spot(best_move[0], best_move[1], player)

            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break
            elif self.is_board_filled():
                print("Match Draw!")
                break

            player = self.swap_player_turn(player)
            print()

    def show_board(self):
        """
        Displays the current state of the board.
        """
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()


# Starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
