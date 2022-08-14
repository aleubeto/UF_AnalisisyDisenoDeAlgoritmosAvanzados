# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

#Mergesort recursivo que ordene de mayor a menor
def merge(left, right):
    i, j = 0, 0
    sorted = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
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

lista =  [2,7,1]
print(DACmergesort(len(lista),lista))

