"""
Cuenta Bancaria
Silvana Arevalo

"""

class CuentaBancaria:
    # atributos de la clase
    todas_las_cuentas = []
    
    def __init__(self, tasa_interes=0.01, balance=0):
        # atributos de instancia
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)
    
    def deposito(self, cantidad):
        self.balance += cantidad
        return self
    def retiro(self, cantidad):
        if cantidad > self.balance:
            print("Fondos insuficientes: Cobrando una tarifa de $5 USD")
            self.balance -= 5
        else:
            self.balance -= cantidad
        return self
    def mostrar_info_cuenta(self):
        return f"Balance: ${self.balance}"
    
    def generar_interes(self):
        if self.balance > 0:
            self.balance += self.balance*self.tasa_interes
        return self
    @classmethod
    def retornar_info_cuentas(cls):
        for i, cuenta in enumerate(cls.todas_las_cuentas):
            print(f"Cuenta {i}: ")
            cuenta.mostrar_info_cuenta()


class Usuario:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuenta = {
            'ahorros': CuentaBancaria(tasa_interes=0.02, balance=200), 
            'corriente': CuentaBancaria(tasa_interes=0.05, balance=1000) 
            }
        
    def mostrar_balance_usuario(self):
        for k in self.cuenta.keys():
            print(f"Cuenta {k}")
            print(self.cuenta[k].mostrar_info_cuenta())
        return self
    
    def hacer_retiro(self, tipo_cuenta, cantidad):
        self.cuenta[tipo_cuenta].retiro(cantidad=cantidad)
        return self
        
    def hacer_deposito(self, tipo_cuenta, cantidad):
        self.cuenta[tipo_cuenta].deposito(cantidad=cantidad)
        return self
        
    def transferencia(self, cantidad, usuario_receptor, tipo_cuenta):
        if usuario_receptor.nombre == self.nombre:
            # si soy receptor de transferencia, incrementar y actualizo balance
            self.cuenta[tipo_cuenta].deposito(cantidad=cantidad)
            print(f"{self.nombre} ha recibido {cantidad} a la cuenta {tipo_cuenta}")
        else:
            # soy emisor de la transferencia, debito y retorno quien debe recibir
            self.cuenta[tipo_cuenta].retiro(cantidad=cantidad)
            print(f"ha transferido {cantidad} de la cuenta {tipo_cuenta} al usuario {usuario_receptor.nombre}")
        return (cantidad, usuario_receptor.nombre)



# cuenta1 = CuentaBancaria(tasa_interes=0.03, balance=800)
# cuenta1.deposito(100).deposito(50).retiro(60).generar_interes().mostrar_info_cuenta()

# cuenta2 = CuentaBancaria(balance=50)
# cuenta2.deposito(300).deposito(50).retiro(100).retiro(100).retiro(50).retiro(150).generar_interes().mostrar_info_cuenta()

# CuentaBancaria.retornar_info_cuentas()

juanaArco = Usuario(nombre='Maria de Arco')
juanaArco.hacer_deposito(cantidad=25, tipo_cuenta='ahorros').hacer_deposito(cantidad=12, tipo_cuenta='corriente').hacer_deposito(cantidad=28, tipo_cuenta='ahorros').hacer_retiro(cantidad=150, tipo_cuenta='corriente').mostrar_balance_usuario()