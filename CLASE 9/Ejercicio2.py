def linear_search(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo.lower():
            return f"{objetivo} SI está en la lista, y esta en la posición {i}"
    return f"{objetivo} NO está en la lista"
 
# Ejemplo de uso
lista = ["manzana", "banana", "cereza", "durazno", "uva"]
resultado = linear_search(lista, "naranja").lower()  
print(resultado)