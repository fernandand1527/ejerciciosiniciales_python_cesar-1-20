import datetime

# Lista para almacenar las cuentas
cuentas = []

def crear_cuenta(nombre, identificacion, correo):
    # Obtener año actual
    año = datetime.datetime.now().year
    consecutivo = len(cuentas) + 1
    codigo = f"{año}-{consecutivo}"
    
    cuenta = {
        "codigo": codigo,
        "fecha": datetime.datetime.now().strftime("%d/%m/%Y"),
        "saldo": 0.0,
        "cliente": {
            "id": identificacion,
            "nombre": nombre,
            "correo": correo
        }
    }
    cuentas.append(cuenta)
    print(f"Cuenta creada: {codigo}")

def consignar(codigo, valor):
    for cuenta in cuentas:
        if cuenta["codigo"] == codigo:
            cuenta["saldo"] += valor
            print(f"Consignados {valor} a la cuenta {codigo}. Nuevo saldo: {cuenta['saldo']}")
            return
    print("Cuenta no encontrada.")

def retirar(codigo, valor):
    for cuenta in cuentas:
        if cuenta["codigo"] == codigo:
            if cuenta["saldo"] >= valor:
                cuenta["saldo"] -= valor
                print(f"Retirados {valor} de la cuenta {codigo}. Nuevo saldo: {cuenta['saldo']}")
            else:
                print("Fondos insuficientes.")
            return
    print("Cuenta no encontrada.")

def mostrar_cuentas():
    for cuenta in cuentas:
        print(f"\nCódigo: {cuenta['codigo']}")
        print(f"Fecha: {cuenta['fecha']}")
        print(f"Saldo: {cuenta['saldo']}")
        print(f"Cliente: {cuenta['cliente']['nombre']} ({cuenta['cliente']['id']}) - {cuenta['cliente']['correo']}")

# --- Ejemplo de uso ---
crear_cuenta("Juan Pérez", "12345", "juan@example.com")
crear_cuenta("Ana Gómez", "67890", "ana@example.com")

consignar("2026-1", 500)
retirar("2026-1", 200)

mostrar_cuentas()
