"""5. Menú de opciones (condicional múltiple) 
Situación: El programa debe simular un menú bancario 
simple. 
Mostrar el siguiente menú al usuario: 
1. Ver saldo   
2. Realizar transferencia   
3. Salir
El usuario debe ingresar un número del 1 al 3 según la opción 
que quiera. El programa mostrará un mensaje correspondiente: 
● Si elige 1 → mostrar "Su saldo es $15.000" 
● Si elige 2 → mostrar "Transferencia realizada con éxito" 
● Si elige 3 → mostrar "Saliendo del sistema..." 
● Si elige otro número → mostrar "Opción inválida" """

print("Menú de opciones:") 
print("1. Ver saldo") 
print("2. Realizar transferencia") 
print("3. Salir") 
opcion = int(input("Ingrese una opción (1-3): ")) 
if opcion == 1: 
    print("Su saldo es $15.000") 
elif opcion == 2: 
    print("Transferencia realizada con éxito") 
elif opcion == 3: 
    print("Saliendo del sistema .") 
else: 
    print("Opción inválida") 