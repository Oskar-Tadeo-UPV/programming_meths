#listas de numeros
"""
    Las listas tambien pueden tener almacenar numeros.
    python ofrece varias herramientas que ayudan a trabajar
    eficientemente con listas de numeros
"""
#Metodo build-in range()
"""
    El metodo range() nos ayuda a crear facilmente
    series de numeros.

    Ejemplos:
"""

for value in range(1,5):
    print(value)
print("---------------------------------------------------------------")
numbers = list(range(0,10))
print(numbers)
print("---------------------------------------------------------------")
even_numbers = list(range(0,11,2))
print(even_numbers)
print("---------------------------------------------------------------")
noun_numbers = list(range(1,11,2))
print(noun_numbers)
print("\n----------------ejercicio---------------------------------------")
table5 = list(range(5,51,5))
print(table5)
print("\n-----------------Trabajo----------------------------------------")
"""
    crear lista con los primero 10 numeros cuadraticos
"""
squares = []
for value in range (1, 11):
    squares.append(value**2)
print(squares)