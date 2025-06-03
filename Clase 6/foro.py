def calcular_promedio(numeros): #defino la funcion
    if len(numeros) == 0: #si no hay elementos en la lista...
        return 0          #me retorna cero por no haber elementos en la lista
    return sum(numeros) / len(numeros) #sum es una funcion predeterminada, y len tambien, juntas me calcularn el promedio de la lista

print(calcular_promedio([10, 20, 30]))  # llamo a la funcion y con numeros determinados(no los ingreso por teclado)
print(calcular_promedio([]))            # me muestra el resultado de la funcion con los numeros determinados