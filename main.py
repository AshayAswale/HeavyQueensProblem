import math
import sys
import random
from array import *
import numpy as np
from hill_climb import HillClimb

def createBoard(argv):
    n = int(argv[0])
    board = np.zeros([n, n], dtype = int) 
    queens = np.zeros([n, 2], dtype = int) # Row of existance and weight

    for i in range(0, n):
        q_wt = random.randint(1,9)
        pos = random.randint(0,n-1)
        board[i][pos] = q_wt
        queens[i][:] = (pos, q_wt)
    print(board.T)
    # print(queens)
    return queens

def main(argv):
    queens = createBoard(argv)

    hill_solver = HillClimb()
    hill_solver.solve(queens)



if __name__ == "__main__":
    main(sys.argv[1:])