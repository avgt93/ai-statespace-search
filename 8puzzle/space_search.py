import bisect
from game import GameState, ActionSpace, Game, State
from collections import deque
import copy
import math
import graphviz

graph = graphviz.Digraph(comment="The Table")
graph.attr(layout="dot")
graph.attr(dpi="500")

class AstarNode:
    @staticmethod
    def manhatten_distance(node):
        manhattendist=0
        for k in range(1,9):
            actual_index=node.data.current_state.numList.index(k)
            i=math.floor(actual_index/3)
            j=actual_index-3*i

            goal_index=node.data.goal_state.numList.index(k)    
            encoded_i=math.floor(goal_index/3)
            encoded_j= goal_index -3 * encoded_i

            manhattendist = manhattendist+ abs(i-encoded_i)+abs(j-encoded_j)
        index= node.data.current_state.numList.index(" ")
        i=math.floor(index/3)
        j=index-3*i

        goal_index=node.data.goal_state.numList.index(" ")
        encoded_i=math.floor(goal_index/3)
        encoded_j= goal_index -3 *encoded_i

        return manhattendist+abs(i-encoded_i)+abs(j-encoded_j)
    
    @staticmethod
    def no_of_misplaced_tiles(node):
        misplaced=0
        for k in range(1,9):
            if node.data.current_state.numList.index(k) != node.data.goal_state.numList.index(k):
                misplaced+=1

            if node.data.current_state.numList.index(" ") != node.data.goal_state.numList.index(" "):
                misplaced+=1
            
            return misplaced

class Node:
    def __init__(self, state: Game):
        self.data = state
        self.parent = []
        self.children = []
        self.terminated = False
        self.goal = False

    def __eq__(self, other):
        if isinstance(other, Node):
            if self.data.current_state.numList == other.data.current_state.numList:
                return True
            else:
                return False

        return False

    def __str__(self):
        return f"Move Performed: {self.data.movePerformed} Node:\n{self.data}"

    def add_child(self, child_node):
        self.children.append(child_node)

    def get_all_children(self):
        child_list = []

        game = copy.deepcopy(self.data)
        can_move = game.move(ActionSpace.MoveLeft)
        if can_move:
            node = Node(game)
            child_list.append(node)

        game = copy.deepcopy(self.data)
        can_move = game.move(ActionSpace.MoveUp)
        if can_move:
            node = Node(game)
            child_list.append(node)

        game = copy.deepcopy(self.data)
        can_move = game.move(ActionSpace.MoveDown)
        if can_move:
            node = Node(game)
            child_list.append(node)

        game = copy.deepcopy(self.data)
        can_move = game.move(ActionSpace.MoveRight)
        if can_move:
            node = Node(game)
            child_list.append(node)
        return child_list
    



