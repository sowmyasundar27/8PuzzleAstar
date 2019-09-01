"""
8 puzzle problem using A* search
"""

from PriorityQueue import queue
from anytree import Node

# Global Vars Initialization
PATH = list()
OUTPUT_FILENAME = 'Output.txt'  # - Misplaced.txt


class MakeNode:
    def __init__(self, state, depth, f_value, move, path):
        """ Initialising an object with state, depth and f(n) value"""
        self.state = state
        self.depth = depth
        self.f_value = f_value
        self.move = move
        self.path = path

    def generate_child(self):
        """ Find the blank tile location and generate child nodes based on the poss """
        for i in range(0, 3):
            for j in range(0, 3):
                if self.state[i][j] == 0:
                    x, y = i, j

        moves_list = [[x, y-1, 'left'], [x, y+1, 'right'], [x-1, y, 'up'], [x+1, y, 'down']]
        children = []
        for i in moves_list:
            child, move = self.move_blank(self.state, x, y, i[0], i[1], i[2])
            if child is not None:
                child_node = MakeNode(child, self.depth+1, 0, move, Node(move, parent=self.path))
                children.append(child_node)

        return children

    def move_blank(self, current_state, x1, y1, x2, y2, move):
        """ Move the blank space in the given direction and if the position value are out
            of limits the return None """
        if 0 <= x2 < len(self.state) and 0 <= y2 < len(self.state):
            temp_puz = self.copymatrix(current_state)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz, move
        else:
            return None, None

    def copymatrix(self, root):
        """ Copy function to create a similar matrix of the given node"""
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp


def heuristic_misplaced(current_state, goal):
    """
    :param current_state: The current state
    :param goal: Goal state
    :return: returns the number of misplaced tiles
    """
    count = 0
    for column in range(0, len(current_state)):
        for row in range(0, len(current_state)):
            if current_state[column][row] != goal[column][row] and current_state[column][row] != 0:
                count += 1
    return count


def value_index(value, state_matrix):
    """
    :param value: The value to be found
    :param state_matrix: Input matrix
    :return: the index
    """
    for i in range(3):
        for j in range(3):
            if state_matrix[i][j] == value:
                return i, j


def heuristic_manhattan(current_state, goal):
    """
    :param current_state:The current state
    :param goal:Goal state
    :return: returns the manhattan distance of misplaced tiles
    """
    manhattan_dist = 0
    for i in range(3):
        for j in range(3):
            if current_state[i][j] != 0:
                x, y = value_index(current_state[i][j], goal)
                manhattan_dist += abs(x-i) + abs(y-j)

    return manhattan_dist


def function_n(current, goal, heuristic):
    """
    :param current: The current state
    :param goal:  Goal state
    :param heuristic: Blank space heuristic-1 , Manhattan distance heuristic - 2
    :return: returns the cost f(n) = g(n)+ h(n)
    """
    if heuristic == 'misplaced_tiles':
        return heuristic_misplaced(current.state, goal) + current.depth
    if heuristic == 'manhattan':
        return heuristic_manhattan(current.state, goal) + current.depth


if __name__ == "__main__":
    """
    Getting User Input for Initial State and Final State
    """
    print("Enter Initial State (Comma Separated) Eg : 1,2,3,4\n")
    initial_string = list(map(int, input().split(',')))
    print("Enter Goal State (Comma Separated) Eg : 1,2,3,4")
    goal_string = list(map(int, input().split(',')))
    print("Enter Heuristic (0,1) => (Manhattan,Misplaced Tiles) | Enter 0 or 1")
    heuristic_string = int(input())

    # Initializing Global Variables
    HEURISTIC_FUNCTION = 'manhattan' if heuristic_string == 0 else 'misplaced_tiles'
    INITIAL_STATE = [initial_string[i:i+3] for i in range(0, len(initial_string), 3)]
    GOAL_STATE = [goal_string[i:i+3] for i in range(0, len(goal_string), 3)]

    f = open(OUTPUT_FILENAME, 'w')
    print("Heuristic Used : ", HEURISTIC_FUNCTION, file=f)
    print("Initial state : ", INITIAL_STATE, file=f)
    print("Goal state : ", GOAL_STATE, file=f)

    frontier = []
    explored = []
    moves_made = []

    initial_node = MakeNode(INITIAL_STATE, 0, 0, 'initial', Node('initial'))
    initial_node.f_value = function_n(initial_node, GOAL_STATE, HEURISTIC_FUNCTION)
    frontier.append(initial_node)
    print("\n", file=f)
    while True:
        cur = frontier[0]
        print("", file=f)
        print("  | ", file=f)
        print("  | ", file=f)
        print(" \\\'/ \n", file=f)
        for i in cur.state:
            for j in i:
                print(j, end=" ", file=f)
            print("", file=f)
        print("f(n) = g(n) + h(n) = ", cur.depth, "+", cur.f_value - cur.depth, "=", cur.f_value, file=f)
        print("Move - ", cur.move, file=f)
        moves_made.append(cur.move)
        if cur.state == GOAL_STATE:
                print("\nGoal State Reached !", file=f)
                print("Goal path - ", cur.path, file=f)
                print("Number of Nodes Expanded - ", len(explored), file=f)
                print("Total number of Nodes Generated - ", len(frontier) + len(explored)-1, file=f)
                print("Nodes expanded - ", moves_made, file=f)
                break

        current_level = []
        children = cur.generate_child()
        for i in children:
                i.f_value = function_n(i, GOAL_STATE, HEURISTIC_FUNCTION)
                visited = 0
                for fr in frontier:
                    if i.state == fr.state:
                        visited = 1
                for ex in explored:
                    if i.state == ex.state:
                        visited = 1
                if visited == 0:
                    frontier.append(i)
                    current_level.append(i)

        frontier.pop(0)
        explored.append(cur)

        frontier = queue(frontier)
