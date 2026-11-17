"""
    Realizar un programa en el que el usuario deba ingresar
    su PIN de acceso.
    
    Si el pin es correcto, entonces el mensaje debe decir:
    'ingreso autorizado'
    Si el pin es incorrecto, entonces el mensaje debe decir:
    'pin incorrecto, restantes #'

"""
PIN_CORRECTO = "1234" # Pin autorizado
MAX_INTENTOS = 3 # Intentos maximos
intentos = 0 
acceso = False # Flag

while intentos < MAX_INTENTOS:
    line = input("PIN (4 digitos): ")

    if line == PIN_CORRECTO:
        print("ingreso autorizado".title)
        acceso = True
        break

    intentos += 1 #Contador de numeros de intentos
    restantes = MAX_INTENTOS - intentos

    if restantes > 0:
        print(f"pin incorrecto, intentos restantes {restantes}")
    else:
        print("PIN incorrecto, cuenta bloqueada temporalmente")

if acceso:
    print("Bienvenid@ a la UPV")