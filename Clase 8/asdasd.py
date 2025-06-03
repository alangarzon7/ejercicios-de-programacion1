# se crea un diccionario "personas", con distintas claves que en este caso son los nombres de las personas, y los valores son su edad.
personas = {
"Alan": 25,
"María": 30,
"Carlos": 22
}

# Se agrega una nuevo nombre(clave) al diciconario y se le asigna el valor (edad) de 28
personas["Lucía"] = 28

# Mostrar todas las claves y valores con un bucle
for nombre, edad in personas.items():
   print(f"{nombre}: {edad} años")