# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

# Función que genera matriz para realizar programación dinámica
def dinamic_chart(matrix):
    dinamicChart = []
    for i in range(len(matrix)):
        temp = []
        for j in range(100):
            if j+1 in matrix[i]:
                temp.append(1)
            else:
                temp.append(0)
        dinamicChart.append(temp)
    return dinamicChart

# Función que realiza algortmo de Backtracking con Bitmask
def backtracking_bitmask(matrix,pivote,i,j,temp,result):
    return 0


'''def backtracking_bitmask(matrix,i,j,result):
    # Caso base
    if i==len(matrix):
        return result
    else:
        result.append(matrix[i][:j+1])
        if j==len(matrix[i])-1:
            i+=1
            j=0
        else:
            j+=1
        return backtracking_bitmask(matrix,i,j,result)'''

# Función de programa principal
def main():
    n = int(input())
    restriction = 1<=n and n<=10
    people = []
    if restriction:

        # Inputs del usuario
        for i in range(n):
            colection = input().split()
            for j in range(len(colection)):
                colection[j] = int(colection[j])
            people.append(colection)

        # Backtracking con Bitmask
        return(backtracking_bitmask(people))

    else:
        print('> El número ingresado no cumple con la restricción 1<=n<=10')
    print(people)

# Función de casos de prueba
def tescase(tc):
    #dc = dinamic_chart(tc)
    #print(backtracking_bitmask(tc,0,0,[]))
    print(backtracking_bitmask(tc,0,0,[],[]))

# Ejecución de función de programa principal
#main()

# Ejecución de casos de prueba
tc1 = [[5,100,1],[2],[5,100]]
tescase(tc1)