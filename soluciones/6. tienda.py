class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Cliente(Persona):
    def __init__(self, nombre, edad, numero_cliente):
        super().__init__(nombre, edad)
        self.numero_cliente = numero_cliente

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Cliente: {self.numero_cliente}")

class Empleado(Persona):
    def __init__(self, nombre, edad, id_empleado, salario):
        super().__init__(nombre, edad)
        self.__id_empleado = id_empleado
        self.__salario = salario

    def mostrar_info(self):
        super().mostrar_info()
        print(f"ID de Empleado: {self.__id_empleado}, Salario: {self.__salario}")

class Producto:
    def __init__(self, id_producto, nombre, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        print(f"ID de Producto: {self.id_producto}, Nombre: {self.nombre}, Precio: {self.precio}")

    def aplicar_descuento(self, porcentaje):
        if 0 < porcentaje < 100:
            self.precio -= self.precio * (porcentaje / 100)
            print(f"Descuento aplicado. Nuevo precio: {self.precio}")
        else:
            print("Porcentaje de descuento no válido.")

# Ejemplo de uso
cliente1 = Cliente("Ana Rodríguez", 30, "CLI123")
empleado1 = Empleado("Luis Gómez", 25, "EMP456", 1500)
producto1 = Producto("PROD789", "Laptop", 1200)

cliente1.mostrar_info()
print()
empleado1.mostrar_info()
print()
producto1.mostrar_info()
producto1.aplicar_descuento(10)
