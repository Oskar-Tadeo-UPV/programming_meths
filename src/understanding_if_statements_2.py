"""
Ejercicio
    Realizar que dertermine el costo de un boleto a partir
    de las sig. condiciones:
    
    -costo para una persona menor o igual a 4 años: gratis 
    -costo para una persona cuya edad es mayor a 4 años pero menor a 18 años: $2OO
    -costo para una persona cuya edad es mayor a 18 años: $500
"""

age = input("Ingresa edad para identificar tu precio:")
print("solo If")
#print(age)
#print(type(age))
age = int(age)
#print(type(age))

if age <= 4:
    cost = 0

if age > 4 and age < 18:
    cost = 200

if age >= 18:
    cost = 500

print(f"El costo del boleto es: {cost}")

# Solucion en un solo bloque (if-elif-else)
print("Bloque If")
if age <= 4:
    cost = 0
elif age > 4 and age < 18:
    cost = 200
elif age >= 18 and age < 65:
    cost = 500
elif age >= 65:
    cost = 0
#else:
#    cost = 0

print(f"El costo del boleto es: {cost}")