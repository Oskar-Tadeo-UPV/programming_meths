"""
    Una lista comprehension combina el for loop
    y la creacion de nuevos elementos en una sola linea
    y automaticamente agrega cada nuevo elemento a la
    lista, es decir, sin usar el mtodo append.
"""

squares = [value**2 for value in range(1,11)]
print(squares)

print("------------------------------------------------------------------")
names = ["renata", "peter", "sebas", "leo", "balam"]

names_upv = [name+"@upv.edu.mx" for name in names]
print(names_upv)