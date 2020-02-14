from common import HeavyQueenCommons
from copy import copy, deepcopy
import time
import random
import numpy as np


class HillClimb:
    def __init__(self, queens, heuristic):
        self.common = HeavyQueenCommons(queens, heuristic)
        self.n = len(queens)

        self._local_qn = deepcopy(queens)
        self._local_qn_master = deepcopy(queens)

    def solve(self):
        # Start Timer
        start_time = time.time()

        # Loop Variables
        looper = True
        solving = True

        # Save initial variables
        start_attack = self.common.getAttackList(self._local_qn)
        lowest_heur = self.common.getHeuristic(start_attack)
        start_heur = (lowest_heur)
        print("Heuristic at start: ", lowest_heur)
        print("\n \n")

        # --note to self--
        # @todo
        #  need better way to decide shoulder moves
        max_shoulder_moves = 10
        global_lowest_heur = lowest_heur
        lowest_qn = deepcopy(self._local_qn)
        moves_tried = 0
        global_cost = 0
        global_moves = []
        restarts = -1

        while solving:
            shoulder_moves = 0

            # Resetting Start State.
            self._local_qn = deepcopy(self._local_qn_master)
            start_attack = self.common.getAttackList(self._local_qn)
            lowest_heur = self.common.getHeuristic(start_attack)
            cost = 0
            move_list = []
            restarts += 1

            # Random Restarts:
            while looper:
                move_log = self.getMoveLog()

                if len(move_log) == 0:  # Board Solved
                    solving = False
                    looper = False
                    break

                # Enquiring Possible moves. Returns only the move
                # Where Heuristic is the lowest.
                possible_moves = self.common.getLowestHeurMoves(move_log)

                # Choose random move out of possible moves, as all
                # the possible moves have same heuristic value
                i = random.randint(0, len(possible_moves)-1)

                # If possible move has lower heuristic value than
                # existing lowest value, make that move.
                if lowest_heur >= possible_moves[i][2]:
                    if lowest_heur == possible_moves[i][2]:
                        shoulder_moves += 1
                    lowest_heur = possible_moves[i][2]
                    col = possible_moves[i][0]
                    row = possible_moves[i][1]
                    self._local_qn[col][0] = row
                    moves_tried += 1
                    cost += possible_moves[i][3]
                    move_list.append([col, row])

                # If the move has heuristic more than the lowest
                # then exit the loop
                else:
                    looper = False

                # Limiting possible side moves
                if shoulder_moves >= max_shoulder_moves:
                    break

                # If time has passed, exit the code with whatever best we have
                elapsed_time = time.time() - start_time
                if elapsed_time > 10:
                    solving = False
                    looper = False
                    break

            # If the lowest heuristic in this run is lower than all time best
            # Save that move as our best move. We will publish this move
            # at the end of the code/time
            if global_lowest_heur > lowest_heur:
                global_lowest_heur = lowest_heur
                lowest_qn = deepcopy(self._local_qn)
                global_cost = cost
                global_moves = deepcopy(move_list)
                # if global_lowest_heur == 0:
                #     solving = False
                #     break

            # Exit code if time has elapsed.
            elapsed_time = time.time() - start_time
            if elapsed_time > 10:
                break

        # Print the best result
        self.common.drawBoard(lowest_qn)
        end_attack = self.common.getAttackList(lowest_qn)
        heur = self.common.getHeuristic(end_attack)

        ################################
        ####### PRINTING RESULTS #######
        ################################
        print("Heuristic at the end: ", global_lowest_heur)
        print("Number of nodes expanded:", moves_tried)
        print("Time to solve the puzzle: ", elapsed_time)
        if len(global_moves) != 0:
            print("Branching Factor: ", (moves_tried / len(global_moves)))
        else:
            print("Branching Factor: --NA--")
        print("Cost to solve: ", global_cost)
        print("Sequence of moves: \n", global_moves)
        # print("Number of restarts: ", restarts)

    """
        Move Log = [queen column, queen moved row, heuristic val, cost]
    """

    def getMoveLog(self):
        # Initialize the variables needed
        move_log = []
        attack_list = []
        move_cost = 0
        heur_val = 0

        # Get list of attacking queens to decide which queen to move
        attack_list = self.common.getAttackList(self._local_qn)

        # No attack means board is soved. Return blank array
        if len(attack_list) == 0:
            return move_log

        # Columns in which queens are attacking each other. (ommits duplicates)
        light_qn_col_list = self.common.getAttackQueenList(attack_list)

        for light_qn_col in light_qn_col_list:  # Checks for all attacking queens
            for j in range(0, self.n):  # Checks for all possible row locations

                # Save the value of the element to be changed.
                # Value will be restored after change is checked.
                val = self._local_qn[light_qn_col][0]

                # if switch is current position, then do not make the move
                if j == self._local_qn[light_qn_col][0]:
                    continue

                # Make the change, and check for the attack list
                # heuristic and costs at the new location
                self._local_qn[light_qn_col][0] = j
                attack_list = self.common.getAttackList(self._local_qn)
                heur_val = self.common.getHeuristic(attack_list)
                move_cost = self.common.getMoveCost(
                    light_qn_col, j, val)

                # Append the values to move_log.
                move_log.append([light_qn_col, j, heur_val, move_cost])

                # Reset the changed value to original value before change.
                self._local_qn[light_qn_col][0] = val
        return np.array(move_log)
