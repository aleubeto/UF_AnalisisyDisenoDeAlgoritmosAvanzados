# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008


# Función que recibe una lista de 4 puntos/coordenadas
def lines():
    pair = input().split()
    return pair[:8] #Retornamos los primeros 8 elementos

# Función booleana que retorna si en 2 rectas hay intersección
def intersection(lines):
    return True # A CURRAR!!!

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