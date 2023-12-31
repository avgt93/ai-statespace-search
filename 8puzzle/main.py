from space_search import Node, Search
from game import Game, State

START_STATE = [1, 2, 3,4, 5, 6, " ", 7, 8, ]
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
print("5. Misplaced Tiles\n\n")

choice = int(input("Enter your choice: "))

print("\n\n")

if choice == 1:
    search.bfs()
elif choice == 2:
    search.dfs(max_depth=5)    
elif choice == 3:
   search.idfs(5)
elif choice == 4:
     search.a_star_manhattan()
elif choice == 5:
    search.a_star_misplaced_tiles()
else:
    print("Invalid choice")
    exit()





