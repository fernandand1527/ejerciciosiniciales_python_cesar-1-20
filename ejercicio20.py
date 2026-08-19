class Vuelo:
    def __init__(self, numero, fecha, origen, destino):
        self.numero = numero
        self.fecha = fecha
        self.origen = origen
        self.destino = destino
        self.pasajeros = []

    def agregar_pasajero(self, nombre):
        self.pasajeros.append(nombre)

    def mostrar_info(self):
        print(f"Vuelo {self.numero} - {self.fecha}")
        print(f"Origen: {self.origen} → Destino: {self.destino}")
        print("Pasajeros:")
        for p in self.pasajeros:
            print(f" - {p}")

# Ejemplo
vuelo1 = Vuelo("XYZ123", "18/08/2026", "Bogotá", "Medellín")
vuelo1.agregar_pasajero("Juan Pérez")
vuelo1.agregar_pasajero("Ana Gómez")
vuelo1.mostrar_info()
