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
        print(f"Balance: ${self.balance}")
        return self
    
    def generar_interes(self):
        if self.balance > 0:
            self.balance += self.balance*self.tasa_interes
        return self
    @classmethod
    def retornar_info_cuentas(cls):
        for i, cuenta in enumerate(cls.todas_las_cuentas):
            print(f"Cuenta {i}: ")
            cuenta.mostrar_info_cuenta()

cuenta1 = CuentaBancaria(tasa_interes=0.03, balance=800)
cuenta1.deposito(100).deposito(50).retiro(60).generar_interes().mostrar_info_cuenta()

cuenta2 = CuentaBancaria(balance=50)
cuenta2.deposito(300).deposito(50).retiro(100).retiro(100).retiro(50).retiro(150).generar_interes().mostrar_info_cuenta()

CuentaBancaria.retornar_info_cuentas()