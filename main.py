import math
import sys
import random
from array import *
import numpy as np
from hill_climb import HillClimb

def createBoard(argv):
    """
        Formation:
            Queen = [Column][Row, Weight]
            
    """
    n = int(argv[0])
    board = np.zeros([n, n], dtype = int) 
    queens = np.zeros([n, 2], dtype = int) # Row of existance and weight

    for i in range(0, n):
        q_wt = random.randint(1,9)
        pos = random.randint(0,n-1)
        board[i][pos] = q_wt
        queens[i][:] = (pos, q_wt)

    print("\n")
    print("### Queen Board ###")
    print(board.T)
    print("\n")
    # print(queens)
    return queens

"""
    Heuristic = 0 -> H1
                1 -> H2
"""
def main(argv):
    queens = createBoard(argv)
    heur = 0 if argv[2] == "H1" else 1 

    if int(argv[1]) == 1:   # A* Algorithm
        pass
    elif int(argv[1]) == 2: # Hill Climb
        hill_solver = HillClimb(queens, heur)
        hill_solver.solve()
    



if __name__ == "__main__":
    main(sys.argv[1:])