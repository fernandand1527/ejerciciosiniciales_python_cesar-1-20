import random

# Crear lista con 10 números aleatorios
numeros = [random.randint(1, 100) for _ in range(10)]
print("Lista original:", numeros)

# Ordenar de menor a mayor
numeros.sort()
print("Lista ordenada:", numeros)
