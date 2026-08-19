print("Bienvenido a la Pizzería Napolitana 🍕")
tipo = input("¿Quiere una pizza vegetariana? (si/no): ").lower()

ingredientes_base = ["mozzarella", "tomate"]

if tipo == "si":
    print("Ingredientes vegetarianos: 1) Pimiento  2) Tofu")
    opcion = int(input("Elija un ingrediente (1-2): "))
    ingrediente = "Pimiento" if opcion == 1 else "Tofu"
    pizza = ingredientes_base + [ingrediente]
    print("Su pizza vegetariana lleva:", ", ".join(pizza))
else:
    print("Ingredientes no vegetarianos: 1) Peperoni  2) Jamón  3) Salmón")
    opcion = int(input("Elija un ingrediente (1-3): "))
    if opcion == 1:
        ingrediente = "Peperoni"
    elif opcion == 2:
        ingrediente = "Jamón"
    else:
        ingrediente = "Salmón"
    pizza = ingredientes_base + [ingrediente]
    print("Su pizza no vegetariana lleva:", ", ".join(pizza))

