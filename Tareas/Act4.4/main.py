# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

import math
import random

# Función que realiza una busqueda binaria aleatoria
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
            return f"El elemento esta presente en el indice: {mid}"
    return "El elemento no esta presente en el arreglo"

# Función que ejecuta programa principal
def main():

    # Inputs del usuario
    search = int(input())
    dataset = input().split(',')
    for i in range(len(dataset)):
        dataset[i] = int(dataset[i])
    print(randomBinarySearch(search, dataset))

# Función de casos de prueba
def testcase(s,d):
    print(randomBinarySearch(s,d))

# Ejecución de programa principal
main()

# Ejecución de casos de prueba
testcase(10,[2,3,4,10,40])  #1
testcase(11,[2,3,4,10,40])  #2
testcase(6,[1,3,6,7,2,20])  #3
testcase(3,[1,3,5,20,100])  #4