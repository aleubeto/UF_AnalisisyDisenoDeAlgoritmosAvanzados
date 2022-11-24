# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

# Función que recibe un conjunto de n elementos
def lines(n):
    elements = input('set = ').split(',')
    for i in range(len(elements)):
        elements[i] = int(elements[i])
    return set(elements[:n]) #Retornamos los primeros n elementos

# Función que implementa algoritmo "meet in the middle"
def meet_in_middle(set,s):
    return set  # A TRABAJAR!!!

# Función que ejecuta programa principal
def main():
    n = int(input('n = '))
    set = lines(n)
    s = int(input('s = '))
    print(meet_in_middle(set,s))

# Función que ejecuta casos de prueba
def tc(set,s):
    print(meet_in_middle(set,s))

# Ejecución de programa principal
# main()

# Ejecución de casos de prueba
tc({45, 34, 4, 12, 5, 2},42)   #tc1
tc({3, 34, 4, 12, 5, 2},10)   #tc1