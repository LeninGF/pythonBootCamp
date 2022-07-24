#
#    Programacion orientada a Objetos 1
#    Silvana Arévaldo
#

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.balance = 0
        
    def mostrar_balance_usuario(self):
        print(f"El usuario {self.nombre} tiene un balance de {self.balance}")
        return self
    
    def hacer_retiro(self, cantidad):
        self.balance -= cantidad
        return self
        
    def hacer_deposito(self, cantidad):
        self.balance += cantidad
        return self
        
    def transferencia(self, cantidad, usuario_receptor):
        if usuario_receptor.nombre == self.nombre:
            # si soy receptor de transferencia, incrementar y actualizo balance
            self.balance += cantidad
            print(f"{self.nombre} ha recibido {cantidad}")
        else:
            # soy emisor de la transferencia, debito y retorno quien debe recibir
            self.balance -= cantidad
            print(f"ha transferido {cantidad} al usuario {usuario_receptor.nombre}")
        return (cantidad, usuario_receptor.nombre)


juanaArco = Usuario(nombre='Maria de Arco',
                     email='juana.arco@historia.com')
juanaArco.balance = 1250.12
richardDawkins = Usuario(nombre='Richard Dawkins',
                     email='richard.dawkins@biologia.com')
richardDawkins.balance = 250.78
carlSagan = Usuario(nombre='Carl Sagan',
                     email='carl.sagan@cosmos.com')
carlSagan.balance = 225.6

juanaArco.hacer_deposito(25).hacer_deposito(12).hacer_deposito(28).hacer_retiro(150.28)

richardDawkins.hacer_deposito(2500).hacer_deposito(150).hacer_retiro(600).hacer_retiro(500)

carlSagan.hacer_deposito(450).hacer_retiro(10).hacer_retiro(20).hacer_retiro(30)

print(juanaArco.mostrar_balance_usuario())
print(richardDawkins.mostrar_balance_usuario())
print(carlSagan.mostrar_balance_usuario())

# transferencia de dinero
print("Haciendo transferencia")
(cantidad_t, receptor_q) = juanaArco.transferencia(100, carlSagan)
print(juanaArco.mostrar_balance_usuario())
print(carlSagan.mostrar_balance_usuario())

# class User:

#     def __init__(self, name):
#         self.name = name
#         self.amount = 0

#     def make_deposit(self, amount):
#         self.amount += amount

#     def make_withdrawl(self,amount):
#         self.amount -= amount

#     def display_user_balance(self):
#         print(f"User: {self.name}, Balance: {self.amount}")

#     def transfer_money(self,amount,user):
#         self.amount -= amount
#         user.amount += amount
#         self.display_user_balance()
#         user.display_user_balance()


# adrien = User("Adrien")
# nibbles = User("Mr. Nibbles")
# benny_bob = User("Benny Bob")

# adrien.make_deposit(100)
# adrien.make_deposit(200)
# adrien.make_deposit(50)
# adrien.make_withdrawl(45)
# adrien.display_user_balance()

# nibbles.make_deposit(1000)
# nibbles.make_deposit(1000)
# nibbles.make_withdrawl(500)
# nibbles.make_withdrawl(300)
# nibbles.display_user_balance()

# benny_bob.make_deposit(1500)
# benny_bob.make_withdrawl(1000)
# benny_bob.make_withdrawl(5000)
# benny_bob.make_withdrawl(3000)
# benny_bob.display_user_balance()


# nibbles.transfer_money(400, adrien)