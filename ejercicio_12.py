# 1.-, 2.-

class Cuenta:
    def __init__(self, saldo):
        """
        Constructor de la clase Cuenta.
        
        Args:
        saldo (float): Saldo inicial de la cuenta.
        """
        self.saldo = saldo
    
    def retirar(self, cantidad):
        """
        Método para retirar dinero de la cuenta.
        
        Args:
        cantidad (float): Cantidad a retirar.
        
        Returns:
        bool: True si el retiro fue exitoso, False si no hay suficiente saldo.
        """
        if self.saldo - cantidad >= 0:
            self.saldo -= cantidad
            return True
        else:
            print("No hay suficiente saldo en la cuenta.")
            return False
    
    def depositar(self, cantidad):
        """
        Método para depositar dinero en la cuenta.
        
        Args:
        cantidad (float): Cantidad a depositar.
        """
        self.saldo += cantidad

# Ejemplo de uso
# Crear una cuenta con saldo inicial de 1000
cuenta1 = Cuenta(1000)

# Depositar 500
cuenta1.depositar(500)

# Intentar retirar 200
retiro_exitoso = cuenta1.retirar(200)
if retiro_exitoso:
    print("Retiro exitoso. Saldo restante:", cuenta1.saldo)

# 3.-

class CuentaConDescubierto(Cuenta):
    def __init__(self, saldo, descubierto):
        """
        Constructor de la clase CuentaConDescubierto.
        
        Args:
        saldo (float): Saldo inicial de la cuenta.
        descubierto (float): Límite del descubierto permitido.
        """
        super().__init__(saldo)
        self.descubierto = descubierto
    
    def retirar(self, cantidad):
        """
        Método para retirar dinero de la cuenta con descubierto.
        
        Args:
        cantidad (float): Cantidad a retirar.
        
        Returns:
        bool: True si el retiro fue exitoso, False si el descubierto es insuficiente.
        """
        if self.saldo - cantidad >= -self.descubierto:
            self.saldo -= cantidad
            return True
        else:
            print("No se puede retirar esa cantidad. Saldo insuficiente.")
            return False

# Ejemplo de uso
# Crear una cuenta con saldo inicial de 1000 y descubierto de 500
cuenta2 = CuentaConDescubierto(1000, 500)

# Depositar 200
cuenta2.depositar(200)

# Intentar retirar 1800 (superando el descubierto)
retiro_exitoso = cuenta2.retirar(1800)
if retiro_exitoso:
    print("Retiro exitoso. Saldo restante:", cuenta2.saldo)
