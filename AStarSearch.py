class Node:
    def __init__(self, up, down, left, right):
        self.parent = None                  # Back tracking
        self.y, self.x = 0, 0
        
        self.up = up                        # Bool values to see if which direction we can take
        self.down = down
        self.left = left
        self.right = right
        
        self.heuristic = 0                  # Function cost for f(n) = g(n) + h(n)
        self.g = 0
        self.f = 0
                  # If true, set a variable inside explore that return always ["up","down","left","right"]
        return

    def availableDirection(self):
        direction = []
        if self.up:
            direction.append("up")
        if self.down:
            direction.append("down")
        if self.left:
            direction.append("left")
        if self.right:
            direction.append("right")
        return direction

'''
                SETTING THE GRAPH
        True = I can go in that direction 
        Fale = I can't go in that direction
        graph[y].append(up, down, left, right) for each colum
'''
def defineGraph():                          # Set the wall in the maze
    graph = []
    graph.append([Node(0,1,0,0), Node(0,1,0,1), Node(0,0,1,1), Node(0,0,1,1), Node(0,1,1,1), Node(0,0,1,1), Node(0,0,1,1), Node(0,1,1,0), Node(0,1,0,1), Node(0,1,1,0), Node(0,1,0,1), Node(0,1,1,0), Node(0,1,0,1), Node(0,1,1,0), Node(0,1,0,0)])
    graph.append([Node(1,1,0,0), Node(1,1,0,0), Node(0,1,0,1), Node(0,0,1,0), Node(1,1,0,0), Node(0,0,0,1), Node(0,1,1,0), Node(1,1,0,0), Node(1,0,0,0), Node(1,1,0,1), Node(1,1,1,0), Node(1,1,0,0), Node(1,0,0,0), Node(1,0,0,1), Node(1,1,1,0)])
    graph.append([Node(1,1,0,1), Node(1,0,1,0), Node(1,0,0,1), Node(0,1,1,0), Node(1,0,0,1), Node(0,1,1,0), Node(1,1,0,0), Node(1,0,0,1), Node(0,0,1,1), Node(1,0,1,0), Node(1,0,0,0), Node(1,1,0,0), Node(0,1,0,1), Node(0,1,1,0), Node(1,1,0,0)])
    graph.append([Node(1,0,0,1), Node(0,0,1,1), Node(0,1,1,0), Node(1,0,0,1), Node(0,1,1,0), Node(1,0,0,1), Node(1,0,1,1), Node(0,0,1,1), Node(0,1,1,0), Node(0,1,0,1), Node(0,1,1,0), Node(1,1,0,1), Node(1,0,1,0), Node(1,1,0,0), Node(1,1,0,0)])
    graph.append([Node(0,1,0,0), Node(0,1,0,1), Node(1,0,1,0), Node(0,1,0,0), Node(1,0,0,1), Node(0,1,1,0), Node(0,1,0,1), Node(0,1,1,0), Node(1,0,0,1), Node(1,0,1,0), Node(1,1,0,0), Node(1,1,0,0), Node(0,1,0,0), Node(1,0,0,1), Node(1,0,1,0)])
    graph.append([Node(1,1,0,0), Node(1,0,0,1), Node(0,0,1,1), Node(1,1,1,0), Node(0,1,0,1), Node(1,0,1,0), Node(1,1,0,0), Node(1,1,0,0), Node(0,0,0,1), Node(0,1,1,0), Node(1,1,0,0), Node(1,1,0,0), Node(1,1,0,0), Node(0,1,0,1), Node(0,1,1,0)])
    graph.append([Node(1,1,0,1), Node(0,0,1,1), Node(0,0,1,1), Node(1,0,1,1), Node(1,0,1,1), Node(0,1,1,0), Node(1,1,0,0), Node(1,0,0,1), Node(0,0,1,1), Node(1,0,1,0), Node(1,1,0,0), Node(1,1,0,0), Node(1,0,0,1), Node(1,0,1,0), Node(1,1,0,0)])
    graph.append([Node(1,1,0,0), Node(0,1,0,0), Node(0,1,0,1), Node(0,0,1,0), Node(0,1,0,1), Node(1,0,1,1), Node(1,0,1,0), Node(0,1,0,1), Node(0,1,1,0), Node(0,1,0,1), Node(1,0,1,0), Node(1,0,0,1), Node(0,0,1,1), Node(0,0,1,1), Node(1,0,1,0)])
    graph.append([Node(1,0,0,1), Node(1,1,1,0), Node(1,0,0,1), Node(0,1,1,1), Node(1,0,1,0), Node(0,0,0,1), Node(0,1,1,0), Node(1,1,0,0), Node(1,1,0,0), Node(1,0,0,1), Node(0,0,1,1), Node(0,0,1,1), Node(0,0,1,1), Node(0,0,1,1), Node(0,1,1,0)])
    graph.append([Node(0,0,0,1), Node(1,0,1,1), Node(0,0,1,0), Node(1,0,0,1), Node(0,0,1,1), Node(0,0,1,1), Node(1,0,1,0), Node(1,0,0,0), Node(1,0,0,1), Node(0,0,1,1), Node(0,0,1,1), Node(0,0,1,1), Node(0,0,1,1), Node(0,0,1,1), Node(1,0,1,0)])
    defineHeuristic(graph)
    yandx(graph)
    return graph

