def mi_funcion(a, b)->int:
    resultado= a+b
    return resultado
x=int(input("Ingrese un valor: "))
y=int(input("ingrese otro valor: "))  
suma=mi_funcion(x, y)  #guardo el valor en la variable suma
print(suma)
