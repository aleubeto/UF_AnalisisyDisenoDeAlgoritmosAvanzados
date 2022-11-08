# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

class Dot:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

#Función de distancia entre dos puntos
def distancia(p1, p2):
    	return (float((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y)))


def bg(n, dots):
    d_min1 = 0
    d_min2 = float('inf')
    for i in range(n):  #for j = i+1, j<n
        for y in range(i+1,n):   
            d_min1 = distancia(dots[i], dots[y])
            d_min2 =  min(d_min1, d_min2)
    
    print(d_min2)
            
    #print(f"La distancia más corta es: {d_min2}")
    
    
def main():
    n = int(input())
    point=()
    points = []
    dots=[]
    for i in range(n):
        point = (input().split(","))
        point[0]=int(point[0])
        point[1]=int(point[1])
        point=list(point)
        points.append(point)
    print(points)
    
    for i in points:
        dots.append(Dot(i[0], i[1]))
        
    print(dots)
    

    
def testcase(n, dots):
    array = []
    for i in dots:
        array.append(Dot(i[0],i[1]))
    #print(array)
    return(bg(n, array))
#main()

tc1 = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
#testcase(len(tc1), tc1)

tc2 = [(1, 1), (22, 1), (4, 1), (1, 1), (2, 1)]
testcase(len(tc2), tc2)