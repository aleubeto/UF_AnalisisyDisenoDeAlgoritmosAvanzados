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

    sigma = (b[1]-a[1])/(b[0]-a[0]) # pendiente de a-b
    tau = (c[1]-b[1])/(c[0]-b[0])   # pendiente de b-c

    if sigma < tau:
        return 'counterclockwise'
    elif sigma > tau:
        return 'clockwise'
    else:
        return 'collinear'

# Función booleana que retorna si en 2 rectas hay intersección
def intersection(lines):

    # Definición de puntos
    p1,q1 = (lines[0],lines[1]),(lines[2],lines[3])
    p2,q2 = (lines[4],lines[5]),(lines[6],lines[7])

    # Condiciones
    generalCase = orientation(p1,q1,p2) != orientation(p1,q1,q2) and orientation(p2,q2,p1) != orientation(p2,q2,q1)
    specialCase = False
    return xor(generalCase,specialCase)


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
tc1 = [[],[],[],[]]
tc2 = [[],[],[],[]]
tc3 = [[],[],[],[]]
tc4 = [[],[],[],[]]
# print(testCase(tc1))
# print(testCase(tc1))
# print(testCase(tc1))
# print(testCase(tc1))