# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

# Función que implementa algoritmo Hill-climbing
def hillclimbing(n):
    # A TRABAJAR!!!
    return []

# Función que imprime el resultado
def printresult(result):
    for i in result:
        print(i)

# Función que ejecuta programa principal
def main():
    n = int(input())
    solution = hillclimbing(n)
    printresult(solution)

# Función que ejecuta un caso de prueba
def tc(testcase):
    solution = hillclimbing(testcase)
    printresult(solution)

# Ejecución de programa principal
main()

# Ejecución de casos de prueba
tc(4)   #tc1
tc(8)   #tc2