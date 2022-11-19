# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

# Función que realiza algoritmo de A*
class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def a_star(maze):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    start = (0,0)
    end = (len(maze)-1, len(maze)-1)
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        print(f'open list = {len(open_list)}')

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares
            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 1:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            if len([open_node for open_node in open_list if child.position == open_node.position and child.g > open_node.g]) > 0:
                continue
            # Add the child to the open list
            open_list.append(child)
    return None

# Función que recibe una lista de 4 puntos/coordenadas
def lines():
    pair = input().split()
    for i in range(len(pair)):
        pair[i] = int(pair[i])
    return pair[:4] #Retornamos los primeros 4 elementos

# Función de programa principal
def main():

    n = int(input())
    matrix = []

    # n Inputs del usuario
    for i in range(n):
        matrix.append(lines())
    
    path = a_star(matrix)
    if path == None:
        print("None")
    else:
        start = (0,0)
        answer = ""
        for i in path:
            if i == start:
                continue
            if i[0] > start[0]:
                answer += "D"
                start = i
            elif i[0] < start[0]:
                answer += "U"
                start = i
            elif i[1] > start[1]:
                answer += "R"
                start = i
            elif i[1] < start[1]:
                answer += "L"
                start = i
        print(answer)

# Función de casos de prueba
def tc(matrix):
    path = a_star(matrix)
    if path == None:
        print("None")
    else:
        start = (0,0)
        answer = ""
        for i in path:
            if i == start:
                continue
            if i[0] > start[0]:
                answer += "D"
                start = i
            elif i[0] < start[0]:
                answer += "U"
                start = i
            elif i[1] > start[1]:
                answer += "R"
                start = i
            elif i[1] < start[1]:
                answer += "L"
                start = i
        print(answer)

# Ejecución de programa principal
main()

# Ejecución de casos de prueba
tc1 =  [[1,0,0,0],
        [1,1,0,1],
        [1,1,0,0],
        [0,1,1,1]]
#tc(tc1)
tc2 = [[1,1,0,0,0], [0,1,1,0,0],
                    [0,1,1,1,0],[0,1,1,1]]
#tc(tc2)
tc3 = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
#tc(tc3)
tc4 = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
#tc(tc4)