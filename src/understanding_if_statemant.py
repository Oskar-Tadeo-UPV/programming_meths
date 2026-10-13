# if Statement
cars = ["audi","bmw","subaru","toyota"]
for car in cars:
    if car == 'audi':
        print(car.upper())
    else:
        print(car)

# El condicional
#   El conedicional es el corazon de un 'if'

# Para determinar igualdad '=='
print("\n---------True condition----------------")
#   Concicional True/Verdadero
truck = "Ford"
print(truck == "Ford")
print("\n---------False condition----------------")
#   Concicional False/Falso
print(truck == "Cheyenne")
print(truck == "ford")
print("\n---------Condition !----------------")
# condicional ! = para determinar desigualdad
print(truck!="Ford") # False
print(truck!="tacoma") # True
print("\n--------------Comparaciones numericas-------------------")
# Comparaciones númericas
age = 18
print(age==18) # True
print(age==25) # False
print(age=="18") # False <Tipado Fuerte

answer = 17
if answer != 42:
    print(f"{answer}. Esa no es la respuesta correcta.")

age = 19
# Simbolo menor que
print(age < 21) # True
print(age <= 21) # True
print(age > 21) #false
print(age < 21)
print(age <= 21)
print(age == 21)