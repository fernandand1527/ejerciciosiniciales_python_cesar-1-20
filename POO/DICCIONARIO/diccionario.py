from palabra import Palabra

class Diccionario():
    def __init__(self):
        self.listaPalabras = []
    
    def agregarPalabra(self):
        espanol = input("Ingrese Palabra en ESPAÑOL: ").upper()
        ingles  = input("Ingrese Palabra en INGLES: ").upper()
        
        #Crear el objeto Palabra
        unaPalabra = Palabra(espanol,ingles)
        self.listaPalabras.append(unaPalabra)
        input("Se ha agregado la palabra dl Diccionario ✅ Presione ENTER para continuar...")
        
        
    def listarPalabras(self):
        for palabra in self.listaPalabras:
            print("=="*20)
            print("Las palabras del diccionario son:")
            print(f"{palabra.espanol} => {palabra.ingles}")
    
    
    def consultarEspanolToIngles(self, espanol):
        """_summary_
            Funcion que consulta una palabra en español
            en ingles

        Args:
            espanol (string): Palabra en español
        """
        
        #Buscar la palabra en la lista
        for palabra in self,self.listaPalabras:
            if palabra.espanol == espanol:
                print(f"La palabra '{espanol}' en ingles es: {palabra.ingles}")
                break
            
            else:
                print(f"La palabra '{espanol}', no existe en nuestro diccionario :(")
                input("Presione ENTER para continuar...")