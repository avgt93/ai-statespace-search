import bisect
from game import Game_State, Action_Space, Game
from copy import deepcopy
from a_star_node import Astar_Node
import math
import graphviz
from node import Node
import bisect
import graphviz
from typing import Set, List
graph = graphviz.Digraph(comment="The Table")
graph.attr(layout="dot")
graph.attr(dpi="500")

class Search:
    def __init__(self, root_node: Node):
        self.root_node = root_node
        self.finished = False
        self.searched_nodes: List[Node] = []

    def bfs(self) -> Node:
        print("Performing Breadth First Search\n")
        fresh_nodes: Set[str] = set()
        fresh_nodes.add(str(self.root_node.data.current_state.num_list))
        queue: List[Node] = [self.root_node]

        while queue:
            current_node = queue.pop(0)
            if current_node in self.searched_nodes:
                continue

            self.searched_nodes.append(current_node)
            if current_node.data.game_status == Game_State.Running:
                children = current_node.get_all_children()
                for child in children:
                    if str(child.data.current_state.num_list) not in fresh_nodes:
                        fresh_nodes.add(str(child.data.current_state.num_list))
                        print(child)
                        graph.node(str(current_node.data.current_state))

                        if child.data.game_status == Game_State.Won:
                            graph.node(str(child.data.current_state), style='filled', color='lightgreen')
                        else:
                            graph.node(str(child.data.current_state))
                        graph.edge(str(current_node.data.current_state), str(child.data.current_state),
                                   label=f"{child.data.move_performed}")

                        graph.render('bfs_graph', format='png', cleanup=True)
                        queue.append(child)
                        if child.data.game_status == Game_State.Won:
                            self.finished = True
                            return child

    def dfs(self, max_depth: int = 10) -> Node:
        print("Performing Depth First Search\n")
        fresh_nodes: Set[str] = set()
        fresh_nodes.add(str(self.root_node.data.current_state.num_list))
        stack: List[dict] = []
        stack.append({"node": self.root_node, "depth": 0})
        print(self.root_node)

        while stack:
            current_node = stack.pop(0)
            depth = current_node["depth"]
            current_node = current_node["node"]

            if current_node in self.searched_nodes:
                continue
            self.searched_nodes.append(current_node)

            if current_node.data.game_status == Game_State.Running:
                children = current_node.get_all_children()
                depth_stack = []
                for child in children:
                    if str(child.data.current_state.num_list) not in fresh_nodes:
                        fresh_nodes.add(str(child.data.current_state.num_list))
                        print(child)
                        graph.node(str(current_node.data.current_state))

                        if child.data.game_status == Game_State.Won:
                            graph.node(str(child.data.current_state), style='filled', color='lightgreen')
                        else:
                            graph.node(str(child.data.current_state))

                        graph.edge(str(current_node.data.current_state), str(child.data.current_state),
                                   label=f"{child.data.move_performed}")
                        graph.render('dfs_graph', format='png', cleanup=True)
                        
                        depth+=1
                        depth_stack.append({"node": child, "depth": depth})
                        
                        #guardclause
                        if depth > max_depth:
                            depth_stack.clear()
                            continue

                        if child.data.game_status == Game_State.Won:
                            self.finished = True
                            return child

                stack = [*depth_stack, *stack]

    def idfs(self, max_depth: int) -> Node:
        print("Performing Iterative Deepening Search\n")
        for depth in range(1, max_depth + 1):
            fresh_nodes: Set[str] = set()
            fresh_nodes.add(str(self.root_node.data.current_state.num_list))
            print(self.root_node)

            result = self.dls(self.root_node, depth, fresh_nodes, depth)

            if result is not None:
                return result

    def dls(self, node: Node, depth: int, fresh_nodes: Set[str], current_depth: int) -> Node:
        if depth == 0:
            if node.data.game_status == Game_State.Won:
                self.finished = True
                return node
            return None

        if node in self.searched_nodes:
            node.terminated = True

        self.searched_nodes.append(node)
        if node.data.game_status == Game_State.Running:
            children = node.get_all_children()
            for child in children:
                if str(child.data.current_state.num_list) not in fresh_nodes:
                    fresh_nodes.add(str(child.data.current_state.num_list))
                    print(child)
                    graph.node(str(node.data.current_state))
                    if child.data.game_status == Game_State.Won:
                        graph.node(str(child.data.current_state), style='filled', color='lightgreen')
                    else:
                        graph.node(str(child.data.current_state))

                    graph.edge(str(node.data.current_state), str(child.data.current_state),
                               label=f"{child.data.move_performed}")
                    graph.render('idfs_graph', format='png', cleanup=True)

                    child.parent.append(node)
                    node.add_child(child)
                    result = self.dls(child, depth=depth - 1, fresh_nodes=fresh_nodes,
                                      current_depth=current_depth)
                    if result is not None:
                        return result

    def a_star_manhattan(self) -> Node:
        print("Performing A* Search with Manhattan Distance\n")
        self.root_node.g_value = 0
        self.root_node.f_value = Astar_Node.manhattan_distance(self.root_node)
        list: List[Node] = [self.root_node]
        
        fresh_nodes: Set[str] = set()
        fresh_nodes.add(str(self.root_node.data.current_state.num_list))
        print(self.root_node)

        while list:
            current_node = list.pop(0)
            if current_node in self.searched_nodes:
                current_node.terminated = True
                continue

            self.searched_nodes.append(current_node)

            if current_node.data.game_status == Game_State.Won:
                self.finished = True
                return current_node

            if current_node.data.game_status == Game_State.Running:
                children = current_node.get_all_children()
                for child in children:
                    if str(child.data.current_state.num_list) not in fresh_nodes:
                        child.parent.append(current_node)
                        current_node.add_child(child)
                        child.g_value = current_node.g_value + 1
                        child.f_value = Astar_Node.manhattan_distance(child) + child.g_value

                        fresh_nodes.add(str(child.data.current_state.num_list))

                        if not self.finished:
                            print(child)

                            graph.node(str(current_node.data.current_state))
                            graph.node(str(child.data.current_state))
                            if child.data.game_status == Game_State.Won:
                                graph.node(str(child.data.current_state), style='filled', color='lightgreen')
                            else:
                                graph.node(str(child.data.current_state))
                            graph.edge(str(current_node.data.current_state), str(child.data.current_state),
                                       label=f"{child.data.move_performed} h:{child.f_value}")
                            graph.render('manhattan_graph', format='png', cleanup=True)

                        if child.data.game_status == Game_State.Won:
                            self.finished = True
                        bisect.insort(list, child, key=lambda x: x.f_value)

    def a_star_misplaced_tiles(self) -> Node:
        print("Performing A* Search with Misplaced Tiles\n")

        self.root_node.g_value = 0
        self.root_node.f_value = Astar_Node.no_of_misplaced_tiles(self.root_node)

        list: List[Node] = []
        list.append(self.root_node)

        fresh_nodes: Set[str] = set()
        fresh_nodes.add(str(self.root_node.data.current_state.num_list))
        print(self.root_node)
        
        while list:
            current_node = list.pop(0)

            if current_node in self.searched_nodes:
                current_node.terminated = True
                continue

            self.searched_nodes.append(current_node)

            if current_node.data.game_status == Game_State.Won:
                self.finished = True

                return current_node
            if current_node.data.game_status == Game_State.Running:
                children = current_node.get_all_children()

                for child in children:
                    if str(child.data.current_state.num_list) not in fresh_nodes:
                        child.parent.append(current_node)
                        current_node.add_child(child)
                        child.g_value = current_node.g_value + 1
                        child.f_value = child.g_value + Astar_Node.no_of_misplaced_tiles(child)
                        fresh_nodes.add(str(child.data.current_state.num_list))

                        if not self.finished:
                            list.append(child)
                            list.sort(key=lambda x: x.f_value)
                            print(child)
                            graph.node(str(current_node.data.current_state))

                            if child.data.game_status == Game_State.Won:
                                graph.node(str(child.data.current_state), style='filled', color='lightgreen')
                            else:
                                graph.node(str(child.data.current_state))

                            graph.edge(str(current_node.data.current_state), str(child.data.current_state),
                                       label=f"{child.data.move_performed} h:{child.f_value}")
                            graph.render('total_graph', format='png', cleanup=True)

                        if child.data.game_status == Game_State.Won:
                            self.finished = True
