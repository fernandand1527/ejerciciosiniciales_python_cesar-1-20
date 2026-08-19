def separar_pares_impares(lista):
    pares = sorted([n for n in lista if n % 2 == 0])
    impares = sorted([n for n in lista if n % 2 != 0])
    return pares, impares

# Ejemplo
nums = [5, 2, 8, 7, 3, 10, 1]
pares, impares = separar_pares_impares(nums)
print("Pares:", pares)
print("Impares:", impares)
