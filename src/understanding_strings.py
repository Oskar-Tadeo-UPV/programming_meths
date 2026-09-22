#STRINGS

"""
Un string es de manera sencilla una serie de caracteres.
En python, todo lo que se encuentre entre comillas simples ''
o dentro de comillas dobles "" es considerado un string

Ejemplo:
    "Esto es un string"
    'Esto tambien es un string'

    'Le dije a un amigo "Python es mi lenguaje favorito"'
    "El lenguaje 'Python' lleva el nombre por Monty Python, no por la serpiente"


Ejemplo Incorrecto:

   (x) " Texto '
   (x) ' Aqui texto"

"""

name = 'oskar tadeo alvarez nájera'
print(name)
print(name.title())
print(name)

name = name.title()
print(name)

#METODOS
"""
    Un metodo es una accion que python puede realizar
    sobre una variable

    El punto . despues de una variable seguido por el nombre del metodo
    es este caso title() dice que tiene que ejecutar el metodo
    de la variable name

    todos los metodos van seguidos de parentesis,
    porque en ocaciones necesitan informacion adicional para funcionar.
    En esta ocacion, el metodo .title() no requiere informacion adicional para ejecutarse.
"""

#OtroS METODOS
print("---------------------")
print(name)
print(name.upper())
print(name.lower())