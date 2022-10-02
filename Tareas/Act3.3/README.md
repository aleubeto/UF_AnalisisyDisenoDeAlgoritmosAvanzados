
# Actividad 3.3 Implementación de "Knapsack problem"

### Escribe un programa en C++ que resuelva el problema de la mochila (Knapsack problem)

La entrada al programa es un **número N** que representa el número de elementos posibles disponibles,
seguido de N enteros que representan el valor de cada uno de esos elementos,
seguido de N enteros que representan los pesos asociados a cada elemento.
por último , **un entero W**, que representa el peso máximo o capacidad de la mochila.

La salida del program debe ser la ganancia (o beneficio) óptimo

~~~
ejemplo de entrada:

3
1
2
3
4
5
1
4

ejemplo de salida:

3
~~~

- Tu programa debe ser llamado main.cpp y debe compilar utilizando el comando `g++` en un ambiente linux.
- Tu programa debe poder ejecutarse utilizando entrada redireccionada en un ambiente linux 
(`./a.out < in.txt`)