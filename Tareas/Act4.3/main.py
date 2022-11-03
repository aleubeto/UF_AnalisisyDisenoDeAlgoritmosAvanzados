# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

class Dot:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y



def main():
    n = int(input())
    point=()
    points = []
    dots=[]
    for i in range(n):
        point = input().split(",")
        points.append(point)
    print(points)
    
    for i in points:
        dots.append(Dot(i[0], i[1]))
    

    

main()
