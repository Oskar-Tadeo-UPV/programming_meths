# Lista de diccionarios
convenant_elite = {
    "name" : "elite",
    "color" : "blue",
    "points" : "10",
    "sheild" : True
}
convenant_jackal = {
    "name" : "jackal",
    "color" : "gray",
    "points" : "6",
    "sheild" : True
}
convenant_grunts = {
    "name" : "grunts",
    "color" : "orange",
    "points" : "3",
    "sheild" : False
}

#Nesting
convenants = []
convenants.append(convenant_elite)
convenants.append(convenant_jackal)
convenants.append(convenant_grunts)
print(convenants)

#Nesting una lista en dicconario
#Menu

tacos = {
    "tortillas": ["maiz", "harina"],
    "guisos" : ["brisket", 'tripa', "pastor"]
}

print(f"Tu has ordenado unos tacos de {tacos['guisos'][0]}")
print(f"En tortilla de harina {tacos['tortillas'][1]}")

# Diccionario de diccionario