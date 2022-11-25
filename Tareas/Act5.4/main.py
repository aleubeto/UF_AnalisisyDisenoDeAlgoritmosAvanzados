# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

# Librerías
import bisect

# Función que recibe un conjunto de n elementos
def lines(n):
    elements = input('set = ').split(',')
    for i in range(len(elements)):
        elements[i] = int(elements[i])
    return elements[:n] #Retornamos los primeros n elementos

# Función que calcula la suma de los subconjuntos posibles en un conjunto
def sumSubarray(set, n, index):
    subsets = []
    for i in range((1 << n)):   # 2**n (subconjuntos totales)
        s = 0
        for j in range(n):
            if (i & (1 << j)):  # Bitmasking con operador &
                s += set[j + index]
        subsets.append(s)
    return subsets

# Función que implementa algoritmo "meet in the middle"
def meet_in_middle(set,s):
    half1 = sumSubarray(set,len(set)//2,0)
    half2 = sumSubarray(set,len(set)-len(set)//2,len(set)//2)
    half2.sort()    # Ordenamiento de segunda mitad
    max = 0

    for i in range(len(half1)):
        if half1[i] <= s:
            p = bisect.bisect_left(half2,s-half1[i])
            if p==len(half2) or p<len(half2) and half2[p] != s-half1[i]:
                p-=1
            if (half2[p]+half1[i] > max):
                max = half2[p]+half1[i]
    return max

# Función que ejecuta programa principal
def main():
    n = int(input('n = '))
    set = lines(n)
    s = int(input('s = '))
    print(meet_in_middle(set,s))

# Función que ejecuta casos de prueba
def tc(set,s):
    print(meet_in_middle(set,s))

# Ejecución de programa principal
# main()

# Ejecución de casos de prueba
tc([45, 34, 4, 12, 5, 2],42)   #tc1
tc([3, 34, 4, 12, 5, 2],10)   #tc2
tc([9, 11, 5, 8, 4, 40],17)   #tc3
tc([1, 3, 2, 10, 6, 20, 22],23)   #tc4