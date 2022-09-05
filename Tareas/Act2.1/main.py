# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

#https://iq.opengenus.org/string-hashing/

from operator import and_


def hash(s) :
    p = 3
    m = 1000000009
    haash = 0
    pod = 1
    for c in s:
        haash = (haash + (ord(c) - ord("a") + 1) * pod) % m
        pod = (pod * p) % m
    return haash

#Función de Hashing

def hashing(n, inputFile):
    #1:Procesamiento de contenido de archivo (incluye espacios y saltos de línea)
    charlist = []
    with open(inputFile) as file:
        for line in file:
            for char in list(line):
                charlist.append(ord(char))

    #2:Creación de tabla de n columnas
    array = []
    while True:
        if len(charlist) == 0:
            break
        elif len(charlist) < n:
            for i in range(n - len(charlist)):
                charlist.append(n)
        array.append(charlist[:n])
        del charlist[:n]

    
    #3:Creación de lista con sumas verticales
    col_sum = [hex(sum(i)%256) for i in zip(*array)]
  

    #4:Conversión de elementos a hexadecimal
    hash_message = ""
    for i in range(len(col_sum)):
        hash_message += col_sum[i][2:]
    print(hash_message.upper())

#Programa principal
def main():
    n = int(input("Introduzca el valor de n: "))
    if (n%4 == 0) & (16 <= n <= 64):
        inputFile = input('Act2.1/scripts/')
        #Introducir el nombre del archivo dentro de la carpeta scripts
        inputFile = f'scripts/{inputFile}'
        hashing(n, inputFile)
    else:
        print("Introduzca un valor n entero múltiplo de 4 y (16 <= n <= 64)")

#Pruebas de ejecución
#hashing(16,'scripts/test1.txt')
main()
#print(hash("opengenus"))