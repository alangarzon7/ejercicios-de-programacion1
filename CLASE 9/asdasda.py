while True:  # Bucle infinito hasta recibir una nota válida
    nota = int(input("Ingrese una nota (0-10): "))

    if 0 <= nota  and nota<= 10:  # Verifica que la nota esté en el rango válido
        if nota <= 5:
            print(f"Tu nota es un {nota}, DESAPROBADO.")
        elif nota <= 8:
            print(f"Tu nota es un {nota}, APROBADO.")
        else:
            print(f"Tu nota es un {nota}, SOBRESALIENTE.")
        break  # Sale del bucle cuando se recibe una entrada válida
    else:
        print("Error. Ingrese una nota válida.")