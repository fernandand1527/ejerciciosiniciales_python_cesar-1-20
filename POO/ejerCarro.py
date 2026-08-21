from carro import Carro

#creando un objeto de la clase Carro
unCarro=Carro("XYZ123","Mazda","2020","Rojo")

print(type(unCarro))

unCarro.girarDerecha()

unCarro.girarIzquierda()

print(f"El carro es de color {unCarro.color.upper()}")
#modificando atributo color
unCarro.color="Verde"

print(f"El carro es de color {unCarro.color.upper()}")

otroCarro=Carro("zzz222","Renault","2021","Azul")
print(f"El carro es de color {otroCarro.color.upper()}")

unCarro.acelerar(20)
unCarro.acelerar(30)
