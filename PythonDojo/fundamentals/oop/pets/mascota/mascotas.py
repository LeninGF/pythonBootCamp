class Mascota():
    def __init__(self, nombre, tipo, golosinas, salud=40, energia=40, sonido='miau'):
        self.nombre = nombre
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = salud
        self.energia = energia
        self.sonido = sonido
    def comer(self):
        self.energia += 5
        self.salud += 10
        return self
    def dormir(self):
        self.energia+=25
        return self
    def jugar(self):
        self.salud+=5
        return self
    def hacer_ruido(self):
        return self.sonido
    def estado(self):
        return {'salud':self.salud, 'energia':self.energia}

if __name__=="__main__":
    print("Clase Mascotas")

