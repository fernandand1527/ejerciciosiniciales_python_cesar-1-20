def sumaLista(listaNumeros)->int:
    suma = 0 
    
    for numero in listaNumeros:
        suma += numero
    return suma

numeros = [3,6,9,21,1000,33] 
sumaNumeros = sumaLista(numeros)
print(f"Lista de numeros: {numeros}")
print(f"La suma de los numeros de la lista es: {sumaNumeros}")



  