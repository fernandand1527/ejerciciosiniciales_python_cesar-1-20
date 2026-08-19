import calendar

def dias_del_mes(año, mes):
    return calendar.monthrange(año, mes)[1]

# Ejemplo
print(dias_del_mes(2026, 2))  # Febrero 2026 → 28
