def linear_search(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return f"{objetivo} SI está en la lista, y esta en la posición {i}"
    return f"{objetivo} NO está en la lista"
 
# Ejemplo de uso
lista = [3, 7, 1, 9, 5]
resultado = linear_search(lista, 9)  
print(resultado)
 