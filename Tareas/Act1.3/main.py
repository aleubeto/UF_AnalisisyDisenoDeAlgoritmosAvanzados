# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008


#Función para imprimir mapa
def print_map(map):
    print('')
    for i in range(len(map)):
        line = ''
        for j in range(len(map[i])):
            line += f'{map[i][j]} '
        print(line)

#Método 1: Backtracking
def isValid(a, h, map, x, y, res):
    if x >= 0 and y >= 0 and x < h and y < a and map[x][y] == 1 and res[x][y] == 0:
        return True
    return False
 
def RatMaze(a, h, map, move_x, move_y, x, y, res):
    if x == h-1 and y == a-1:
        return True
    for i in range(4):
        x_new = x + move_x[i]
 
        y_new = y + move_y[i]
 
        if isValid(a, h, map, x_new, y_new, res):
 
            res[x_new][y_new] = 1
            if RatMaze(a, h, map, move_x, move_y, x_new, y_new, res):
                return True
            res[x_new][y_new] = 0
    return False

def backtracking_solution(a, h, map):
    res = [[0 for i in range(a)] for i in range(h)]
    res[0][0] = 1

    move_x = [-1, 1, 0, 0]

    move_y = [0, 0, -1, 1]
 
    if RatMaze(a, h, map, move_x, move_y, 0, 0, res):
        return(res)
    else:
        return("Solution does not exist")

#Método 2: Ramificación y poda (branch and bound)
import queue

def newMap(map,path):
    i = 0
    j = 0
    pos = set()
    pos.add((0,0))
    newMap = map
    for move in path:
        if move == 'L':
            i-=1
        elif move == 'R':
            i+=1
        elif move == 'U':
            j-=1
        elif move == 'D':
            j+=1
        pos.add((j,i))
    for j, row in enumerate(map):
        for i, col in enumerate(row):
            if(j,i) in pos:
                newMap[j][i] = '1'
            else:
                newMap[j][i] = '0'
    return newMap

def valid(map,moves):
    i = 0
    j = 0
    for move in moves:
        if move == 'L':
            i-=1
        elif move == 'R':
            i+=1
        elif move == 'U':
            j-=1
        elif move == 'D':
            j+=1
        if not(0 <= i < len(map[0]) and 0 <= j < len(map)):
            return False
        elif(map[j][i] == '0'):
            return False
    return True

def findEnd(map,moves):
    i = 0
    j = 0
    for move in moves:
        if move == 'L':
            i-=1
        elif move == 'R':
            i+=1
        elif move == 'U':
            j-=1
        elif move == 'D':
            j+=1
    if i==len(map[0])-1 and j==len(map)-1:
        result = newMap(map,moves)
        print_map(result)
        return True
    return False

def bnb_solution(map):
    nums = queue.Queue()
    nums.put('')
    path=''
    while not findEnd(map,path):
        path = nums.get()
        for j in ['L','R','U','D']:
            put = path + j
            if valid(map,put):
                nums.put(put)

#Ejecución
def main():
    m = int(input())
    n = int(input())
    map1 = []
    map2 = []
    for i in range(m):
        line = input()
        map1.append([int(x) for x in line.split()[:n]])
        map2.append(line.split()[:n])
    #Solución con Backtracking
    backtracking = backtracking_solution(n, m, map1)
    print_map(backtracking)
    #Solución con Branch and Bound
    bnb = bnb_solution(map2)

#Casos de prueba
#test1 = [['1','0','0','0'],['1','1','0','1'], ['0','1','0','0'], ['1','1','1','1']]
#bnb_solution(test1)
#print_map(backtracking_solution(len(test1),len(test1),test1))
main()