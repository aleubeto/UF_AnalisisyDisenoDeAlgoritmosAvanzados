# Actividad 3.4 Implementación de "Graph coloring"

### Escribe un programa en C++ que proponga una solución al problema de coloración de grafos

La entrada al programa es un **grafo no dirigido**, en forma de **matriz de adyacencias**.
Si no es posible asignar colores diferentes a cada nodo, se despliega el mensaje `"No es posible asignar colores a los nodos"`.

Si es posible asignar colores diferentes a nodos adyacentes, el output es una **lista de colores asignados** a cada nodo.

~~~
ejemplo de entrada:

5
0 0 1 0 1
0 0 1 1 1
1 1 0 1 0
0 1 1 0 1
1 1 0 1 0

Ejemplo de salida:

Node: 0, Assigned Color: 0
Node: 1, Assigned Color: 0
Node: 2, Assigned Color: 1
Node: 3, Assigned Color: 2

~~~

- Tu programa debe ser llamado main.cpp y debe compilar utilizando el comando g++ en un ambiente linux.
- Tu programa debe poder ejecutarse utilizando entrada redireccionada en un ambiente linux 
(./a.out < in.txt)