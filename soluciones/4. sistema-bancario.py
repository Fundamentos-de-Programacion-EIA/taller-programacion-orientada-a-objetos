class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Cliente(Persona):
    def __init__(self, nombre, edad, numero_cuenta, saldo):
        super().__init__(nombre, edad)
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Cuenta: {self.__numero_cuenta}, Saldo: {self.__saldo}")

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito realizado. Nuevo saldo: {self.__saldo}")
        else:
            print("Cantidad no válida para depositar.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro realizado. Nuevo saldo: {self.__saldo}")
        else:
            print("Cantidad no válida para retirar.")

class Empleado(Persona):
    def __init__(self, nombre, edad, id_empleado, salario):
        super().__init__(nombre, edad)
        self.__id_empleado = id_empleado
        self.__salario = salario

    def mostrar_info(self):
        super().mostrar_info()
        print(f"ID de Empleado: {self.__id_empleado}, Salario: {self.__salario}")

# Ejemplo de uso
cliente1 = Cliente("Pedro López", 35, "CUENTA123", 5000)
empleado1 = Empleado("Laura Martínez", 28, "EMP5678", 2500)

cliente1.mostrar_info()
cliente1.depositar(1000)
cliente1.retirar(2000)
print()
empleado1.mostrar_info()
