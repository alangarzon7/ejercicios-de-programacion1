# Lista para almacenar los datos de los estudiantes
estudiantes = []

while True:
    # Pedir datos al usuario
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = input("Ingrese la edad del estudiante: ")
    ciudad = input("Ingrese la ciudad del estudiante: ")

    # Guardar los datos en un diccionario y agregarlo a la lista
    estudiante = {"Nombre": nombre,
                  "Edad": edad,
                  "Ciudad": ciudad}
    estudiantes.append(estudiante)

    # Preguntar si desea agregar otro estudiante
    continuar = input("¿Desea agregar otro estudiante? (si/no): ").lower()
    if continuar != "sí":
        break  # Salir del bucle si el usuario no quiere agregar más estudiantes

# Mostrar la lista de estudiantes ingresados
for i in estudiantes:
    print(i)