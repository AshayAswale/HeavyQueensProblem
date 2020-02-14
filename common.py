from copy import copy, deepcopy
import random
import numpy as np


class HeavyQueenCommons:

    """
        Heuristic = 0 -> H1
                    1 -> H2
    """

    def __init__(self, queen, heuristic_):
        self._local_qn = deepcopy(queen)
        self.heuristic = heuristic_

    """
        Attacking Queen List:
            list = [(Row of queen_1, Row of queen_2, Wt of queen_1, Wt of queen_2)]
    """
    @staticmethod
    def getAttackList(qn_pos):
        count = 0   # This will have count of attacking positions
        attack_qn_lst = []  # This will maintain the list of attacking queens

        for q_1 in range(0, len(qn_pos)-1):         # Iterating board columns
            for q_2 in range(q_1+1, len(qn_pos)):   # Iterating board rows
                diff = q_1 - q_2          # Distance in column of two queens

                # When queens are attacking sideways
                is_same_row = qn_pos[q_1][0] == qn_pos[q_2][0]

                # When queens are attacking diagonally
                is_diag_up = qn_pos[q_1][0] == qn_pos[q_2][0] + diff
                is_diag_dn = qn_pos[q_1][0] == qn_pos[q_2][0] - diff

                # If queens are attacking in any configuration, add to attacking list
                if is_same_row or is_diag_up or is_diag_dn:
                    count += 1
                    attack_qn_lst.append(
                        [q_1, q_2, qn_pos[q_1][1], qn_pos[q_2][1]])
        return np.array(attack_qn_lst)

    @staticmethod
    def getH1(attack_list):
        # If board has been solved, then there will be no attacking queens.
        # Hence return 0
        if len(attack_list) == 0:
            return 0

        # Returning Lowest weight of queen amongst attacking queens
        min_a = attack_list[:, 2].min()
        min_b = attack_list[:, 3].min()
        return min(min_a, min_b)**2     # Squaring the weight before sending

    @staticmethod
    def getH2(attack_list):
        # Initialize the sum
        min_sum = 0

        # Add the minimums of all the attacking pairs
        for i in range(len(attack_list)):
            min_sum += min(attack_list[i][2], attack_list[i][3])**2
        return min_sum

    def getHeuristic(self, attack_list):
        if self.heuristic == 0:  # H1
            return self.getH1(attack_list)
        else:                    # H2
            return self.getH2(attack_list)

    # ---NOTE TO SELF---
    # IS THIS NEEDED ???
    @staticmethod
    def getLightQnColumn(attack_list):
        # min_a = attack_list[:][3:4].index(min(attack_list[:][3:4]))
        qn_list = []
        min_a = np.where(attack_list[:, 2] == attack_list[:, 2].min())
        min_b = np.where(attack_list[:, 3] == attack_list[:, 3].min())
        if attack_list[min_a[0][0], 2] < attack_list[min_b[0][0], 3]:
            for i in min_a:
                qn_list.append(attack_list[i, 0])
        elif attack_list[min_a[0][0], 2] > attack_list[min_b[0][0], 3]:
            for i in min_b:
                qn_list.append(attack_list[i, 1])
        else:
            # min_a = np.append(min_a, min_b)
            for i in min_a:
                qn_list.append(attack_list[i, 0])
            for i in min_b:
                qn_list = np.append(qn_list, attack_list[i, 1])
        qn_list = np.unique(qn_list)
        # print (qn_list)
        return qn_list

    """
        qn_col - column of the queen
        final_row - row in which queen is to be moved
        init_row - initial row from the queen
    """

    def getMoveCost(self, qn_col, final_row, init_row):
        qn_wt = self._local_qn[qn_col][1]       # Weight of the queen
        move_dist = abs(init_row - final_row)   # Distance to be moved
        cost = move_dist*qn_wt*qn_wt            # Total Cost Calculation
        return cost

    # def getLightestQn(self, attack_qn):
    #     min_a = attack_qn[:][3].index(min(attack_qn[:][3]))
    #     print (min_a)
    #     return min_a

    @staticmethod
    def getLowestHeurMoves(move_log):
        indexes = np.where(move_log[:, 2] == move_log[:, 2].min())
        a = []
        for i in indexes[0]:
            a.append(move_log[i])
        return np.array(a)

    @staticmethod
    def getLowestCostMoves(possbl_moves):
        indexes = np.where(possbl_moves[:, 3] == possbl_moves[:, 3].min())
        a = []
        for i in indexes[0]:
            a.append(possbl_moves[i])
        return np.array(a)

    @staticmethod
    def drawBoard(queens_posn):
        n = len(queens_posn)
        board = np.zeros([n, n], dtype=int)
        for i in range(0, n):
            pos = queens_posn[i][0]
            q_wt = queens_posn[i][1]
            board[i][pos] = q_wt

        print("### Solved Queen Board ###")
        print(board.T)
        print("\n")

    @staticmethod
    def getAttackQueenList(attack_list):
        queen_list = np.concatenate((attack_list[:, 0], attack_list[:, 1]))
        return np.unique(queen_list)
