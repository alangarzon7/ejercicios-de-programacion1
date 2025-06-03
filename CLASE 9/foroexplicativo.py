while True:  
    nota = int(input("Ingrese una nota (0-10): "))

    if 0 <= nota and nota <= 10:  
        if nota <= 5:
            print(f"Tu nota es un {nota}, DESAPROBADO.")
        elif nota <= 8:
            print(f"Tu nota es un {nota}, APROBADO.")
        else:
            print(f"Tu nota es un {nota}, SOBRESALIENTE.")
        break 
    else:
        print("Error. Ingrese una nota válida.")
        
        