class Personaje():
    def __init__(self,nombre,clase,vida,fuerza,poder,ataque_especial):
        self.nombre = nombre
        self.clase=clase
        self.vida=vida
        self.fuerza=fuerza
        self.poder=poder
        self.ataque_especial=ataque_especial
        
    def mostrar_estado(self):
        print(f"{self.nombre} es de clase {self.clase}, tiene {self.vida} de vida, {self.fuerza}, y {self.poder} de poder.")
    def muerte(self):
        print(f"{self.nombre}  ha muerto..")
    def atacar(self):
        print(f"{self.nombre} esta atacando..")
    def defender(self):
        print(f"{self.nombre} se esta defendiendo..")
    def tomar_pocion(self):
        print(f"{self.nombre} se toma una pocion de vida y recupera su salud..")
    def usar_ataque_especial(self):
        print(f"{self.nombre} ataca con {self.ataque_especial}")
mago = Personaje("Gandalf","Mago",500, 30,700,"Kamehameha")
guerrero = Personaje("Gutz","Guerrero", 700, 60,500, "Hachazo profundo")  

print(mago.fuerza) #llamar el atribto del mago para mostrarlo. 
        
print("========Estos son los personajes=======")
mago.mostrar_estado()
guerrero.mostrar_estado()

print("=====Que comience la lucha========")
mago.atacar()
guerrero.defender()
guerrero.tomar_pocion()
guerrero.atacar()
mago.usar_ataque_especial()
mago.muerte()
print(f"El ganador es {guerrero.nombre}. Felicidades!")