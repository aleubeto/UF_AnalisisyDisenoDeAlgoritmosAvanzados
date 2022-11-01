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

# Ejecución de programa principal
main()