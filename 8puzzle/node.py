from game import Game, Action_Space
from copy import deepcopy
from typing import List

class Node:
    def __init__(self, state: Game) -> None:
        self.data: Game = state
        self.parent: List['Node'] = []
        self.children: List['Node'] = []
        self.terminated: bool = False
        self.goal: bool = False

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            if self.data.current_state.num_list == other.data.current_state.num_list:
                return True
            else:
                return False
        return False

    def __str__(self) -> str:
        return f"Move Performed: {self.data.move_performed} Node:\n{self.data}"

    def add_child(self, child_node: 'Node') -> None:
        self.children.append(child_node)

    def get_all_children(self) -> List['Node']:
        child_list: List['Node'] = []

        game = deepcopy(self.data)
        can_move = game.move(Action_Space.Left)
        if can_move:
            node = Node(game)
            child_list.append(node)

        game = deepcopy(self.data)
        can_move = game.move(Action_Space.Up)
        if can_move:
            node = Node(game)
            child_list.append(node)

        game = deepcopy(self.data)
        can_move = game.move(Action_Space.Down)
        if can_move:
            node = Node(game)
            child_list.append(node)

        game = deepcopy(self.data)
        can_move = game.move(Action_Space.Right)
        if can_move:
            node = Node(game)
            child_list.append(node)
        return child_list