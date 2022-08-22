# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

#Implementación de PD y algoritmos avaros para el cambio de monedas

#Función de cambio con progra dinámica
def dinamic(n,coins,p,q):
    coins.sort(reverse=True)
    change = q - p
    array = [0]
    result = []

    #División exacta entre de cada dígito de 0 a Change para asignarle una moneda
    for i in range(change):
        for j in range(n):
            if((i+1)%coins[j]==0):
                array.append(coins[j])
                break

    #Recorrido de atrás hacia adelante de lista
    aux = len(array)-1
    for i in range(len(array),0,-1):
        if(i == aux):
            result.append(array[aux])
            aux -= array[i]

    #Recuento de resultados
    for i in coins:
        print(f'{result.count(i)}')
    
#Función de cambio con algoritmo aváro
def greedy(n,coins,p,q):
    coins.sort()
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
def main():
    n = int(input("+ Introduce el número de denominaciones de monedas: "))
    coins = []
    for i in range(n):
        coins.append(int(input("- Introduzca el valor " + str(i + 1) + " de denomicación de las monedas: ")))
    p = int(input("+ Introduce el precio del producto: "))
    q = int(input("+ Introduce el billete o moneda(s) de pago: "))

    # Ejecución de funciones
    dinamic(n,coins,p,q)
    greedy(n,coins,p,q)

# Ejecuciones de prueba 1
dinamic(4,[1,2,5,10], 20, 35)
greedy(4,[1,2,5,10], 20, 35)

print('')

# Ejecuciones de prueba 2
dinamic(4,[1,2,5,10], 99, 100)
greedy(4,[1,2,5,10], 99, 100)

print('')

# Ejecuciones de prueba 3
dinamic(4,[1,2,5,10], 39, 50)
greedy(4,[1,2,5,10], 39, 50)

print('')

# Ejecuciones de prueba 4   !Resultados diferentes pero correctos :D
dinamic(4,[1,2,5,10], 13, 20)
greedy(4,[1,2,5,10], 13, 20)