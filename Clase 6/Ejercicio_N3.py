"""crear una funcion que realice la suma,resta, division y ultiplicacion de dos numeros 
y lo imprima con el nombre de cada operacion
a)si el usuario intruce 1, que sume dos numeros
b)si el usuario intruce 2, que reste dos numeros
c)si el usuario intruce 3, que multiplique dos numeros
d)si el usuario intruce 4, que divida dos numeros"""
def operaciones(opcion,a, b)->int:
    if opcion==1:
       print(f"Suma de {a} y {b} es: {a+b}")
    elif opcion==2:
        print(f"La resta de{a} y {b} es: {a-b}")
    elif opcion==3:
        print(f"La multiplicacion de {a} y {b} es: {a*b}")
    elif opcion==4:
        print(f"La divison entre {a} y {b} es: {a/b}")
    return operaciones


while True:
    op=int(input("Elige una opcion, 1(suma), 2(resta), 3(multiplicacion) o 4(division):"))
    if op>=1 and op<=4:
        break
else:
    print("Error, eliga una opcion correcta: ")
a=int(input("Elige un numero: "))
b=int(input("Elige otro numero: "))
operaciones(op,a,b)