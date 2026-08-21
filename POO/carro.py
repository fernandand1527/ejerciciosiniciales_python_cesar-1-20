class Carro:
    def __init__(self, placa, marca, modelo, color):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0

    def girarDerecha(self):
        print("Girando a la derecha")

    def girarIzquierda(self):
        print("Girando a la izquierda")

    def arrancar(self):
        print("Arrancando el carro")

    def acelerar(self, vel):
        self.velocidad += vel
        print(f"El carro va a {self.velocidad} km/h")

    def parar(self):
        self.velocidad = 0
        print("El carro se ha detenido")
