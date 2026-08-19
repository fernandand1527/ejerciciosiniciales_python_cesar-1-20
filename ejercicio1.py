# Reforma tributaria (impuestos según salario)

salario = float(input("Ingrese su salario mensual en millones: "))

if 12 <= salario <= 15:
    print("Debe pagar un impuesto del 3%")
elif 15 < salario <= 20:
    print("Debe pagar un impuesto del 5%")
elif 20 < salario <= 30:
    print("Debe pagar un impuesto del 8%")
elif salario > 30:
    print("Debe pagar un impuesto del 10%")
else:
    print("No paga impuesto")