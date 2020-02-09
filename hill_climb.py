from common import HeavyQueenCommons

class HillClimb:
    def __init__(self):
        self.common = HeavyQueenCommons()

    def solve(self, queens):
        attack_list = self.common.getAttackList(queens)
        print(attack_list)
