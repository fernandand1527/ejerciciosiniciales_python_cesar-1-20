from datetime import datetime
import os

cuentas = []   # Lista para almacenar las cuentas
clientes = []  # Lista para almacenar los clientes

# -------------------------------
# Función para crear cliente
# -------------------------------
def crearCliente():
    os.system("cls")
    identificacion = input("Ingrese la identificación del cliente: ")
    
    # Verificar si el cliente ya existe
    for cliente in clientes:
        if cliente["identificacion"] == identificacion:
            print("El cliente ya existe.")
            return identificacion
    
    # Si no existe, lo crea
    nombre = input("Ingrese el nombre del cliente: ")
    correo = input("Ingrese el correo del cliente: ")
    cliente = {
        "identificacion": identificacion,
        "nombre": nombre,
        "correo": correo
    }
    
    clientes.append(cliente)  # Agregando cliente a la lista
    return identificacion

# -------------------------------
# Función para crear cuenta
# -------------------------------
def CrearCuenta():
    fechaHoy = datetime.now()
    yearNow = fechaHoy.year
    consecutivo = len(cuentas) + 1
    codigoCuenta = f"{yearNow}{consecutivo:04d}"  # Formato Año + consecutivo
    
    # Crear cliente si no existe
    idCliente = crearCliente()
    
    # Crear cuenta con saldo inicial 0
    cuenta = {
        "codigo": codigoCuenta,
        "cliente": idCliente,
        "saldo": 0
    }
    cuentas.append(cuenta)
    print(f"Cuenta creada exitosamente con código: {codigoCuenta}")

# -------------------------------
# Otras funciones
# -------------------------------
def Consignar():
    os.system("cls")
    print("CONSIGNAR")
    CodigoCuentaConsignar = input("Ingrese el código de la cuenta a Consignar: ")
    for cuenta in cuentas:
        if cuenta['codigoCuenta'] == CodigoCuentaConsignar:
            ValorAConsignar = float(input("Ingrese el monto a consignar: "))
            cuenta['saldo'] += ValorAConsignar
            print(f"Consignación exitosa")
            
        else:
            print("No existe la cuenta con el código ingresado.")
            return

def Retirar():
    pass

def ConsultarCuentaPorCodigo():
    pass

def ConsultarCuentaPorIdentificacionCliente():
    pass

def ListarCuentas():
    os.system("cls")
    print("\t\tLISTADO DE CUENTAS")
    for cuenta in cuentas:
        print(f"Código: {cuenta['codigo']}, Cliente: {cuenta['cliente']}, Saldo: {cuenta['saldo']}")

# -------------------------------
# Menú principal
# -------------------------------
def menu():
    while True:
        os.system("cls")  # Limpia la pantalla en Windows
        
        print("\t\tMENU BANCO ADSO 3229426")
        print("\t1. Crear cuenta")
        print("\t2. Consignar")
        print("\t3. Retirar")
        print("\t4. Consultar cuenta por código")
        print("\t5. Consultar cuenta por identificación del cliente")        
        print("\t6. Listar cuentas")            
        print("\t7. Salir")
        
        opcion = int(input("Ingrese opción (1-7): "))
        
        match opcion:
            case 1: CrearCuenta()
            case 2: Consignar()
            case 3: Retirar()
            case 4: ConsultarCuentaPorCodigo()
            case 5: ConsultarCuentaPorIdentificacionCliente()    
            case 6: ListarCuentas()
            case 7: 
                print("Va a salir del sistema")
                break
            case _: 
                print("Opción no válida")
        
        

# -------------------------------
# Ejecutar menú
# -------------------------------
menu()
