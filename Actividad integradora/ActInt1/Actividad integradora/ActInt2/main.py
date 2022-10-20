INF = 99999

import sys  
 
 
class Grapho():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def printMST(self, parent):

        answer = self.graph[1][parent[1]]
        for i in range(1, self.V):
            if (answer > self.graph[i][parent[i]]):
                answer = self.graph[i][parent[i]]
        print("Flujo Maximo de información", answer)
 
    def minKey(self, key, mstSet):
 
    
        max = -sys.maxsize - 1
 
        for v in range(self.V):
            if key[v] > max and mstSet[v] == False:
                max = key[v]
                min_index = v
 
        return min_index
 

    def primMST(self):
        key = [-sys.maxsize - 1] * self.V
        parent = [None] * self.V 
        key[0] = 0
        mstSet = [False] * self.V
 
        parent[0] = -1  
 
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
 

            mstSet[u] = True
            
            for v in range(self.V):

                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] < self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
 
        self.printMST(parent)

class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def printSolution(self, src, dist): #O(n) 
        for node in range(self.V):
            if src == node: continue
            if node + 1 < src + 1 : continue
            print("node ", src + 1," to node ", node + 1, ": ", dist[node])

    def minDistance(self, dist, sptSet): #O(n)

        min = 1e7
 
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index

    def dijkstra(self, src): # O(n**2)
 
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
 
 
def floydWarshall(graph, tamano):   # O(n**3)
 
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
def printSolution(dist, tamano): # O(n**2)
    for i in range(tamano):
        for j in range(tamano):
            if(dist[i][j] == INF):
                print("-1", end=" ")
            else:
                print(dist[i][j], end=' ')
            if j == tamano-1:
                print()
 

def main(): # O(n)
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
    
def testcase(n, arco1, arco2):  # O(n)
    g = Graph(n)
    g.graph = arco1

    for i in range(0,n):
        for j in range(0,n):
            if arco1[i][j] == -1:
                arco1[i][j] = INF
                
    floydWarshall(arco1, n)
    
    for i in range(0,n):
        g.dijkstra(i)
    
    m = Grapho(n)
    m.graph = arco2
    m.primMST()
    
    
print("\nCaso de prueba 1")    
testcase(4, [[0,16,45,32],[16,0,18,21],[45,18,0,7],[32,21,7,0]], [[0,48,12,18],[52,0,42,32],[18,46,0,56],[24,36,52,0]])
    