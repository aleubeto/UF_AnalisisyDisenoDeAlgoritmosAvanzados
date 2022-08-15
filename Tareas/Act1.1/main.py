# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

#Mergesort recursivo que ordene de mayor a menor
def merge(left, right):
    i, j = 0, 0
    sorted = []
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1

    sorted += left[i:]
    sorted += right[j:]
    return sorted

#Función que ordena array de elementos aplicando función recursiva
def DACmergesort(n, array):

    #Caso base: no es posible dividir más el array
    if (n<=1):
        return array

    else:
        mid = n//2
        left_array = DACmergesort(len(array[:mid]),array[:mid])
        right_array = DACmergesort(len(array[mid:]),array[mid:])
        return merge(left_array, right_array)

prueba1 = []
prueba2 = [2]
prueba3 = [6,3]
prueba4 = [2,6,8,3,4,0,-2,4]

print(DACmergesort(len(prueba1),prueba1))
print(DACmergesort(len(prueba2),prueba2))
print(DACmergesort(len(prueba3),prueba3))
print(DACmergesort(len(prueba4),prueba4))



