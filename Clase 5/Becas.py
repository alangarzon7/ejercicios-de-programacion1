"""6. Sistema de becas 
Para obtener una beca, un estudiante debe cumplir al menos 
una de estas condiciones: 
● Tener un promedio mayor a 8 
● O bien, tener promedio mayor a 6 y bajos recursos Pedí al 
usuario su promedio y si tiene bajos recursos. Informá si 
accede a la beca o no. """
ingresos=float(input("Cual es su ingreso mensual: "))
promedio= float(input("Ingrese su promedio: "))
if ingresos<200.000:
    print("usted entra en la categoria de bajos recursos")
elif ingresos>200.000:
    print("Usted entra en la categoria de altos recursos")
if promedio>8:
    print("Felicidades!Usted cumple los requisitos para acceder a la beca")
elif promedio>6 and ingresos<200.000:
    print("Felicidades!Usted cumple los requisitos para acceder a la beca")
else:
    print("Usted no cumple los requisitos para acceder a la beca")