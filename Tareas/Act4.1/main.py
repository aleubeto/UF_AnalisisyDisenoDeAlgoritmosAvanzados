# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008


# Importar operador Exclusive Or
from operator import xor

# Función que recibe una lista de 4 puntos/coordenadas
def lines():
    pair = input().split()
    for i in range(len(pair)):
        pair[i] = float(pair[i])
    return pair[:8] #Retornamos los primeros 8 elementos

# Función que retorna la orientación de 3 puntos
def orientation(a,b,c):

    expression = (b[1]-a[1]) * (c[0]-b[0]) - (c[1]-b[1]) * (b[0]-a[0])

    if expression < 0:
        return 'counterclockwise'
    elif expression > 0:
        return 'clockwise'
    else:
        return 'collinear'

# Función booleana que retorna si en 2 rectas hay intersección
def intersection(lines):

    # Definición de puntos
    p1,q1 = (lines[0],lines[1]),(lines[2],lines[3])
    p2,q2 = (lines[4],lines[5]),(lines[6],lines[7])

    # Definición de orientaciones
    o1 = orientation(p1,q1,p2)
    o2 = orientation(p1,q1,q2)
    o3 = orientation(p2,q2,p1)
    o4 = orientation(p2,q2,q1)
    
    # Condiciones
    generalCase = o1 != o2 and o3 != o4
    # specialCase = False / No se implementa
    return generalCase


# Función de programa principal
def main():

    n = int(input())
    matrix = []
    result = []

    # n Inputs del usuario
    for i in range(n):
        matrix.append(lines())

    # Arreglo de booleanos por intersección
    for i in matrix:
        result.append(intersection(i))

    # Salida estándar de solución
    print(result)

# Función de casos de prueba
def testCase(matrix):
    result = []
    for i in matrix:
        result.append(intersection(i))
    return result

# Ejecución del programa principal
main()

# Ejecución de casos de prueba
tc1 =  [[-2,-1,2,2,1,-2,-1,2],
        [-2,-2,2,4,2,-2,0,4],
        [-2,0,0,4,2,0,-2,2],
        [2,-4,0,0,-4,2,-2,-4]]
tc2 =  [[10,10,30,40,30,20,10,40],
        [-4,4,0,0,2,2,0,6],
        [10,40,40,30,30,20,10,50],
        [2,2,12,4,10,2,2,8]]
tc3 =  [[5,-5,10,4,10,-6,5,5],
        [-2,-2,-2,6,-4,8,-4,2],
        [5,-10,0,5,5,0,-5,-5],
        [4,-4,0,0,5,0,-2,-4]]
tc4 =  [[-2,2,2,6,0,10,-4,6],
        [6,-8,8,2,8,-4,-2,2],
        [-4,-4,0,0,2,4,0,6],
        [-4,-2,0,15,4,4,-4,6]]
#print(testCase(tc1))
#print(testCase(tc2))
#print(testCase(tc3))
#print(testCase(tc4))