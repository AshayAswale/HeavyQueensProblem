from common import HeavyQueenCommons
from copy import copy, deepcopy
import time
import random
import numpy as np


# Create the Node Class for creating the nodes
class Node:
    def __init__(self, parent=None, config=None):
        self.parent = parent
        self.config = config
        self.c = ""
        self.g = 0
        self.h = 0
        self.f = 0

    # Function to encode the configurations to a string
    def encode(self, config):
        n = len(config)
        s = ""
        for x in range(0, n):
            s = s + str(config[x][0])
        return s

    # Function to compare 2 Nodes
    def __eq__(self, other):
        # return self.encode(self.config) == other.encode(other.config)
        return self.c == other.c


class AStar:
    def __init__(self, start, heuristic):
        self.common = HeavyQueenCommons(start, heuristic)
        self.n = len(start)
        self.start_node = Node(None, start)
        self.start_node.c = self.start_node.encode(start)
        self._local_qn = deepcopy(start)
        self._local_qn_master = deepcopy(start)

    def Solve(self):
        # Initializing the starting variables
        open_list = []
        closed_list = []
        open_list.append(self.start_node)
        targ = []
        start_time = time.time()
        global maxcost
        maxcost = float("inf")

        # Looping over the nodes
        while len(open_list) and time.time() - start_time < 10:
            current_node = open_list[0]
            current_index = 0
            # Finding the best node to explore
            for index, item in enumerate(open_list):
                if item.f > maxcost:
                    open_list.pop(index)
                if item.f < current_node.f:
                    current_node = item
                    current_index = index
                if item.f == current_node.f and item.h < current_node.h:
                    current_node = item
                    current_index = index

            # Putting the node to be explored to the closed list
            open_list.pop(current_index)
            closed_list.append(current_node)
            # print(len(open_list))
            # Checking if the node is the target node
            attack_list = self.common.getAttackList(current_node.config)
            end = len(attack_list)

            if end == 0:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.encode(current.config))
                    # self.common.drawBoard(current.config)
                    current = current.parent

                ################################
                ####### PRINTING RESULTS #######
                ################################
                print("Number of nodes expanded: %s" % (len(closed_list) - 1))
                print("Time to solve the puzzle: %0.2f Seconds" % (time.time() - start_time))
                print("Effective branching factor: %s" % ((len(closed_list) - 1) / len(path)))
                print("Cost to solve the puzzle: %s" % current_node.f)
                print("Sequence of moves: %s \n \n" % path[::-1])
                self.common.drawBoard(current_node.config)
                return

            # Calling function to generate neighbours of the current node
            self.generate_neighbours(current_node, open_list, closed_list)

    def generate_neighbours(self, current_node, open_list, closed_list):
        global maxcost
        neighbours = []
        attack_list = self.common.getAttackList(current_node.config)
        queen_attack = self.common.getAttackQueenList(attack_list)

        # Running Iterations to generate next possible nodes
        for queen in queen_attack:
            for j in range(0, self.n):
                val = current_node.config[queen][0]
                if j == val:
                    continue
                neighbour_node = Node(current_node, deepcopy(current_node.config))
                neighbour_node.config[queen][0] = j
                neighbour_node.c = neighbour_node.encode(neighbour_node.config)

                # Checking if the node already exists in the closed lst
                cl = 0
                for closed_neighbour in closed_list:
                    if neighbour_node == closed_neighbour:
                        cl = 1
                if cl == 1:
                    continue

                # Calculating the costs for the node
                neighbour_attack_list = self.common.getAttackList(neighbour_node.config)
                neighbour_node.h = self.common.getHeuristic(neighbour_attack_list)
                neighbour_node.g = current_node.g + self.common.getMoveCost(queen, j, val)
                neighbour_node.f = neighbour_node.g + neighbour_node.h

                # Checking if the cost of node is greater than the maximum cost
                if neighbour_node.f > maxcost:
                    continue

                # Setting the maximum cost
                if neighbour_node.h == 0 and maxcost > neighbour_node.f:
                    maxcost = neighbour_node.f
                # print("Target Cost: %s"%maxcost)

                # Checking if the node belongs to the open list
                op = 0
                for index, open_neighbour in enumerate(open_list):
                    if neighbour_node == open_neighbour:
                        if neighbour_node.g > open_neighbour.g:
                            op = 1
                        else:
                            open_list.pop(index)
                if op == 1:
                    continue
                # Adding the node to the open list
                open_list.append(neighbour_node)
