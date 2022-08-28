#Método 1: Backtracking
def backtracking_solution(map):
    return map

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
        map.append(line.split()[:n])
    #Solución con Backtracking
    backtracking = backtracking_solution(map)
    print_map(backtracking)
    #Solución con Branch and Bound
    bnb = bnb_solution(map)
    print_map(bnb)

#Casos de prueba
#test1 = [[1,0,0,0], [1,1,0,1], [0,1,0,0], [1,1,1,1]]
#print_map(backtracking_solution(test1))
#print_map(bnb_solution(test1))
main()