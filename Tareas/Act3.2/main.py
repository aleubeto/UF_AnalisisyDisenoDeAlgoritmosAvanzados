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
 
 
def floydWarshall(graph):
 
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
    printSolution(dist)
 
 
# A utility function to print the solution
def printSolution(dist):
    for i in range(tamano):
        for j in range(tamano):
            if(dist[i][j] == INF):
                print("-1", end=" ")
            else:
                print(dist[i][j], end=' ')
            if j == tamano-1:
                print()
 

tamano = int(input())
a = []
INF = 99999


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

floydWarshall(a)

 
# This code is contributed by Divyanshu Mehta