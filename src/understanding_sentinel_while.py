"""
    while - sentine - centinela
    while True:
        print("hola")

    Realizar un programa que capture el importe y que
    acumule todos éstos importes en una variable.    
"""

sum = 0.0
message = """
    Sistema gestor de acumulacion de valores.
    La creatividad esta en tus manos.

    En todo momento, si quieres salir del programa
    puede tupear q, e, quit, exit

Ingresar un valor: """

while True:
    value_txt = input(message)
    if value_txt == 'quit' or \
        value_txt == 'exit' or \
        value_txt== 'q' or \
        value_txt== 'e':
        break

    try:
        value = float(value_txt)
        sum += value #Estructura acumuladora
    except ValueError:
        print("Ingresaste un dato no valido")
print(f"Tu valor total acumulado es: {sum}")