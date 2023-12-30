import graphviz
from space_search import Node, Search
from game import Game, State ,GameState
from collections import deque

graph = graphviz.Digraph(comment="The Table")
graph.attr(layout="dot")
graph.attr(dpi="500")


search = Search(
            Node(
                Game(
                    # State([1, 2 , 3," ", 4 ,6, 7,5, 8]),
                    State([7,2,4,5," ",6,8,3,1]),

                    # State([1, 2 , 3, 4 , 5,6," " , 7, 8]),
                    # State([1, 2 , 3, 4 , " " ,5, 7, 8, 6]),
                    State([" ", 1, 2, 3, 4, 5, 6, 7, 8]),
                    # State([1, 2, 3, 4, 5, 6, " ", 7, 8]),


                )
            )
        )

# results = search.start_single_search_bfs()
# graph = graphviz.Source(search.graphvize)

# graph.render('output_graph', format='png', cleanup=True)



# for node in results:
#     graph.node(str(node.data))

# if node.parent:
#     graph.edge(str(node.parent.data), str(node.data))

# # Render and display the graph
# graph.view()

print("Welcome")
print("You are playing 8 puzzle game. Your options are:")
print("1. Breadth First Search")
print("2. Depth First Search")
print("3. Iterative Deepening Search")
print("4. Manhattan Distance")
print("5.Misplaced Tiles")
print()

choice = int(input("Enter your choice: "))

print()

if choice == 1:
    results = search.start_single_search_bfs()
elif choice == 2:
    results = search.start_single_search_dfs()    
elif choice == 3:
    results = search.start_idfs(5)
elif choice == 4:
    results = search.start_manhattan()
elif choice == 5:
    results = search.start_misplacedtiles()
else:
    print("Invalid choice")
    exit()






# def recuresive(node):
#   varr=node.get_all_children();
#   print(node)
#   if varr != []:
#     for i in node.children:
#       recuresive(i)
# recuresive(search.root)



# def visualize_bfs_search(root):
#     graph = graphviz.Digraph('BFS_Tree')
#     queue = deque([(None, root)])  # (parent, current_node)

#     while queue:
#         parent, current_node = queue.popleft()

#         if current_node is not None:
#             graph.node(str(current_node), label=str(current_node.data))
#             if parent is not None:
#                 graph.edge(str(parent), str(current_node))

#         children = current_node.get_all_children() if current_node else []
#         queue.extend((current_node, child) for child in children)

#     return graph

# # Assuming search.root is the root node of your tree
# bfs_graph = visualize_bfs_search(search.root)

# # Save the graph to a file (e.g., in PNG format)
# bfs_graph.render('bfs_graph', format='png', cleanup=True)



   




