# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

# n = representa el número de elementos posibles disponibles
# values =  enteros que representan el valor de cada uno de esos elementos
# weights =  enteros que representan los pesos asociados a cada elemento
# w = la capacidad o peso máximo de la mochila

def knapsack(n, values, weights, w): #Orden cuadrático O(n**2)
    K = [[0 for x in range(w+1)] for x in range(n+1)]
    for i in range(n + 1):
        for w in range(w + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i-1] <= w:
                K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][w]

def main(): #Orden lineal O(n)
    n = int(input())
    vals = []
    wgth = []
    for i in range(n):
        vals.append(int(input()))
    for i in range(n):
        wgth.append(int(input()))
    w = int(input())
    print(f'\n{knapsack(n,vals,wgth,w)}')

# Ejecución de programa principal
main()

# Casos de prueba
print(knapsack(3, [1,2,3], [4,5,1], 4))
