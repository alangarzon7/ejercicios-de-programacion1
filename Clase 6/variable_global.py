x=int(input("Ingrese un valor: "))  #variable global
def mi_funcion()->int:
    x=20  #variable local(solo esta dentro de la funcion )
    print(x)   #output : 20
mi_funcion()   #llamo a la funcion
print(x)  #output : valor ingresado
