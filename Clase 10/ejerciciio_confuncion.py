# Función para pedir datos del estudiante
def pedir_datos():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = input("Ingrese la edad del estudiante: ")
    ciudad = input("Ingrese la ciudad del estudiante: ")
    return {"Nombre": nombre, "Edad": edad, "Ciudad": ciudad}

# Lista de estudiantes
estudiantes = []

while True:
    estudiantes.append(pedir_datos())  # Llamamos a la función para obtener los datos

    continuar = input("¿Desea agregar otro estudiante? (sí/no): ").lower()
    if continuar != "sí":
        break  # Si el usuario ingresa algo distinto de "sí", el programa termina

# Mostrar la lista de estudiantes../n es un salto de linea

print("\nLista de estudiantes ingresados:")
for estudiante in estudiantes:
    print(estudiante)