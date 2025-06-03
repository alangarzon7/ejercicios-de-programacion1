"""6. Ingreso de contraseña 
Situación: El programa debe pedir al usuario que 
ingrese una contraseña. 
Solo se permite acceder si la contraseña ingresada es 
"python123". 
Si es incorrecta, debe pedirla nuevamente hasta que 
sea correcta. 
Al ingresar la correcta, mostrar "Acceso autorizado". """
contraseña=(input("Ingrese su contraseña: ")).lower()
while contraseña!="python123":
    print("Contraseña incorrecta")
    contraseña=(input("Ingrese su contraseña: ")).lower()
    
print("ACCESO AUTORIZADO")
    