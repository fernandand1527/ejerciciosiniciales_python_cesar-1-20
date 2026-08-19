def es_triangulo(a, b, c):
    # Condición: la suma de dos lados > el tercero
    return a + b > c and a + c > b and b + c > a

def es_rectangulo(a, b, c):
    # Ordenamos los lados para identificar la hipotenusa
    lados = sorted([a, b, c])
    return lados[0]**2 + lados[1]**2 == lados[2]**2

# --- Ejemplo de uso ---
print("¿Es triángulo?", es_triangulo(3, 4, 5))       # True
print("¿Es rectángulo?", es_rectangulo(3, 4, 5))     # True
print("¿Es triángulo?", es_triangulo(1, 2, 3))       # False
     # False

