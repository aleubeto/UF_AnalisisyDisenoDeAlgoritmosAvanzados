# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

# Clase nodo 
class Node:
      #Constructor de clase Nodo
  def __init__(self):
    self.children = {}
    self.end = False

#Clase árbol
class Trie:
  #Constructor de clase Trie
  def __init__(self):
    self.root = Node()

  #Complejidad lineal O(n)
  def insert(self, word: str) -> None:
    #Empezamos a recorrer desde Root
    cur = self.root
    #Para cada caracter dentro de la palabra...
    for char in word:
      #Si no existe en los nodos hijos, se inserta y se vuelve el nodo actual
      if char not in cur.children:
        cur.children[char] = Node()
      cur = cur.children[char]
    #Al acabar el ciclo, llegamos al último caracter, lo marcamos como end=True
    cur.end = True
  
  #Complejidad lineal O(n)
  def search(self, word: str) -> bool:
    #Empezamos a recorrer desde Root
    cur = self.root
    #Para cada caracter dentro de la palabra...
    for char in word:
      #Si el caracter a buscar no está en los nodos hijos, no es posible encontrar word
      if char not in cur.children:
        return False
      #De lo contrario, avanzamos al siguiente Nodo
      cur = cur.children[char]
    #Al acabar el ciclo, llegamos al último caracter, comprobamos si llegamos a un Nodo final
    return cur.end

def main():
    # Creación del arbol, complejidad O(n)
    n = int(input("Introduzca el número de palabras del árbol TRIE: "))
    trie_n = Trie()
    for i in range(n):
        x = str(input(f"Introduzca el valor {i} del árbol: "))
        trie_n.insert(x)
    
    # Creación de lista de búsqueda, complejidad O(n)
    m = int(input("\nIntroduzca el número de palabras a buscar: "))
    list_m = []
    for i in range(m):
        y = str(input(f"Introduzca la palabra {i} de la lista de búsqueda: "))
        list_m.append(y)
        
    # Búsqueda de las palabras de la list_m en el trie_n
    for i in list_m:
        print(trie_n.search(list_m))
        
    
main()


# Caso de prueba 1
case1 = Trie()
case1.insert("there")
case1.insert("their")
case1.insert("any")
case1.insert("answer")
case1.insert("bye")
case1.insert("toc")
case1_list = ["answer", "ant", "their"]

# Caso de prueba 2
case2 = Trie()
case2.insert("apple")
case2.insert("application")
case2.insert("apple pie")
case2.insert("airplane")
case2_list = ["app", "aircraft", "apple"]

# Caso de prueba 3
case3 = Trie()
case2_list = ["empty", "trie",]

# Caso de prueba 4
case4 = Trie()
case4.insert("alejandro")
case4.insert("juan")
case4.insert("maximiliano")
case4_list = ["ale", "ferrer", "max"]




