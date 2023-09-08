import graphviz
from space_search import Node, Search
from game import Game, State ,GameState

graph = graphviz.Digraph(comment="The Table")
graph.attr(layout="dot")
graph.attr(dpi="500")


search = Search(
            Node(
                Game(
                    State([2, 4, 6, 7, 3, 1, " ", 5, 8]),
                    State([1, 2, 3, 4, 5, 6, 7, 8, " "]),
                )
            )
        )

results = search.start_single_search_bfs()

nodeList = [search.root]
childrenList = []
parent = []

while nodeList:
  node = nodeList.pop(0)
  color = "lightblue"
  if node.data.gameStatus == GameState.Won:
    color = "green"
    
  graph.node(str(node.data), style="filled", color=color, shape="egg")
  if len(node.parent) > 0:
    for parentNode in node.parent:
      graph.edge(str(parentNode.data), str(node.data), label=str(node.data.movePerformed))
      
  childrenList.extend(node.children)
  if len(nodeList) == 0:
    if len(childrenList) != 0:
      nodeList = childrenList
      childrenList = []
  



# for child in search.root.children:
#   print(child)
#   graph.edge(str(search.root.data), str(child.data), label=str(child.data.movePerformed))
  
graph.render("Missionary Cannibal", format="jpg", view=True)
   
# print (results)
# while len(results.parent) != 0:
#           print(results)
#           results = results.parent[0]

# print(search.root)