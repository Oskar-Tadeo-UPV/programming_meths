magicians = ['harry', 'ron', 'hermione', 'snape', 'voldermort']
print(magicians)
print("\n--------------- no usando for")
print(magicians[0], magicians[1], magicians[2], magicians[3], magicians[4])

#ciclo for
print("\n--------------- Usando ciclo for")
for magician in magicians:
    print(magician)
    # Esto se conoce como looping

print("\n--------------- Usando ciclo for con end=' '")
for magician in magicians:
    print(magician, end=" ")
print()
print("\n--------------- dandole un mensaje a cada mago")
for magician in magicians:
    print(f"{magician.title()} ese fue un gran hechizo")
    print(f"No puedo esperar el siguiente hechizo, {magician.upper()}\n")
print("Gracias a todos, fue un gran espectaculo")

#Identacion
"""
    Python utiliza la identacion para determinar cuando una linea
    de codigo esta conectada a la linea de codigo anterior.

    Basicamente. se utiliza 4 espacios en blanco para obligarnos a
    escribir ordenado y estructurado
"""

# No olvidemos identar - Traceback Identation Error
magicians = ["alice", "david", 'caroline']
#for magician in magicians:
#print(magician) # Identation Error

#Error de logica / logic error
for magician in magicians:
    print(magician)
print(f"No puedo esperara a ver el siguiente truco, {magician}")

for magician in magicians:
    print(magicians) # Esto imprime la lista las veces de indices que tenga la lista.


#Identacion Inecesaria / Identaton error
#message = 'Hello world'
#    print(message)

#NO olvidar los ":" - Syntax Error
#for magician in magicians
#    print(magician)
