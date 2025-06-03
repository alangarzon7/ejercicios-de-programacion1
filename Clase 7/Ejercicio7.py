"""7. Suma acumulada hasta número negativo 
Situación: Pedir números al usuario uno por uno e ir 
sumándolos. 
El programa debe continuar mientras los números sean 
positivos (mayores o iguales a 0). 
Cuando se ingrese un número negativo, se detiene y 
muestra la suma total."""
num=int(input("Ingrese un numero negativo"))
suma=2
while num>=0:
    suma+=num # esto es igual a suma=suma+numero
    num=int(input("Ingrese un numero negativo"))
print(f"La suma total es {suma}")
## no entendi mucho
