from common import HeavyQueenCommons
from copy import copy, deepcopy
import numpy as np

class HillClimb:
    def __init__(self, queens, heuristic):
        self.common = HeavyQueenCommons(queens, heuristic)
        self.n = len(queens)
        
        self._local_qn = deepcopy(queens)
        self._local_qn_master = deepcopy(queens)

    def solve(self):
        looper = True
        start_attack = self.common.getAttackList(self._local_qn)
        lowest_heur = self.common.getHeuristic(start_attack)
        print ("Attacking Positions at start: ", lowest_heur)

        while looper:

            move_log = self.getMoveLog()

            # print("### Move Log ###")
            # print(move_log)
            # print("\n")

            possible_moves = self.common.getLowestHeurMoves(move_log)
            possible_moves = self.common.getLowestCostMoves(possible_moves)

            # print("### Lowest Heuristic Moves ###")
            # print(possible_moves)
            # print("\n")
            
            if lowest_heur > possible_moves[0][2]:
                lowest_heur = possible_moves[0][2]
                col = possible_moves[0][0]
                row = possible_moves[0][1]
                self._local_qn[col][0] = row
            else:
                looper = False
        self.common.drawBoard(self._local_qn)
        end_attack = self.common.getAttackList(self._local_qn)
        heur = self.common.getHeuristic(end_attack)
        print ("Attacking Positions at end: ", heur)



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
        light_qn_col_list = self.common.getLightQnColumn(attack_list)
        # light_qn_col = np.random.choice(light_qn_col_list)
        for light_qn_col in light_qn_col_list:
            for j in range(0,self.n):      # Row Iterator
                if j == self._local_qn[light_qn_col][0]:    # if switch is current position
                    continue
                self._local_qn[light_qn_col][0] = j
                attack_list = self.common.getAttackList(self._local_qn)
                heur_val = self.common.getHeuristic(attack_list)
                move_cost = self.common.getMoveCost(light_qn_col, j)
                move_log.append([light_qn_col, j, heur_val, move_cost])
                self._local_qn[light_qn_col][0] = self._local_qn_master[light_qn_col][0] 
        # print (move_log)
        return np.array(move_log)
