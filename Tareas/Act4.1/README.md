# Actividad 4.1 Implementación Intersección y proximidad aplicando geometría computacional

### Poner en práctica la implementación de algoritmos de geometría computacional relativos a intersección y proximidad

En equipos de tres personas y utilizando la técnica de **programación de geometría computacional**, construye un programa que implemente el algoritmo para determinar si dos segmentos de rectas intersectan.

El programa recibe un conjunto de `n` *(donde `n` es un número múltiplo de 4)* puntos ubicados en un plano cartesiano, con el formato:

~~~
x1,y1,x2,y2,x3,y3,x4,y4

x5,y5,x6,y6,x7,y7,x8,y8

.

.

xn-3,yn-3,xn-2,yn-2,xn-1,yn-1,xn,yn
~~~

La salida del programa será un **arreglo de booleanos** indicado con `True` si el par de segmentos de recta (4 puntos por renglón) intersectan, `False` en caso contrario.

El arreglo se deberá de mostrar en la salida estándar.