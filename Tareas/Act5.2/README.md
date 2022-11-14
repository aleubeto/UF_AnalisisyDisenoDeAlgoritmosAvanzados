# Actividad 5.2 Implementacion backtracking con Bitmask

### Poner en práctica la implementación del algoritmo de backtracking con Bitmask

En equipos de dos personas y utilizando la técnica de programación de **backtracking**, construye un programa que implemente el algoritmo de backtracking **con bitmasking** para determinar el número de combinaciones que se puede lograr en el problema: Tipos de gorras en un conjunto de personas.

Considere el siguiente problema:

> Existen 100 diferentes tipos de gorras y cada una tiene un ID de 1 a 100. Ademas, hay `n` personas cada una tiene una colección variable de gorras. Cierta fecha todas esas personas deciden ir a una fiesta usando una gorra, pero para verse de manera única han decidido que ninguno de ellos usará el mismo tipo de gorra.
> 
> Se les ha encomendado encontrar el numero total de arreglos o forma diferentes que ninguno de ellos lleve el mismo tipo de gorra. Tomando en cuenta la restricción que `1 <= n <= 10`.
> 
> La primer linea contiene el valor de `n`, después `n` líneas contiene las colecciones de gorras de cada persona.

~~~
EJEMPLO DE EJECUCIÓN:

Input: 
3
5 100 1     // Colección de la primer persona.
2           // Colección de la segunda persona.
5 100       // Colección de la tercer persona.

Output:
4
(5, 2, 100)
(100, 2, 5)
(1, 2, 5)
(1, 2, 100)
~~~
