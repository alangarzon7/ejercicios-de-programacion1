"""3. Mayor de tres números 
Situación: Ingresar tres números y mostrar cuál es el 
mayor de los tres. 
"""
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))
if num1>num2 and num1>num3:
    print(f"{num1} es el mayor de los 3 numeros")
elif num2>num1 and num2>num3:
    print(f"{num2} es el mayor de los 3 numeros")
else:
    print(f"{num3} es el mayor de los 3 numeros")