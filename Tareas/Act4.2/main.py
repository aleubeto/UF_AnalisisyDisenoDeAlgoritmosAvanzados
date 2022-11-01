# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

from functools import cmp_to_key

#Clase punto donde se almacenan las coordenadas x & y
class Dot:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

#Objeto global punto(0,0) utilizado como margen de referencia        
p0 = Dot(0, 0)

def nextToTop(S):
    	return S[-2]

#Función de distancia entre dos puntos
def distancia(p1, p2):
    	return ((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))

#Función orientación entre 3 puntos dados
def orientacion(p, q, r):
    val = ((q.y - p.y) * (r.x - q.x) -(q.x - p.x) * (r.y - q.y))
    if val == 0:
        # orientación colineal
        return 0 
    elif val > 0:
        # orientación a favor de las manecillas del reloj
        return 1 
    else:
        # orientación en contra de las manecillas del reloj
        return 2 

#Función compara para ordenar un arreglo de puntos respecto al punto (0,0)
def compara(p1, p2):
    
	# Find orientation
	a = orientacion(p0, p1, p2)
	if a == 0:
		if distancia(p0, p2) >= distancia(p0, p1):
			return -1
		else:
			return 1
	else:
		if a == 2:
			return -1
		else:
			return 1

#Función que encuentra el polígono convexo del conjunto de puntos dados
def convexo(array, n):
    ymin = array[0].y
    min = 0
    for i in range(1, n):
        y = array[i].y
        if ((y < ymin) or
			(ymin == y and array[i].x < array[min].x)):
            ymin = array[i].y
            min = i

    array[0], array[min] = array[min], array[0]
    
    p0 = array[0]
    array = sorted(array, key=cmp_to_key(compara))
    
    m = 1 
    for i in range(1, n):
        while ((i < n - 1) and
		(orientacion(p0, array[i], array[i + 1]) == 0)):
            i += 1
            
        array[m] = array[i]
        m += 1 
    
    if m < 3:
        return

    S = []
    S.append(array[0])
    S.append(array[1])
    S.append(array[2])

    for i in range(3, m):
        while ((len(S) > 1) and (orientacion(nextToTop(S), S[-1], array[i]) != 2)):
            S.pop()
        S.append(array[i])

    while S:
        p = S[-1]
        print("(" + str(p.x) + ", " + str(p.y) + ")")
        S.pop()
    print("")


# Función de casos de prueba
def testcase(dots):
    array = []
    for i in dots:
        array.append(Dot(i[0],i[1]))
    n = len(array)
    convexo(array, n)


# Ejecución de casos de prueba
tc1 = [(1, 4), (2, 1), (2, 3), (3, 2), (3, 3), (3, 4), (4, 1), (4, 3)]
tc2 = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
tc3 = [(1, 1), (1, 2), (1, 4), (2, 1), (2, 3), (3, 2), (3, 3), (3, 4), (4, 2), (4, 3)]
tc4 = [(1, 3), (2, 1), (2, 3), (2, 4), (3, 2), (3, 3), (4, 1), (4, 4)]

print("Caso de prueba 1")
testcase(tc1)

print("Caso de prueba 2")
testcase(tc2)

print("Caso de prueba 3")
testcase(tc3)

print("Caso de prueba 4")
testcase(tc4)