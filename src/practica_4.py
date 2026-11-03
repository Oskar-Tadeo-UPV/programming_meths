subtotal = input("subtotal (MXN): ")
iva_txt = input("IVA (%): ")
tip_txt = input("Propina (%):")

try:
    subtotal = float(subtotal_txt)
    subtotal = float(iva_txt/100)
    subtotal = float(tip_txt/100)
except:
    print("Entrada no valida. Ej.: 150.0, 16, 10")
    raise SystemExit(1)