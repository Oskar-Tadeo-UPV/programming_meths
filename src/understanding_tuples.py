"""
    Tuplas

    Las tuplas son listas de elementos que no cambias de tamaño.
    Las tuplas son listas inmutables

    Se utilizan los parentesis () para definir una tupla.
    
    Ejemplo:
        Si tenemos un rectangulo (largo, ancho) que siempre va a 
        tener cierto tamaño, podemos asegurar que sus no van a 
        cambiar si colocamos sus valores en una tupla
"""
dimensions = (200, 50) # 200 de largo x 50 de ancho
print("tupla original: ", dimensions)

# Vamos a imprimir elementos de una tupla
# Se realiza de la misma forma que con una lista
print(dimensions[0])
print(dimensions[1])
#print(dir(dimensions))

# Lista
dimensions_2 = [200, 50]
#print("metodos y atributos de las listas:", dir(dimensions_2))

# String
name = "Oskar"
#print("metodos y atributos de las listas:", dir(name))

# Numeros
age = 18
#print("metodos y atributos de los numeros: ", dir(age))




# vamos a ver el valor de una lista
names = ["Carlos","Wendy","Marco","Luis"]
print(names)
names[0] = "Mercury"
names[1] = "Mercury"
names[2] = "Mercury"
print(names)

#dimensions[0] = 500 Esta operacion no esta permitida

#Looping throgh a tuple
for dimension in dimensions:
    print(dimension)


# Slicing in tuples
names = ("Carlos","Wendy","Marco","Luis")
print(names[1:3])

dimensions = (500, 1000, 20)
print("tupla re-definida:", dimensions)

# Tipos de datos booleanos
answer = True
print(answer)
#print(dir(answer))