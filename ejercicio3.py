 # Precio de entrada según edad
edad = int(input("Ingrese la edad del cliente: "))

if edad < 5:
    print("La entrada es gratis")
elif edad <= 18:
    print("Debe pagar 5000 pesos")
else:
    print("Debe pagar 10000 pesos")
