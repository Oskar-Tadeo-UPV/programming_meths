def greet_to_person(name):
    """
        Esta funcion saluda a una persona.
    """
    print(f"Hola: {name}")

greet_to_person("oskar".title())
greet_to_person("charly".upper())
greet_to_person("mercado".title())
greet_to_person("aaron".title())

name = input ("escribe el nombre del usuario: ")
greet_to_person(name)