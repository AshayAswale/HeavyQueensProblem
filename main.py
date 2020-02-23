import csv
import sys
import random
import numpy as np
from hill_climb import HillClimb
from astar import AStar


def createBoard(argv):
    """
        Formation:
            Queen = [Column][Row, Weight]

    """
    n = int(argv)
    queens = np.zeros([n, 2], dtype=int)  # Row of existence and weight

    board = np.zeros([n, n], dtype=int)
    for i in range(0, n):
        q_wt = random.randint(1, 9)
        pos = random.randint(0, n-1)
        board[i][pos] = q_wt
        queens[i][:] = (pos, q_wt)

    print("\n")
    print("### Queen Board ###")
    print(board.T)
    print("\n")
    return queens


def getDemoBoard(input_file):

    with open(input_file, 'r', encoding="utf-8-sig") as csv_file:
        csv_reader = csv.reader(csv_file)
        n = 0
        for row in csv_reader:
            n += 1

    queens = np.zeros([n, 2], dtype=int)  # Row of existence and weight

    with open(input_file, 'r', encoding="utf-8-sig") as csv_file2:
        csv_reader2 = csv.reader(csv_file2)
        i = 0
        for row in csv_reader2:
            j = 0
            for column in row:
                if column != '':
                    queens[j][0] = i
                    queens[j][1] = column
                j += 1
            i += 1

    board = np.zeros([n, n], dtype=int)  # Empty board
    x = 0
    for rw in queens:
        board[queens[x][0]][x] = queens[x][1]
        x += 1

    print("\n")
    print("### Starting State ###")
    for r in board:
        print(r)
    print("\n")
    csv_file.close()
    return queens


"""
    Heuristic = 0 -> H1
                1 -> H2
"""


def main(argv):
    # queens = createBoard(argv[0])
    queens = getDemoBoard(argv[0])
    heur = 0 if argv[2] == "H1" else 1

    if int(argv[1]) == 1:   # A* Algorithm
        astar_solver = AStar(queens, heur)
        print(astar_solver.Solve())
    elif int(argv[1]) == 2:  # Hill Climb
        hill_solver = HillClimb(queens, heur)
        hill_solver.solve()
        # hill_solver.solveSimulatedAnnealing()


if __name__ == "__main__":
    main(sys.argv[1:])
