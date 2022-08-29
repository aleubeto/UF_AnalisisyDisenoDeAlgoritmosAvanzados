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
def bnb_solution(map):
    return map

#Función para imprimir mapa
def print_map(map):
    print('')
    for i in range(len(map)):
        line = ''
        for j in range(len(map[i])):
            line += f'{map[i][j]} '
        print(line)

#Ejecución
def main():
    m = int(input('m: '))
    n = int(input('n: '))
    map = []
    for i in range(m):
        line = input()
        map.append([int(x) for x in line.split()[:n]])
    #Solución con Backtracking
    backtracking = backtracking_solution(n, m, map)
    print_map(backtracking)
    #Solución con Branch and Bound
    bnb = bnb_solution(map)
    print_map(bnb)

#Casos de prueba
#test1 = [[1,0,0,0], [1,1,0,1], [0,1,0,0], [1,1,1,1]]
#print_map(backtracking_solution(test1))
#print_map(bnb_solution(test1))
main()