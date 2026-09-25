#Numeros
# Enteros - Integers
"""
Los numeros enteros los podemos sumar(+), restar (-),
multiplicar (*) y/o dividir (/).
"""
#Operaciones con enteros
print("\nOperaciones con enteros")
print(2+3)
print(3-2)
print(2*3)
print(3/2)

#Usando con variables de tipo enteras
print("\nOperaciones variables tipo enteras")
number_1 = 5
number_2 = 10
print(number_1+number_2)

#Operaciones con decimales
print("\nOperaciones con decimales")
print(2.1 + 1.5)
print(3.5 - 0.9)
print(2 * 5.1)
print(1.5 / 2)

# Enteros
# Sumar +
# Restar -
# Multiplicar *
# Dividir /
# Dividir enteros //n
# Potencias **n
print("\nExponentes")
print(3 **2) # 3^2
print(3 **3) # 3^3
print(10 **6) # 10^6
print(10 %2) # Modulo (mod)

print("\nDecimales o numeros de flotantes")
print(0.1 + 0.1)
print(0.2 - 0.2)
print(2 * 0.1)
print(2 * 0.2)

# Imprimir la edad de alguien
age = 34 # Variable del tipo init
# message = "Charly tiene " + age + " años" (TYPEERROR)
print("\nusando 'str()'")
message = "Charly tiene " + str(age) + " años"
print(message)

# Type Error

"""
    Type Error: Python no reconoce el tipo de informacion que se está utilizando
"""
print("\nusando 'f string'")
message_f = f"Charly tiene {age} años"
print(message_f)

# Metodo build-in type()

print(type(age), type("hola"), type(0.25), type(True))
