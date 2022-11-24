Utilizando la técnica de programación de **backtracking**, construye un programa que implemente el algoritmo encontrarse en el medio **(meet in the middle)**.

En el problema *Meet in the middle*, dado un conjunto de `n` enteros donde `n<=40`, donde cada uno de ellos es a lo mas `10**12`, determina el subconjunto con la suma máxima cuya suma es menor o igual que `S`, donde `S<=10**18`.

~~~
EJEMPLO DE EJECUCIÓN

Input: set[] = {45, 34, 4, 12, 5, 2} y S = 42

Output: 41
// La suma máxima del subconjunto es 41, el cual se obtiene de la suma de 34, 5 y 2.

Input: set[] = {3, 34, 4, 12, 5, 2} y S = 10

Output: 10
// La suma máxima del subconjunto es 10, el cual se obtiene de la suma de 2, 3 y 5.
~~~