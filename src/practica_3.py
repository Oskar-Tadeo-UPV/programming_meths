
name = input("¿como te llamas? ")
age_txt = input("¿Cuál es tu edad? ")

print(f"Hola {name}, tienes {age_txt} años")
try:
    age = int(age_txt) #convierte string a int
    print("En corea tendrias:", age+1)
except:
    print("solo aceptamos edades enteras")
    print("Por favor, no ingreses caracteres alfabéticos o simbolos")

print("Procesos posteriores")

"""
    name = input("¿como te llamas? ")
    age_txt = input("¿Cuál es tu edad? ")


    try:
        age = int(age_txt) #convierte string a int
    
    except:
       print("solo aceptamos edades enteras")
        print("Por favor, no ingreses caracteres alfabéticos o simbolos")
        raise SystemExit(1)


    print(f"Hola {name}, tienes {age_txt} años")
    print("En corea tendrias:", age+1)
    print("Procesos posteriores")
"""