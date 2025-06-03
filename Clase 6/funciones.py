def add_numbers(a: int, b: int) -> int:      ########## a y b son parametros, no  es lo mismo que num1 y num2
    return a + b
 ###################################################### delimito la funcion
 
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
result = add_numbers(num1, num2)
print(result)
 