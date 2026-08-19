class Carro:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        return f"{self.marca} {self.modelo} ({self.año})"

class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def mostrar_info(self):
        return f"'{self.titulo}' de {self.autor} ({self.año})"

# Objetos
carro1 = Carro("Toyota", "Corolla", 2020)
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)

print(carro1.mostrar_info())
print(libro1.mostrar_info())
