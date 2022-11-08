# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

# Función que realiza una busqueda binaria aleatoria

import math
import random

def randomBinarySearch(search, arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = random.randint(start, end)
        if search < arr[mid]:
            end = mid - 1
        elif search > arr[mid]:
            start = mid + 1
        else:
            print("El elemento esta presente en el indice: ", mid)
            return 0 
    print("El elemento no esta presente en el arreglo")
    return 0

# Función que ejecuta programa principal
def main():

    # Inputs del usuario
    search = int(input())
    dataset = input().split(',')
    for i in range(len(dataset)):
        dataset[i] = int(dataset[i])
    randomBinarySearch(search, dataset)
    return 0

# Ejecución de programa principal
main()