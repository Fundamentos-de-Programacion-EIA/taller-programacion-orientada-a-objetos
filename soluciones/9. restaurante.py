class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Mesero(Persona):
    def __init__(self, nombre, edad, id_empleado):
        super().__init__(nombre, edad)
        self.id_empleado = id_empleado

    def mostrar_info(self):
        super().mostrar_info()
        print(f"ID de Empleado: {self.id_empleado}")

class Platillo:
    def __init__(self, id_platillo, nombre, precio):
        self.id_platillo = id_platillo
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        print(f"ID de Platillo: {self.id_platillo}, Nombre: {self.nombre}, Precio: {self.precio}")

# Ejemplo de uso
mesero1 = Mesero("José Pérez", 25, "EMP789")
platillo1 = Platillo("PLAT001", "Enchiladas", 150)

mesero1.mostrar_info()
print()
platillo1.mostrar_info()
