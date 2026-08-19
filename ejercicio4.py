def decimalBinario(numero):
    respuesta = ""
    resultado = numero
    while True:
        valorInicial = resultado
        residuo = valorInicial % 2
        respuesta += str(residuo)
        resultado = valorInicial // 2

        if resultado == 1:
            respuesta += str(resultado)
            break
        else:
            valorInicial = resultado

    # Invertimos la cadena al final
    respuesta = "".join(reversed(respuesta))
    return respuesta


# Programa principal
numeroEntrada = int(input("Ingrese un número Entero para convertir a Binario: "))
binario = decimalBinario(numeroEntrada)
print(f"El número {numeroEntrada} en binario es: {binario}")


    
  
        



