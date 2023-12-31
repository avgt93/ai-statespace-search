import math

class Astar_Node:
    @staticmethod
    def manhattan_distance(node: 'Astar_Node') -> int:
        manhattan_distance = 0
        for k in range(1, 9):
            current_index = node.data.current_state.num_list.index(k)
            current_i = math.floor(current_index / 3)
            current_j = current_index - 3 * current_i

            goal_index = node.data.goal_state.num_list.index(k)
            goal_i = math.floor(goal_index / 3)
            goal_j = goal_index - 3 * goal_i

            manhattan_distance += abs(current_j - goal_j) + abs(current_i - goal_i)

        return manhattan_distance

    @staticmethod
    def no_of_misplaced_tiles(node: 'Astar_Node') -> int:
        hamming_distance = 0
        for k in range(1, 9):
            if node.data.current_state.num_list.index(k) != node.data.goal_state.num_list.index(k):
                hamming_distance += 1

        return hamming_distance