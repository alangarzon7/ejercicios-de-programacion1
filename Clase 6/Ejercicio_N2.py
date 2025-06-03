"""Crear una función que calcule el IVA de un producto
y lo imprima con la leyenda “El IVA correspondiente al
(valor ingresado) es (resultado de la función)."""

def iva(n:float):
    return n *0.21
precio_producto=float(input("Ingrese el precio del producto: "))
iva_producto=iva(precio_producto)
print(f"El IVA correspondiente a {precio_producto} es {iva_producto}")