def binary_search(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
 
# Ejemplo de uso
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = binary_search(lista, 5)  # Devuelve 3,,,,resvisar pq el profe cambio el numero
print(resultado)
 