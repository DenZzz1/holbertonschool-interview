#!/usr/bin/python3
"""Module that solves the N queens puzzle."""
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at (row, col).

    Args:
        board (list): list where index is row and value is column
            of the queen placed in that row.
        row (int): row to check.
        col (int): column to check.

    Returns:
        bool: True if it's safe to place a queen there.
    """
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """Recursively solve the N queens puzzle using backtracking.

    Args:
        n (int): size of the board.
        row (int): current row being processed.
        board (list): current state of queen placements.
        solutions (list): list to store found solutions.
    """
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)
            board[row] = -1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * n
    solve_nqueens(n, 0, board, solutions)

    for solution in solutions:
        print(solution)
