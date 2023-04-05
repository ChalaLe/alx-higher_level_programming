#!/usr/bin/python3
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard."""

import sys


def n_queens(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""

    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_safe(board, row, col):
        """function checks whether it is safe to place
        a queen at a given position on the board"""
        for i in range(row):
            if board[i] == col or \
                    board[i] - i == col - row or \
                    board[i] + i == col + row:
                return False
        return True

    def solve(board, row):
        """function places queens on the board row by row, and
        when a complete solution is found, it is printed"""
        if row == n:
            print(board)
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row+1)

    solve([None]*n, 0)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        n_queens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
