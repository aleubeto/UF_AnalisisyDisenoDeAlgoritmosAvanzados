# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

#Implementación de PD y algoritmos avaros para el cambio de monedas

def dinamic(n,coins,p,q):
    
    return 0

def greedy(n,coins,p,q):
    
    return 0



#Introducción de los valores vía teclado
n = int(input("Introduce el número de denominaciones de monedas: "))
coins = []
for i in range(n):
    coins.append(int(input("Introduzca el valor " + str(i + 1) + " de denomicación de las monedas: ")))
p = int(input("Introduce el precio del producto: "))
q = int(input("Introduce el billete o moneda(s) de pago: "))

# Ejecución de funciones
dinamic(n,coins,p,q)
greedy(n,coins,p,q)

# Ejecuciones de prueba
dinamic(4,[1,2,5,10], 20, 30)
greedy(4,[1,2,5,10], 20, 30)


