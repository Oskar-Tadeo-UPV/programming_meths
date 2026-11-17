"""
    Realizar una funcion que genere el nombre completo
    de una persona, dados su: nombre, segundo nombre y
    apellinos.
"""
def create_fullname(firstname, lastname, middlename=""):
    """
    This function creates the fullname of a person given:
    firstname, middlename, lastname.
    """
    fullname = f"{firstname} {middlename} {lastname}"
    if middlename == "":
        fullname = f"{firstname} {lastname}"
    else:
        fullname = f"{firstname} {middlename} {lastname}"
    return fullname.title()

"""
print("\nPositional Arguments")
# Positional Arguments
fullname1=create_fullname("osKaR", "TAdEo", "AlVaReZ NáJEra")
print(fullname1.title())

print("\nKeyword Arguments")
# Keyword Arguments
fullname2=create_fullname(lastname="MORENO Hernández", firstname="CriSTIan", middlename="eduardo")
print(fullname2.title())

print("\nMixing Arguments")
# Mixing Positional & Keyword
fullname3=create_fullname("Carlos", "Tovar Garcia", middlename="Antonio")
print(fullname3.title())

print("\nOptional Arguments")
# Optional Arguments
fullname4=create_fullname("osKaR", lastname="AlVaReZ NáJEra")
print(fullname4.title())
"""