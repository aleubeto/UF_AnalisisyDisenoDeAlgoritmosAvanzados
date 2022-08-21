# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

#Implementación de PD y algoritmos avaros para el cambio de monedas

#Función de cambio con progra dinámica
def dinamic(n,coins,p,q):
    change = change_list(n)
    
    return change

#Función de cambio con algoritmo aváro
def greedy(n,coins,p,q):
    change = q - p
    i = n - 1
    while (i>=0):
        if (change >= coins[i]):
            print(change//coins[i])
            change = change % coins[i]
        else:
            print(0)
        i -= 1
        
        




#Introducción de los valores vía teclado
n = int(input("+ Introduce el número de denominaciones de monedas: "))
coins = []
for i in range(n):
    coins.append(int(input("- Introduzca el valor " + str(i + 1) + " de denomicación de las monedas: ")))
p = int(input("+ Introduce el precio del producto: "))
q = int(input("+ Introduce el billete o moneda(s) de pago: "))

# Ejecución de funciones
dinamic(n,coins,p,q)
greedy(n,coins,p,q)

# Ejecuciones de prueba
dinamic(4,[1,2,5,10], 20, 30)
greedy(4,[1,2,5,10], 20, 35)


