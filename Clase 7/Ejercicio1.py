"""1. Clasificación de nota 
Situación: Ingresar una nota del 0 al 10 y mostrar si 
el estudiante está: 
● Desaprobado (0 a 5) 
● Aprobado (6 a 8) 
● Sobresaliente (9 o 10) """
nota=int(input("Ingrese una nota: "))
while nota>=0 and nota<=10:
    if nota<=5 and nota>=0:
        print(f"Tu nota es un {nota}, DESAPROBADO.")
    elif nota>=6 and nota<=8:
        print(f"Tu nota es un {nota},APROBADO")
    else:
        print(F"Tu nota es un {nota}, SOBRESALIENTE")
    break
else:
    print("Error. Ingrese una nota valida.")
    