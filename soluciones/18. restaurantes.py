class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Cliente(Persona):
    def __init__(self, nombre, edad, numero_mesa, pedido):
        super().__init__(nombre, edad)
        self.numero_mesa = numero_mesa
        self.pedido = pedido

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Mesa: {self.numero_mesa}, Pedido: {self.pedido}")

class Mesero(Persona):
    def __init__(self, nombre, edad, id_empleado, seccion_asignada):
        super().__init__(nombre, edad)
        self.id_empleado = id_empleado
        self.seccion_asignada = seccion_asignada

    def mostrar_info(self):
        super().mostrar_info()
        print(f"ID de Empleado: {self.id_empleado}, Sección Asignada: {self.seccion_asignada}")

# Ejemplo de uso
cliente1 = Cliente("Sofía Morales", 28, "MESA10", "Enchiladas")
mesero1 = Mesero("Pedro García", 32, "EMP567", "Sección A")

cliente1.mostrar_info()
print()
mesero1.mostrar_info()
