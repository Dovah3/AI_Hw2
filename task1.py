import random
import time


def get_conflicts(board):
    """
    Calculates the number of pairwise conflicts between queens on a chess board.
    A conflict occurs when two queens threaten each other on the same row, column, or diagonal.

    Args:
        board (list): List where the index is the row and the value at each index is the column
                      of the queen in that row.

    Returns:
        int: Total number of pairwise conflicts.
    """
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts


def choose_conflicted_queen(board):
    """
    Identifies a queen that is in conflict on the board.

    Args:
        board (list): Current configuration of the board.

    Returns:
        int: Index of a randomly selected queen that is in conflict, if any.
    """
    n = len(board)
    conflicted = [i for i in range(n) if is_in_conflict(i, board)]
    return random.choice(conflicted) if conflicted else None


def is_in_conflict(queen_index, board):
    """
    Determines if a queen is in conflict with any other queen.

    Args:
        queen_index (int): Index of the queen to check.
        board (list): Board configuration.

    Returns:
        bool: True if the queen is in conflict, False otherwise.
    """
    for i in range(len(board)):
        if i != queen_index:
            if board[i] == board[queen_index] or abs(board[i] - board[queen_index]) == abs(i - queen_index):
                return True
    return False


def min_conflicts(n, max_iterations=100000):
    """
    Solves the N-Queens problem using the Min-Conflicts algorithm, a heuristic for solving CSPs
    that minimizes the number of conflicts.

    Args:
        n (int): Number of queens and the size of the chessboard.
        max_iterations (int): Maximum number of iterations to attempt before giving up.

    Returns:
        list: A solution as a board configuration that solves the N-Queens problem, or None if no solution is found.
    """
    # Initialize board randomly
    board = [random.randint(0, n - 1) for _ in range(n)]

    for _ in range(max_iterations):
        conflicts = get_conflicts(board)
        if conflicts == 0:
            return board

        queen = choose_conflicted_queen(board)

        # Try to find the best position for the conflicted queen
        min_conflict_count = float('inf')
        best_position = board[queen]
        for col in range(n):
            board[queen] = col
            current_conflicts = get_conflicts(board)
            if current_conflicts < min_conflict_count:
                min_conflict_count = current_conflicts
                best_position = col

        # Move queen to the position that minimizes conflicts
        board[queen] = best_position

    return None  # No solution found


if __name__ == "__main__":
    n = int(input('Please enter how many Queens you want: '))
    if n <= 3:
        print("No solution is possible for the given number of queens.")
        exit()

    start_time = time.time()
    solution = min_conflicts(n)

    if solution:
        print("Solution found:")
        for row, col in enumerate(solution):
            print(f"Queen {row + 1} at column {col + 1}")
    else:
        print("No solution found after reaching maximum iterations.")

    end_time = time.time()
    print(f"Total time: {end_time - start_time:.2f}s")