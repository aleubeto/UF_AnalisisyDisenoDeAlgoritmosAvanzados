# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

# Función que realiza algortmo de Backtracking con Bitmask
def backtracking_bitmask(matrix):
    return matrix   # A trabajar!!!

# Función de programa principal
def main():
    n = int(input())
    restriction = 1<=n and n<=10
    people = []
    if restriction:

        # Inputs del usuario
        for i in range(n):
            colection = input().split()
            for j in range(len(colection)):
                colection[j] = int(colection[j])
            people.append(colection)

        # Backtracking con Bitmask
        backtracking_bitmask(people)

    else:
        print('> El número ingresado no cumple con la restricción 1<=n<=10')

# Ejecución de función de programa principal
main()