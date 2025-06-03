"""Una discoteca permite el ingreso solo a personas mayores de 18 
años. Además, si tienen entre 18 y 21 años, no pueden consumir 
alcohol. Pedí al usuario su edad y determiná si puede ingresar y 
si puede o no consumir alcohol."""
edad=int(input("Ingrese su edad: "))
if edad>=18 and edad<=21:
    print("usted puede ingresar, pero no puede consumir alcohol")
elif edad<18:
    print("usted no puede ingresar a la discoteca")
else:
    print("usted puede ingresar y consumir alcohol")

