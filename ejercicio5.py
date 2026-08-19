# Crear lista de palabras
palabras = []
cantidad = int(input("¿Cuántas palabras desea ingresar? "))

for i in range(cantidad):
    palabra = input(f"Ingrese la palabra {i+1}: ")
    palabras.append(palabra)

# Buscar ocurrencias
buscar = input("Ingrese la palabra que desea buscar: ")
conteo = palabras.count(buscar)

print(f"La palabra '{buscar}' aparece {conteo} veces en la lista.")

# Ejemplo de uso de set
thisset = {"apple", "banana", "cherry"}  # aquí sí lo definimos
thisset.add("orange")
print(thisset)

