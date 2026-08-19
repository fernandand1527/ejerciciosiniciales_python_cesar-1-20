# Lista de días de la semana
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Guardar temperaturas mínimas y máximas
temperaturas = []
for dia in dias:
    print(f"Ingrese temperaturas para {dia}:")
    t_min = float(input("  Temperatura mínima: "))
    t_max = float(input("  Temperatura máxima: "))
    temperaturas.append({"dia": dia, "min": t_min, "max": t_max})

print("\n--- Resultados ---")

# 1. Temperatura media de cada día
for registro in temperaturas:
    media = (registro["min"] + registro["max"]) / 2
    print(f"{registro['dia']}: media = {media:.1f}°C")

# 2. Día con menor temperatura mínima
menor = min(temperaturas, key=lambda x: x["min"])
print(f"\nEl día con menor temperatura fue {menor['dia']} ({menor['min']}°C)")

# 3. Buscar días cuya temperatura máxima coincide con un valor
buscar = float(input("\nIngrese una temperatura máxima a buscar: "))
coincidencias = [r["dia"] for r in temperaturas if r["max"] == buscar]

if coincidencias:
    print("Días con esa temperatura máxima:", ", ".join(coincidencias))
else:
    print("No existe ningún día con esa temperatura máxima.")
