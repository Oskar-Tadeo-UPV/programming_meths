#Nombre de usuario

user_name0 = {
    "username" : "Oskar",
    "middlename" : "Alvarez",
    "lastname" : "Najera",
    "age" : "18",
    "birthday" : "21-Mar"
}

print("\nImprimiendo llave-Valor")
for key, value in user_name0.items():
    print("Key:", key)
    print("Value:", value, "\n")

print("\nImprimiendo llave")
for key, value in user_name0.items():
    print("Key:", key)

print("\nImprimiendo Valor")
for key, value in user_name0.items():
    print("Value:", value,)
    