#!/usr/bin/python3
"""  """
import sys


def print_solutions(solutions):
    for solution in solutions:
        print(solution)


def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solve_nqueens(n, board, col, solutions):
    if col == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for i in range(n):
        if is_safe(board, i, col):
            board[col] = i
            solve_nqueens(n, board, col + 1, solutions)
            board[col] = 0


def main():
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
    board = [0] * n
    solve_nqueens(n, board, 0, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
