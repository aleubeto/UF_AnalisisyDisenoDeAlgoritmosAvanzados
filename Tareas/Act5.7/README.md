# Actividad 5.7 Implementación Hill-Climbing

### Poner en práctica la implementación del algoritmo de Hill-Climbing

Utilizando la técnica de programación búsqueda avanzada, construye un programa que implemente el algoritmo de **Hill-Climbing** para dar solución al problema de las *N-Queens* el cual consiste en colocar `N` reinas del juego del ajedrez en un tablero de NxN de tal forma que ninguna reina se pueda atacar a las demás.

~~~
// Ejemplo 1
Input:
4

Output:
{ 0,  1,  0,  0}
{ 0,  0,  0,  1}
{ 1,  0,  0,  0}
{ 0,  0,  1,  0}

// Ejemplo 2
Input: N = 8

Output:
{ 0, 0, 0, 0, 0, 0, 1, 0}
{ 0, 1, 0, 0, 0, 0, 0, 0}
{ 0, 0, 0, 0, 0, 1, 0, 0}
{ 0, 0, 1, 0, 0, 0, 0, 0}
{ 1, 0, 0, 0, 0, 0, 0, 0}
{ 0, 0, 0, 1, 0, 0, 0, 0}
{ 0, 0, 0, 0, 0, 0, 0, 1}
{ 0, 0, 0, 0, 1, 0, 0, 0}
~~~