class Search:
    def __init__(self, root: Node):
        self.root = root
        self.finished = False
        self.searchedNodes = []  
        self.graphvize=['digraph G {']  


    def start_search_bfs(self):
        queue = []
        queue.append(self.root)

        while queue:
            current_node = queue.pop(0)

            if current_node in self.searchedNodes:
                continue

            self.searchedNodes.append(current_node)

            if current_node.data.gameStatus == GameState.Won:
                continue

            if current_node.data.gameStatus == GameState.Running:
                children = current_node.get_all_children()
                for child in children:
                    if child not in current_node.parent:
                        child.parent.append(current_node)
                        current_node.add_child(child)
                        if child not in self.searchedNodes:
                            queue.append(child)

    def start_single_search_bfs(self):
        print("Performing Breadth First Search\n")
        generatedNodes=set()
        generatedNodes.add(str(self.root.data.current_state.numList))
        queue = []
        queue.append(self.root)

        # self.graphvize.append(f'{str(self.root)};')
        # graph.node(str(self.root), label=str(self.root.data))


        count=0
        while queue:
            current_node = queue.pop(0)
            if current_node in self.searchedNodes:
                continue

            count+=1

            self.searchedNodes.append(current_node)

            if current_node.data.gameStatus == GameState.Running:                
                children = current_node.get_all_children()
                for child in children:   
                    if str(child.data.current_state.numList) not in generatedNodes:
                        generatedNodes.add(str(child.data.current_state.numList))
                        print(child)
                        graph.node(str(current_node.data.current_state))
                        if child.data.gameStatus==GameState.Won:
                            graph.node(str(child.data.current_state), style='filled', color='lightgreen')
                        else:
                            graph.node(str(child.data.current_state))
                        # check garna pryo yaha
                        graph.edge(str(current_node.data.current_state), str(child.data.current_state), label=f"{child.data.movePerformed}")
                        
                        graph.render('bfs_graph', format='png', cleanup=True)

                        queue.append(child)

                        if child.data.gameStatus==GameState.Won:
                            self.graphvize.append(f'"{str(child.data.current_state)}" [style=filled, color=lightgreen]}}')
                            self.finished = True
                            print(f"Total Number of States:{count}")
                            return child            
                        
                     

    def start_search_dfs(self):
        stack = []
        stack.append(self.root)

        while stack:
            current_node = stack.pop(0)
            if current_node in self.searchedNodes:
                current_node.terminated = True
                continue

            self.searchedNodes.append(current_node)

            if current_node.data.gameStatus == GameState.Won:
                continue

            if current_node.data.gameStatus == GameState.Running:
                children = current_node.get_all_children()
                temp = []
                for child in children:
                    if child not in self.searchedNodes:
                        child.parent.append(current_node)
                        current_node.add_child(child)
                        temp.append(child)

                stack = [*temp, *stack]

    def start_single_search_dfs(self):
        print("Performing Depth First Search\n")
        generatedNodes=set()
        generatedNodes.add(str(self.root.data.current_state.numList))
        stack = []
        stack.append({"node": self.root, "depth": 0})
        print(self.root)
        
        count=0
        while stack:
            current_node = stack.pop(0)
            current_node=current_node["node"]

            if current_node in self.searchedNodes:
                continue

            count+=1
            self.searchedNodes.append(current_node)

            if (count %100 ==0):
                print(f"no of states generated:{count}")


            if current_node.data.gameStatus == GameState.Running:
                children = current_node.get_all_children()
                temp = []
                for child in children:
                    if str(child.data.current_state.numList) not in generatedNodes:
                        generatedNodes.add(str(child.data.current_state.numList))
                        print(child)
                        graph.node(str(current_node.data.current_state))

                        if child.data.gameStatus==GameState.Won:
                            graph.node(str(child.data.current_state), style='filled', color='lightgreen')
                        else:
                            graph.node(str(child.data.current_state))

                        graph.edge(str(current_node.data.current_state), str(child.data.current_state), label=f"{child.data.movePerformed}")
                        graph.render('dfs_graph', format='png', cleanup=True)


                        temp.append({"node": child, "depth":2})
                        
                        if child.data.gameStatus == GameState.Won:
                            self.finished = True
                            print(f"Total Number of States:{count}")
                            return child

                stack = [*temp, *stack]


    def start_idfs(self, max_depth: int):
        print("Performing Iterative Deepening Search\n")
        for depth in range(1, max_depth + 1):
            generatedNodes=set()
            generatedNodes.add(str(self.root.data.current_state.numList))

            print(self.root)
          
            result = self.depth_limited_search(self.root, depth, generatedNodes, depth)
        
            if result is not None:
                return result

    def depth_limited_search(self, node, depth, generatedNodes, current_depth):
    
        if depth == 0:
            if node.data.gameStatus == GameState.Won:
                self.finished = True
                return node
            return None

        if node in self.searchedNodes:
            node.terminated=True

        self.searchedNodes.append(node)

        if node.data.gameStatus == GameState.Running:
           children=node.get_all_children()
           for child in children:
               if str(child.data.current_state.numList) not in generatedNodes:
                   generatedNodes.add(str(child.data.current_state.numList))
                   print(child)
                   graph.node(str(node.data.current_state))
                   if child.data.gameStatus==GameState.Won:
                    graph.node(str(child.data.current_state), style='filled', color='lightgreen')
                   else:
                        graph.node(str(child.data.current_state))

                   graph.edge(str(node.data.current_state), str(child.data.current_state), label=f"{child.data.movePerformed}")
                   graph.render('idfs_graph', format='png', cleanup=True)

                   child.parent.append(node)
                   node.add_child(child)
                   result=self.depth_limited_search(child, depth=depth-1, generatedNodes=generatedNodes, current_depth=current_depth)
                   if result is not None:
                       return result


    def start_manhattan(self):
        print("Performing A* Search with Manhattan Distance\n")
        self.root.g_value=0
        self.root.f_value=AstarNode.manhatten_distance(self.root)
        list=[]
        list.append(self.root)  
        generatedNodes=set()
        generatedNodes.add(str(self.root.data.current_state.numList))
        print(self.root)    

        count=0
        while list:
            count +=1
            current_node=list.pop(0)
            if current_node in self.searchedNodes:
                current_node.terminated=True
                continue

            self.searchedNodes.append(current_node)

            if current_node.data.gameStatus == GameState.Won:
                self.finished = True
                print(f"Total Number of nodes Expanded:{count}")
                return current_node

            if current_node.data.gameStatus == GameState.Running:   
                children = current_node.get_all_children()
                for child in children:
                    if str(child.data.current_state.numList) not in generatedNodes:
                        child.parent.append(current_node)
                        current_node.add_child(child)   
                        child.g_value=current_node.g_value+1
                        child.f_value=AstarNode.manhatten_distance(child) + child.g_value 

                        generatedNodes.add(str(child.data.current_state.numList))

                        if not self.finished:
                          
                            print(child)
                            
                            graph.node(str(current_node.data.current_state))
                            graph.node(str(child.data.current_state))
                            if child.data.gameStatus==GameState.Won:
                                graph.node(str(child.data.current_state), style='filled', color='lightgreen')
                            else:
                                graph.node(str(child.data.current_state))
                            graph.edge(str(current_node.data.current_state), str(child.data.current_state), label=f"{child.data.movePerformed} h:{child.f_value}")
                            graph.render('manhattan_graph', format='png', cleanup=True)
                            

                        if child.data.gameStatus==GameState.Won:
                            self.finished = True
                            print(f"Total Number of States:{count}")
                        bisect.insort(list, child, key=lambda x: x.f_value)
                        
    def start_misplacedtiles(self):
        print("Performing A* Search with Misplaced Tiles\n")
        self.root.g_value=0
        self.root.f_value=AstarNode.no_of_misplaced_tiles(self.root)
        list=[]
        list.append(self.root)
        generatedNodes=set()
        generatedNodes.add(str(self.root.data.current_state.numList))
        print(self.root)    

        count=0 
        while list:
            count+=1
            current_node=list.pop(0)
            if current_node in self.searchedNodes:
                current_node.terminated=True
                continue

            self.searchedNodes.append(current_node)

            if current_node.data.gameStatus == GameState.Won:
                self.finished = True
                print(f"Total Number of States:{count}")
                return current_node
            
            if current_node.data.gameStatus==GameState.Running:
                children=current_node.get_all_children()
                for child in children:
                    if str(child.data.current_state.numList) not in generatedNodes:
                        child.parent.append(current_node)
                        current_node.add_child(child)   
                        child.g_value=current_node.g_value+1
                        child.f_value=child.g_value+AstarNode.no_of_misplaced_tiles(child)

                        generatedNodes.add(str(child.data.current_state.numList))

                        if not self.finished:
                            list.append(child)
                            list.sort(key=lambda x: x.f_value)
                            print(child)    
                            
                            graph.node(str(current_node.data.current_state))
                            if child.data.gameStatus==GameState.Won:
                                graph.node(str(child.data.current_state), style='filled', color='lightgreen')
                            else:
                                graph.node(str(child.data.current_state))
                            graph.edge(str(current_node.data.current_state), str(child.data.current_state), label=f"{child.data.movePerformed} h:{child.f_value}")
                            graph.render('total_graph', format='png', cleanup=True)

                        if child.data.gameStatus==GameState.Won:
                            self.finished = True
                           




# search = Search(
#             Node(
#                 Game(
#                     State([2, 4, 6, 7, 3, 1, " ", 5, 8]),
#                     State([1, 2, 3, 4, 5, 6, 7, 8, " "]),
#                 )
#             )
#         )

# results = search.start_single_search_bfs()
# while len(results.parent) != 0:
#           print(results)
#           results = results.parent[0]

# print(search.root)
