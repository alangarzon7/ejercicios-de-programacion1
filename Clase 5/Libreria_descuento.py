"""Una librería ofrece un 10% de descuento a estudiantes y un 5% a 
jubilados. El resto de los clientes no tiene descuento. Pedí al 
usuario el monto total de la compra y si es estudiante o jubilado. 
Mostrá el total a pagar según corresponda."""
monto=float(input("Ingrese el monto total de la compra: "))
cliente=input("eres estudiante, jubilado o ninguno?: ").lower()
if cliente=="estudiante":
    print("Los estudiantes tienen un 10% de descuento")
    monto_final=monto*0.9
    print(f"El monto final a pagar con el descuento es {monto_final}")
elif cliente=="jubilado":
    print("Los jubilados tienen un 5% de descuento")
    monto_final=monto*0.95
    print(f"El monto final a pagar con el descuento es {monto_final}")
elif cliente=="ninguno":
    print(f"El monto a pagar es: {monto}")



    



    