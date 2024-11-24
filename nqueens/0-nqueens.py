#!/usr/bin/python3
import sys

arg = sys.argv

def explore(matrix, y, n, all_solutions):
    """
    Recursive function to solve the N-Queens problem.
    """
    if y == n:
        all_solutions.append([row[:] for row in matrix])
        return

    for x in range(n):
        if checker(matrix, x, y):
            matrix[x][y] = 1  # Place a queen
            explore(matrix, y + 1, n, all_solutions)  # Recursive call
            matrix[x][y] = 0  # Remove the queen

def checker(matrix, x, y):
    """
    Checks if a queen can be placed on the square (x, y) of the board.
    """
    # Check the row
    for i in range(y):
        if matrix[x][i] == 1:
            return False

    # Check the upper left diagonal
    for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
        if matrix[i][j] == 1:
            return False

    # Check the lower left diagonal
    for i, j in zip(range(x, len(matrix), 1), range(y, -1, -1)):
        if matrix[i][j] == 1:
            return False

    return True

if len(arg) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(arg[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

all_solutions = []
matrix = [[0 for _ in range(n)] for _ in range(n)]

explore(matrix, 0, n, all_solutions)

for solution in all_solutions:
    print([[i, j] for i in range(n) for j in range(n) if solution[i][j] == 1])
