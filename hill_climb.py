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
        start_time = time.time()
        looper = True
        solving = True

        start_attack = self.common.getAttackList(self._local_qn)
        lowest_heur = self.common.getHeuristic(start_attack)
        start_heur = (lowest_heur)
        print("Heuristic at start: ", lowest_heur)
        print("\n \n")

        # MOVE TO SELF
        max_shoulder_moves = 100
        global_lowest_heur = lowest_heur
        lowest_qn = deepcopy(self._local_qn)
        moves_tried = 0

        while solving:
            shoulder_moves = 0
            self._local_qn = deepcopy(self._local_qn_master)
            start_attack = self.common.getAttackList(self._local_qn)
            lowest_heur = self.common.getHeuristic(start_attack)

            while looper:
                move_log = self.getMoveLog()
                if len(move_log) == 0:
                    solving = False
                    looper = False
                    break

                possible_moves = self.common.getLowestHeurMoves(move_log)
                i = random.randint(0, len(possible_moves)-1)

                if lowest_heur >= possible_moves[i][2]:
                    if lowest_heur == possible_moves[i][2]:
                        shoulder_moves += 1
                    lowest_heur = possible_moves[i][2]
                    col = possible_moves[i][0]
                    row = possible_moves[i][1]
                    self._local_qn[col][0] = row
                    moves_tried += 1
                else:
                    looper = False

                if shoulder_moves >= max_shoulder_moves:
                    break

                elapsed_time = time.time() - start_time
                if elapsed_time > 10:
                    solving = False
                    looper = False
                    break

            if global_lowest_heur > lowest_heur:
                global_lowest_heur = lowest_heur
                lowest_qn = deepcopy(self._local_qn)

            elapsed_time = time.time() - start_time
            if elapsed_time > 10:
                break

        self.common.drawBoard(lowest_qn)
        end_attack = self.common.getAttackList(lowest_qn)
        heur = self.common.getHeuristic(end_attack)
        print("Attacking Positions at end: ", global_lowest_heur)

        print("\n Moves tried:", moves_tried)

    """
        Move Log = [queen column, queen moved row, heuristic val, cost]
    """

    def getMoveLog(self):
        move_log = []
        attack_list = []
        move_cost = 0
        heur_val = 0
        # for i in range(0,self.n):    # Column Iterator
        attack_list = self.common.getAttackList(self._local_qn)
        if len(attack_list) == 0:
            return move_log
        light_qn_col_list = self.common.getAttackQueenList(attack_list)
        # light_qn_col = np.random.choice(light_qn_col_list)
        for light_qn_col in light_qn_col_list:
            for j in range(0, self.n):      # Row Iterator
                # if switch is current position
                if j == self._local_qn[light_qn_col][0]:
                    continue
                self._local_qn[light_qn_col][0] = j
                attack_list = self.common.getAttackList(self._local_qn)
                heur_val = self.common.getHeuristic(attack_list)
                move_cost = self.common.getMoveCost(light_qn_col, j)
                move_log.append([light_qn_col, j, heur_val, move_cost])
                self._local_qn[light_qn_col][0] = self._local_qn_master[light_qn_col][0]
        # print (move_log)
        return np.array(move_log)
