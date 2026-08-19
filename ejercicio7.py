for i in range(5):
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    if edad >= 80:
        fase = "Fase 1"
    elif edad >= 70:
        fase = "Fase 2"
    elif edad >= 60:
        fase = "Fase 3"
    elif edad >= 30:
        fase = "Fase 4"
    elif edad >= 18:
        fase = "Fase 5"
    else:
        fase = "En espera de autorización"
    print(f"Edad: {edad} → {fase}")

                

                