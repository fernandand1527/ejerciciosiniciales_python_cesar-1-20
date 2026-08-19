class Animal:
    def __init__(self, peso):
        self.peso = peso

    def respirar(self):
        print("Respirando...")

class Pez(Animal):
    def nadar(self):
        print("El pez nada en el agua.")

class Perro(Animal):
    def ladrar(self):
        print("El perro ladra: ¡Guau!")

class Gato(Animal):
    def maullar(self):
        print("El gato maulla: ¡Miau!")

# Objetos
pez = Pez(1.2)
perro = Perro(15)
gato = Gato(5)

pez.nadar(); pez.respirar()
perro.ladrar(); perro.respirar()
gato.maullar(); gato.respirar()
