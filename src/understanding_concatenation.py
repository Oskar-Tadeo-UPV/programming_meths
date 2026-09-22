# combinacion / Combinacion de Stings

first_name = "oskar"
last_name = "tadeo"

#concatenacion de las variables
full_name = first_name + last_name

#concatenacion anterior pero usando un espacion representado como (" ")
full_name = first_name + " " + last_name
print(full_name)

#Se pueden usar metodos con las concatenaciones
print(full_name.title())

print("hola".upper(), first_name + " " + last_name)

#whitespace
"""
Whitespace se refiere a cualquier caracter que no se imprime, es decir, un espacion ( ),
tabuladores (\t) y finales de linea (\n)

Se utilizan comunmente para organizar las salidas de texto a usuario de tal manera que sea
más amigable que sea más amigable de leer o ver para los usuarios
"""

print("python")
print("\tpython")
print("\t\tpython")
print("Lenguajes:\n\tpython\nC\nJavaScripts")

#Cocatencaion usando f-Strings

famous_person = "oskar tadeo"
message = "{famous_person} una vez dijo: Python is love"
print(message)
message = f"{famous_person.upper()} una vez dijo: Python is love"
print(message)