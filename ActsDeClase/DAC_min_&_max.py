#Valor mínimo de un arreglo DAC recursivo
def DACmin(array, index, n):

	#Caso base 1; Array de un solo elemento
	if(n-1 == 0):
		return array[index]

	#Caso base 2: Array de dos elementos
	if(index >= n-2):
		if(array[index] < array[index+1]):
			return array[index]
		return array[index+1]

	#Llamada recursiva
	min = DACmin(array, index+1, n)
	if(array[index] < min):
		return array[index]
	else:
		return min

#Ejemplo de ejecución
lista = [41,12,22,1,6]
print(DACmin(lista,0,len(lista)))

#Valor máximo de un arreglo DAC recursivo
def DACmax(array, index, n):

	#Caso base 1; Array de un solo elemento
	if(n-1 == 0):
		return array[index]

	#Caso base 2: Array de dos elementos
	if(index >= n-2):
		if(array[index] > array[index+1]):
			return array[index]
		return array[index+1]

	#Llamada recursiva
	min = DACmax(array, index+1, n)
	if(array[index] > min):
		return array[index]
	else:
		return min

#Ejemplo de ejecución
lista = [41,12,22,1,6]
print(DACmax(lista,0,len(lista)))