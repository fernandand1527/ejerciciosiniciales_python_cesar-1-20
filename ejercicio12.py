def contar_palabra(texto, palabra):
    # Convertimos todo a minúsculas para que no afecte mayúsculas/minúsculas
    texto = texto.lower()
    palabra = palabra.lower()

    # Dividimos el texto en palabras
    lista_palabras = texto.split()

    # Contamos cuántas veces aparece
    return lista_palabras.count(palabra)


# --- Ejemplo de uso ---
texto = "Python es genial. Aprender Python es divertido porque Python es poderoso."
palabra = "python"

cantidad = contar_palabra(texto, palabra)
print(f"La palabra '{palabra}' aparece {cantidad} veces en el texto.")
