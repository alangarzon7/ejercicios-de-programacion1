"""En una competencia de boxeo, los luchadores se clasifican 
según su peso: 
● Menos de 60 kg: "Peso ligero" 
● Entre 60 y 80 kg: "Peso medio" 
● Más de 80 kg: "Peso pesado" Pedí al usuario su peso y 
mostrá su categoría."""
peso=float(input("Ingrese su peso para determinar su categoria: "))
if peso<60:
    print(f"Si tu peso es {peso}, tu categoria es Peso Ligero")
elif peso>=60 and peso<=80:
    print(f"Si tu peso es {peso}, tu categoria es Peso Medio")
else:
    print("Tu categoria es Peso Pesado")