class Node:
  #Constructor de clase Nodo
  def __init__(self):
    self.children = {}
    self.end = False

class Trie:
  #Constructor de clase Trie
  def __init__(self):
    self.root = Node()

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