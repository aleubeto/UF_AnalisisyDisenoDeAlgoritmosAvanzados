# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

# Función de ejecución del programa principal
def main():

    # Declaración de variables
    n = int(input())
    dots = []

    # Entrada de puntos por parte del usuario
    for i in range(n):
        newDot = input().split(',')
        for j in range(len(newDot)):
            newDot[j] = int(newDot[j])
        dots.append(tuple(newDot))
    print(dots)

# Función de casos de prueba
def testcase(dots):
    return dots

# Ejecución de programa principal
main()

# Ejecución de casos de prueba
tc1 = [(1, 2), (3, 4), (5, 6), (5, 6), (5, 6)]
tc2 = [(1, 2), (3, 4), (5, 6), (5, 6), (5, 6)]
tc3 = [(1, 2), (3, 4), (5, 6), (5, 6), (5, 6)]
tc4 = [(1, 2), (3, 4), (5, 6), (5, 6), (5, 6)]
#testcase(tc1)
#testcase(tc2)
#testcase(tc3)
#testcase(tc4)