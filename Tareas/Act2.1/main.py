#long hash(string s) {
#    const int p = 3;
#    const int m = 1000000009;
#    long hash = 0;
#    long pow = 1;
#    for (for every character c in s) {
#        hash = (hash + (c - 'a' + 1) * pow) % M;
#        pow = (pow * p) % M;
#    }
#    return hash;
#}
#https://iq.opengenus.org/string-hashing/

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
                charlist.append(char)

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

    for i in range(len(array)):
        print(len(array[i]),array[i])
    
    #3:Creación de lista con sumas verticales

    #4:Conversión de elementos a hexadecimal

#Programa principal
def main():
    n = int(input())
    inputFile = input('Act2.1/scripts/')
    inputFile = f'scripts/{inputFile}'
    hashing(n, inputFile)

#Pruebas de ejecución
hashing(16,'scripts/test1.txt')
#main()
#print(hash("opengenus"))