def yandx(graph):                                            # defining the y & x for each node
    for row in range(10):
        for colum in range(15):
            graph[row][colum].y, graph[row][colum].x  = row, colum

def defineHeuristic(graph):                                 # the function define an heuristic value for this tipe of graph
    for i in range(10):
        graph[9 - i][7].heuristic = i ** 2
        for j in range(1, 8):
            graph[9 - i][7 + j].heuristic = (j + i) ** 2
        for k in range(7):
            graph[9 - i][k].heuristic = (7 + i - k) ** 2

def printHeuristic(graph):                                  # this function prints a table of the heuristic value holded by the graph
    for i in range(10):
        for k in range(15):
            print("\t",graph[i][k].heuristic, end=" ")
        print()
        print()
        print()

def explore(graph, node):                                   # siblings will be returned to APath()
    siblings = []
    for i in node.availableDirection():
        if i is "up":
            siblings.append(graph[node.y - 1][node.x])
        elif i is "down":
            siblings.append(graph[node.y + 1][node.x])
        elif i is "left":
            siblings.append(graph[node.y][node.x - 1])
        elif i is "right":
            siblings.append(graph[node.y][node.x + 1])
    return siblings

def parentCost(child, current):
    child.parent = current
    child.g = current.g + 1
    child.f = child.g + child.heuristic
    return

def pathRevering(node):
    path = []
    while node is not None:
        path.append(node)
        node = node.parent
    return path[::-1]

def APath(graph, start, end):
    openList = []                                           # Nodes expanded, will be choosen the one with less f cost
    closedList = []                                         # Nodes visited with current node list
    currentNode = start
    openList.append(start)

    while openList != []:
        currentNode = openList[0]
        index = 0                                           # index is used to store in wich location of the array current node is stored

        for i, node in enumerate(openList):
            if currentNode.f > node.f:
                currentNode = node
                index = i
        
        if currentNode == end:                              # In case current node is the end node we find the path
            return pathRevering(currentNode)


        openList.pop(index)                                 # Poping the current node from the list
        closedList.append(currentNode)                      # Appending it to the nodes can't be visited again
        siblings = explore(graph, currentNode)              # List of adjacent nodes 

        
        for child in siblings:                              # loop through all adjacent nodes
            if child in closedList: continue                # don't take any action for this adjacent node

            parentCost(child, currentNode)                  # linking these two nodes

            if child not in openList:
                openList.append(child)

def printPath(path):
    print("----     PATH     ----")
    for node in path:
        print(f"Node[{node.y}][{node.x}] \tf(n) = {node.g} + {node.heuristic} = {node.f}\n   ↓")



start, end = (0,7) , (9,7)
graph = defineGraph()
printHeuristic(graph)
path = APath(graph, graph[start[0]][start[1]], graph[end[0]][end[1]])
printPath(path)

