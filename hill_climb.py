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
        attack_list = self.common.getAttackList(self._local_qn)

        # print("### Queen List ###")
        # print(self._local_qn)
        # print("\n")

        print("### Attack List ###")
        print(attack_list)
        print("\n")

        self.iterate()

    """
        Move Log = [queen column, queen moved row, heuristic val, cost]
    """
    def iterate(self):
        move_log = []
        attack_list = []
        move_cost = 0
        heur_val = 0
        # for i in range(0,self.n):    # Column Iterator
        attack_list = self.common.getAttackList(self._local_qn)
        light_qn_col_list = self.common.getLightQnColumn(attack_list)
        light_qn_col = np.random.choice(light_qn_col_list)
        for j in range(0,self.n):      # Row Iterator
            if j == self._local_qn[light_qn_col][0]:    # if switch is current position
                continue
            self._local_qn[light_qn_col][0] = j
            attack_list = self.common.getAttackList(self._local_qn)
            heur_val = self.common.getHeuristic(attack_list)
            move_cost = self.common.getMoveCost(light_qn_col, j)
            move_log.append([light_qn_col, j, heur_val, move_cost])
            self._local_qn[light_qn_col][0] = self._local_qn_master[light_qn_col][0] 
        print (move_log)
