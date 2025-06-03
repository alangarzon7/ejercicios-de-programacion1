"""Crear una función que eleve un número al cuadrado y lo imprima."""
def cuadrado(a):
    return a**2 #para elevar a cualquier numero, se utiliza el **
num=int(input("Ingresa un numero para elevarlo al cuadrado: "))
resultado=cuadrado(num)
print(f"El cuadrado de {num} es {resultado}.") 