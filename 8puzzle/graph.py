import graphviz
from space_search import Node, Search
from game import Game, State ,GameState
from collections import deque

graph = graphviz.Digraph(comment="The Table")
graph.attr(layout="dot")
graph.attr(dpi="500")

START_STATE = [1, 2, 3, 4, 8, " ", 7, 6, 5]
GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, " "]
start_state = State(START_STATE)
goal_state = State(GOAL_STATE)
game = Game(start_state, goal_state)
node = Node(game)

search = Search(node)



print("Welcome")
print("You are playing 8 puzzle game. Your options are:")
print("1. Breadth First Search")
print("2. Depth First Search")
print("3. Iterative Deepening Search")
print("4. Manhattan Distance")
print("5. Misplaced Tiles")
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





