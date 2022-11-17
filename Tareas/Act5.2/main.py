# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

# Función que realiza algortmo de Backtracking con Bitmask
def backtracking_bitmask(matrix):
    dinamicChart = []
    for i in range(len(matrix)):
        temp = []
        for j in range(100):
            if j+1 in matrix[i]:
                temp.append(True)
            else:
                temp.append(False)
        dinamicChart.append(temp)

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

# Función de casos de prueba
def tescase(tc):
    backtracking_bitmask(tc)

# Ejecución de función de programa principal
#main()

# Ejecución de casos de prueba
tc1 = [[5,100,1],[2],[5,100]]
tescase(tc1)