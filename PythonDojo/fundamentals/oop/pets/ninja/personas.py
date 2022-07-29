class Ninja():
    def __init__(self, nombre, apellido, mascotas, premio, comida_mascotas):
        self.nombre = nombre
        self.apellido = apellido
        self.mascotas = mascotas
        self.premio = premio
        self.comida_mascota = comida_mascotas
    def caminar(self):
        self.mascotas.jugar()
        print(f"paseando a {self.mascotas.nombre}")
    def alimentar(self):
        self.mascotas.comer()
        print(f"alimentando a {self.mascotas.nombre} con {self.comida_mascota}")
    def bañar(self):
        self.mascotas.hacer_ruido()
        print(f"bañando a {self.mascotas.nombre}")


      	
    
if __name__=="__main__":
    print("Clase Personas")
