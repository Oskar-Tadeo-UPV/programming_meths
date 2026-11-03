guisos = ["salsa verde", 'deshebrada', "nopales"]

if "salsa verde" in guisos:
    print("hay salsa verde")
elif 'deshebrada' in guisos:
    print ("hay deshebrada")
elif "guiso especial" in guisos:
    print ("hay guiso especial")

#lista vacia
guisos_2 = ["salsa verde", 'deshebrada', "nopales", "asado"]

if guisos_2:
    for guiso in guisos_2:
        print(guiso)
else:
    print("No hay guisos")

print("-----------------------------------------------------------------------------------")
guisos_disponible = ["salsa verde", 'deshebrada', "nopales", 'asado', "picadillo"]
guisos_a_ordenar = ["barbacoa", 'deshebrada', "cabrito"]
for guiso in guisos_a_ordenar:

    if guiso in guisos_disponible:
        print(f"Si tenemos del guiso {guiso}")
    else:
        print(f"No tenemos {guiso}, una disculpa")
        print("¿tas pendejo o que mijo?".upper())