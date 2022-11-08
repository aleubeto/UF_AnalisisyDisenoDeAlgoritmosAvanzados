# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

import math

# Declaración de clase Dot
class Dot:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

#Función de distancia entre dos puntos, O(1)
def distancia(p1, p2):
    	return round(math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2),5)

# Función que retorna el camino más corto, O(n**2)
def bg(n, dots):
    d_min1 = 0
    d_min2 = float('inf')
    for i in range(n):  #for j = i+1, j<n
        for y in range(i+1,n):   
            d_min1 = distancia(dots[i], dots[y])
            d_min2 =  min(d_min1, d_min2)            
    return f"La distancia más corta es: {d_min2}"
    
# Función que ejecuta el programa principal, O(n)
def main():
    n = int(input())
    dots=[]
    for i in range(n):
        point = (input().split(","))
        point[0]=int(point[0])
        point[1]=int(point[1])
        dots.append(Dot(point[0],point[1]))        
    print(bg(n, dots))
    
# Función que ejecuta casos de prueba, O(n)    
def testcase(n, dots):
    array = []
    for i in dots:
        array.append(Dot(i[0],i[1]))
    print(bg(n, array))

# Ejecución de programa principal
main()

# Ejecución de casos de prueba
tc1 = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
#testcase(len(tc1), tc1)
tc2 = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
#testcase(len(tc2), tc2)
tc3 = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
#testcase(len(tc3), tc3)
tc4 = [(1, 1), (22, 1), (4, 1), (1, 1), (2, 1)]
#testcase(len(tc4), tc4)