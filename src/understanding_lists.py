#Listas
"""
Las listas nos permiten almacenar informacion en un lugar
la cantidad que se desee: ya sean pocos elementos o millones
de elementos.

Una lista es una colección de items (elementos que tiene un orden particular.)
Se puede crear listas que incluyan strings, enteros, floats, los nombres de las
personas de tu familia, etc., podemos almacenar (los tipos de datos permitidos en Python)
lo que queramos en una lista.

Son elementos Mutables: pueden modificarse el tamaño de la lista.

Se recomienda nombrar una variable del tipo lista en plurar.

En Python, los corchetes [] indican una lista, sus elementos se separan por comas.

Ejemplo:
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized', "apache"]
print(bicycles)

#¿Cómo puedo acceder a los elementos de una lista

"""
Las listas son colecciones ordenadas. Se puede acceder a un ejemplo
de una lista diciendo a Python la posicion o índice del elementos deseado.

Para obtener el valor deseado, se debe escribir el nombre de la lista, seguido del índice
del elementos entre corchetes.
"""
print(bicycles[0], bicycles[1], bicycles[2])
print(bicycles[0].upper())

#los indices comienza en 0, no en 1
#bicycles = ['trek', 'cannondale', 'redline', 'specialized', "apache"]
print(bicycles[1]) # cannondale
print(bicycles[3]) # specialized

#accediendo al último elemento de la dista 
print(bicycles[-1]) # apache
print(bicycles[-2]) # specialized

#Utilizando valos individuales de una lista
message = f"My first bycicle was a {bicycles[-1].upper()}"
print(message)