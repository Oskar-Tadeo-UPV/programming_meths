weigth_txt = input("Peso (kg): ")
heigth_txt = input("Altura (mts): ")

try:
    weigth = float(weigth_txt)
    heigth = float(heigth_txt)
    imc = weigth / (heigth **2)
    print(f"Tu indice de masa corporal es {imc}")
except ValueError:
    print("Datos no invalidos. Ej.: peso 75.9, altura 1.65")
except ZeroDivisionError:
    print("La altura debe ser diferente de 0")
except Exception as err:
    print(err)
print("Procesos posteriores")