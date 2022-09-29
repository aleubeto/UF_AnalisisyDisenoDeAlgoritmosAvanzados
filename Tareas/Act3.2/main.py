# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

INF = 99999

class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def printSolution(self, src, dist):
        for node in range(self.V):
            if src == node: continue
            print("node ", src + 1," to node ", node + 1, ": ", dist[node])

    def minDistance(self, dist, sptSet):

        min = 1e7
 
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index

    def dijkstra(self, src):
 
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):

            u = self.minDistance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
 
        self.printSolution(src, dist)
 
 
def floydWarshall(graph, tamano):
 
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(tamano):
 
        # pick all vertices as source one by one
        for i in range(tamano):
 
            # Pick all vertices as destination for the
            # above picked source
            for j in range(tamano):
 
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    printSolution(dist, tamano)
 
 
# A utility function to print the solution
def printSolution(dist, tamano):
    for i in range(tamano):
        for j in range(tamano):
            if(dist[i][j] == INF):
                print("-1", end=" ")
            else:
                print(dist[i][j], end=' ')
            if j == tamano-1:
                print()
 

def main():
    tamano = int(input())
    a = []
    

    for c in range(0, tamano):
        x = input()
        x = x.split(" ")
        for i in range(0, len(x)):
            x[i] = int(x[i])
        a.append(x)
        
    g = Graph(tamano)
    g.graph = a

    for i in range(0, tamano):
        g.dijkstra(i)

    for i in range(0, tamano):
        for j in range(0, tamano):
            if a[i][j] == -1:
                a[i][j] = INF

    floydWarshall(a, tamano)
    
def testcase(n, arco):
    g = Graph(n)
    g.graph = arco
    
    for i in range(0,n):
        g.dijkstra(i)
        
    for i in range(0,n):
        for j in range(0,n):
            if arco[i][j] == -1:
                arco[i][j] = INF
                
    floydWarshall(arco, n)
    
    
print("\nCaso de prueba 1")    
testcase(4, [[0,2,-1,3],[-1,0,1,5],[2,3,0,-1],[3,-1,4,0]])
    
print("\nCaso de prueba 2")
testcase(5, [[0,4,8,-1,-1],[4,0,1,2,-1],[8,-1,0,4,2],[-1,2,4,0,7],[-1,-1,2,7,0]])

print("\nCaso de prueba 3")    
testcase(5, [[0,4,5,-1,-1],[4,0,-1,1,-1],[5,-1,0,3,6],[-1,1,-1,0,2],[-1,-1,6,2,0]])

print("\nCaso de prueba 4")    
testcase(4, [[0,3,4,-1],[-1,0,-1,5],[-1,-1,0,3],[8,-1,-1,0]])
    

