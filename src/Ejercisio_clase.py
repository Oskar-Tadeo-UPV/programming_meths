total = 0.0
counter = 0
minimun = None
maximun = None

while True:
    value_txt = input("ingresar un valor o 'exit', 'quit'").lower().replace(" ", "")
    if value_txt in ['exit', 'quit']:
        break

    try:
        value = float(value_txt)
    except ValueError:
        print("Dato Introducido invalido")
        continue

    total += value
    counter += 1

    if minimun is None or value < minimun:
        minimun = value
    if maximun is None or value > minimun:
        maximun = value
if counter == 0:
    print("sin valores ingresados")
