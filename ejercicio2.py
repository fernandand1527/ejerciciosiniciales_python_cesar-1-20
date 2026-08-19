# Grupos A y B (nombre y sexo)
nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M/F): ")

primera_letra = nombre[0]

if (sexo == "F" or sexo == "f") and primera_letra < "M":
    print("Pertenece al grupo A")
elif (sexo == "M" or sexo == "m") and primera_letra > "N":
    print("Pertenece al grupo A")
else:
    print("Pertenece al grupo B")





