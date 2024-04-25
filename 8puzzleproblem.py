# Python3 program to print the path from root
# node to destination node for N*N-1 puzzle
# algorithm using Branch and Bound
# The solution assumes that instance of
# puzzle is solvable

import heapq
import time

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, g=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.g = g

    def __lt__(self, other):
        return (self.g + self.h()) < (other.g + other.h())

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(tuple(self.state))

    def h(self):
        # Heuristic: Number of misplaced tiles (excluding the empty tile)
        return sum(1 if self.state[i] != goal_state[i] and self.state[i] != 0 else 0 for i in range(9))

    def expand(self):
        successors = []
        zero_index = self.state.index(0)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        directions = ['Up', 'Down', 'Left', 'Right']

        for i, move in enumerate(moves):
            new_row = zero_index // 3 + move[0]
            new_col = zero_index % 3 + move[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_index = new_row * 3 + new_col
                new_state = self.state[:]
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                successors.append(PuzzleNode(new_state, self, directions[i], self.g + 1))

        return successors

    def get_path(self):
        path = []
        current = self
        while current:
            path.append((current.state, current.move, current.h()))
            current = current.parent
        path.reverse()
        return path

def astar(start_state):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, start_state)
    start_time = time.time()

    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.state == goal_state:
            end_time = time.time()
            time_taken = end_time - start_time
            return current_node.get_path(), time_taken

        closed_set.add(tuple(current_node.state))
        successors = current_node.expand()

        for successor in successors:
            if tuple(successor.state) not in closed_set:
                heapq.heappush(open_list, successor)

if __name__ == "__main__":
    print("Enter the initial state (use 0 for the blank space):")
    initial_state = [int(x) for x in input().split()]

    print("Enter the goal state:")
    goal_state = [int(x) for x in input().split()]

    initial_node = PuzzleNode(initial_state)
    solution, time_taken = astar(initial_node)

    if solution:
        print("Solution found:")
        num_steps = len(solution) - 1
        for step in solution:
            print(step[0][:3])
            print(step[0][3:6])
            print(step[0][6:])
            print("Heuristic:", step[2])
            print("Move:", step[1])
            print()
        print("Goal state:")
        print(goal_state[:3])
        print(goal_state[3:6])
        print(goal_state[6:])
        print("Goal state found!")
        print("Number of steps required to reach the goal state:", num_steps)
        print("Time taken to solve the problem:", round(time_taken, 6), "seconds")
    else:
        print("No solution found.")

'''
Enter the initial state (use 0 for the blank space):
2 8 3 1 6 4 7 0 5
Enter the goal state:
1 2 3 8 0 4 7 6 5
'''