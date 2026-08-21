from diccionario import Diccionario
from palabra import Palabra

miDiccionario = Diccionario()
miDiccionario.agregarPalabra()
miDiccionario.agragarPalabra()
miDiccionario.agragarPalabra()
input("Presione enter para continuar")
pal = input("Ingrese la palabra en español para consultarla en ingles: ").upper()
miDiccionario.consultarEspanolToIngles(pal)
miDiccionario.listarPalabras()
input("Presione enter para continuar")
miDiccionario.consultarEspañolToIngles(pal)
