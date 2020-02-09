class HeavyQueenCommons:
    def __init__(self):
        pass

    @staticmethod
    def getAttackList(qn_pos):
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
                    attack_qn_lst.append((q_1, q_2))
        return attack_qn_lst    