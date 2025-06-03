def linear_search(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1
 
# Ejemplo de uso
lista = [3, 5, 2, 4, 9]
resultado = linear_search(lista, 150)  
print(resultado)