"""
    Programacion orientada a Objetos 1
    Silvana Arévaldo
"""

class Usuario():
    def __init__(self, nombre, email) -> None:
        self.nombre = nombre
        self.email = email
        self.balance = 0
    def mostrar_balance_usuario(self):
        print(f"El usuario {self.nombre} tiene un balance de {self.balance}")
    
    def hacer_retiro(self, cantidad):
        self.balance -= cantidad
        
    def hacer_deposito(self, cantidad):
        self.balance += cantidad
        
    def transferencia(self, cantidad, nombre_receptor):
        if nombre_receptor == self.nombre:
            # si soy receptor de transferencia, incrementar y actualizo balance
            self.balance += cantidad
            print(f"{self.nombre} ha recibido {cantidad}")
        else:
            # soy emisor de la transferencia, debito y retorno quien debe recibir
            self.balance -= cantidad
            print(f"ha transferido {cantidad} al usuario {nombre_receptor}")
        return (cantidad, nombre_receptor)


juanaArco = Usuario(nombre='Maria de Arco',
                     email='juana.arco@historia.com')
juanaArco.balance = 1250.12
richardDawkins = Usuario(nombre='Richard Dawkins',
                     email='richard.dawkins@biologia.com')
richardDawkins.balance = 250.78
carlSagan = Usuario(nombre='Carl Sagan',
                     email='carl.sagan@cosmos.com')
carlSagan.balance = 225.6

juanaArco.hacer_deposito(25)
juanaArco.hacer_deposito(12)
juanaArco.hacer_deposito(28)
juanaArco.hacer_retiro(150.28)

richardDawkins.hacer_deposito(2500)
richardDawkins.hacer_deposito(150)
richardDawkins.hacer_retiro(600)
richardDawkins.hacer_retiro(500)

carlSagan.hacer_deposito(450)
carlSagan.hacer_retiro(10)
carlSagan.hacer_retiro(20)
carlSagan.hacer_retiro(30)

print(juanaArco.mostrar_balance_usuario())
print(richardDawkins.mostrar_balance_usuario())
print(carlSagan.mostrar_balance_usuario())

# transferencia de dinero
print("Haciendo transferencia")
(cantidad_t, receptor_q) = juanaArco.transferencia(100, 'Carl Sagan')
carlSagan.transferencia(cantidad=cantidad_t, nombre_receptor=receptor_q)
print(juanaArco.mostrar_balance_usuario())
print(carlSagan.mostrar_balance_usuario())
