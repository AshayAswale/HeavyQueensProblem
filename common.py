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
    def getAttackList(self, qn_pos):
        count = 0
        attack_qn_lst = []
        for q_1 in range(0, len(qn_pos)-1):
            for q_2 in range(q_1+1, len(qn_pos)):
                diff = q_1 - q_2
                is_same_row = qn_pos[q_1][0] == qn_pos[q_2][0]
                is_diag_up = qn_pos[q_1][0] == qn_pos[q_2][0] + diff
                is_diag_dn = qn_pos[q_1][0] == qn_pos[q_2][0] - diff
                if is_same_row or is_diag_up or is_diag_dn:
                    count += 1
                    attack_qn_lst.append([q_1, q_2, qn_pos[q_1][1], qn_pos[q_2][1]])
        return np.array(attack_qn_lst)


    def getHeuristic(self, attack_list):
        return len(attack_list)

    def getLightQnColumn(self, attack_list):
        # min_a = attack_list[:][3:4].index(min(attack_list[:][3:4]))
        qn_list = []
        min_a = np.where(attack_list[:,2] == attack_list[:,2].min())
        min_b = np.where(attack_list[:,3] == attack_list[:,3].min())
        if attack_list[min_a[0][0], 2]<attack_list[min_b[0][0],3]:
            for i in min_a:
                qn_list.append(attack_list[i,0])
        elif attack_list[min_a[0][0], 2]>attack_list[min_b[0][0],3]:
            for i in min_b:
                qn_list.append(attack_list[i,1])
        else:
            # min_a = np.append(min_a, min_b)
            for i in min_a:
                qn_list.append(attack_list[i,0])
            for i in min_b:
                qn_list = np.append(qn_list, attack_list[i,1])
        qn_list = np.unique(qn_list)
        # print (qn_list)
        return qn_list


    def getMoveCost(self, col, row):
        qn_wt = self._local_qn[col][1]
        qn_org_row = self._local_qn[col][0]
        move_dist = abs(qn_org_row - row)
        cost = move_dist*qn_wt
        return cost

    # def getLightestQn(self, attack_qn):
    #     min_a = attack_qn[:][3].index(min(attack_qn[:][3]))
    #     print (min_a)
    #     return min_a

    @staticmethod
    def getLowestHeurMoves(move_log):
        indexes = np.where(move_log[:,2] == move_log[:,2].min())
        a = []
        for i in indexes[0]:
            a.append(move_log[i])
        return np.array(a)

    @staticmethod
    def getLowestCostMoves(possbl_moves):
        indexes = np.where(possbl_moves[:,3] == possbl_moves[:,3].min())
        a = []
        for i in indexes[0]:
            a.append(possbl_moves[i])
        return np.array(a)

    @staticmethod
    def drawBoard(queens):
        n = len(queens)
        board = np.zeros([n, n], dtype = int) 
        for i in range(0, n):
            q_wt = random.randint(1,9)
            pos = random.randint(0,n-1)
            board[i][pos] = q_wt
            queens[i][:] = (pos, q_wt)
        
        print("### Solved Queen Board ###")
        print(board.T)
        print("\n")
