# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

# Función que realiza algoritmo de A*
def a_star(matrix):
    return matrix   #A TRABAJARRRRRRR

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

    print(a_star(matrix))

# Función de casos de prueba
def tc(matrix):
    print(a_star(matrix))

# Ejecución de programa principal
# main()

# Ejecución de casos de prueba
tc1 = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
tc(tc1)
tc2 = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
tc(tc2)
tc3 = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
tc(tc3)
tc4 = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
tc(tc4)