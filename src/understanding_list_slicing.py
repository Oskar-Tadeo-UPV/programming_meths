players = ["peter", "mercado", "aaron", "fatima", "renata"]
print("Lista original: ", players)

#Slicing
print("Lista Separada: ", players[3:5]) #("fatima", "renata")

"""
El slicing me permite trabajar con un grupo especifico de una lista:
al resultado se le conoce como "un slice".
"""
print("\n///////////////////////////////////////////////////////////////")
print("1:4 ", players[1:4])
print(":3 ", players[:3])
print("2: ", players[2:])
print("-3: ", players[-3:])

print("\n///////////////////////////////////////////////////////////////")
#casos especiales del slicing
print(players)
print("\n------------------------------------------------------")
print(players[1:10])
print("\n------------------------------------------------------")
print(players[-10:10])
print("\n------------------------------------------------------")
print(players[6:1])
print("\n------------------------------------------------------")
print(players[:0])

print("\n///////////////////////////////////////////////////////////////")
#looping through a slice
print("looping through a slice")
students = ["peter", "mercado", "aaron", "fatima", "renata"]

#slicong [::] Tarea
for student in students[3:5]:
    print(f"El estudiambre {student}, va a pasar la materia")
print(students)

#¿Como podemos copiar una lista?
my_food = ["pizza","tacos","flautas"]
my_friend_food = my_food #manera erronea de copiar listas

# Maneras correctas de copiar listas
#1-° -utilizando slicing
my_friend_food_2 = my_food[:]
print(my_friend_food_2)
#2-° -utilizando metodo de las listas .copy()
my_friend_food_3 = my_food.copy()
print(my_friend_food_3)
#3-° -utilizando metodo build in list()
my_friend_food_4 = list(my_food)
print(my_friend_food_4)