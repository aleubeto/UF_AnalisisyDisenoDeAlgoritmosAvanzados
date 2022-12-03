# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

# Verificamos que la reina n oesté siendo atacada
def attacked(i, j,matrix,N):
    for k in range(0,N):
        if matrix[i][k]==1 or matrix[k][j]==1:
            return True
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if matrix[k][l]==1:
                    return True
    return False

#Función principal de Hill Climbing
def hillclimbing(n,matrix,N):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):

            if (not(attacked(i,j,matrix,N))) and (matrix[i][j]!=1):
                matrix[i][j] = 1
                if hillclimbing(n-1,matrix,N)==True:
                    return True
                matrix[i][j] = 0

    return False

#Función main de ejecución manual
def main():
    N = int(input())
    matrix = [[0]*N for _ in range(N)]
    hillclimbing(N,matrix,N)
    for i in matrix:
        print (i)
        
main()

#Funcion testcases
def testcase(N):
    matrix = [[0]*N for _ in range(N)]
    hillclimbing(N,matrix,N)
    for i in matrix:
        print (i)

print("Caso de prueba n = 4")        
testcase(4)

print("Caso de prueba n = 8")        
testcase(8)

print("Caso de prueba n = 12")        
testcase(12)

print("Caso de prueba n = 0")        
testcase(0)

        
