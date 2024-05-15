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

class Vehiculo:
    def __init__(self, numero_matricula, modelo, precio_por_dia):
        self.numero_matricula = numero_matricula
        self.modelo = modelo
        self.precio_por_dia = precio_por_dia

    def mostrar_info(self):
        print(f"Número de Matrícula: {self.numero_matricula}, Modelo: {self.modelo}, Precio por Día: {self.precio_por_dia}")

class Coche(Vehiculo):
    def __init__(self, numero_matricula, modelo, precio_por_dia):
        super().__init__(numero_matricula, modelo, precio_por_dia)

class Moto(Vehiculo):
    def __init__(self, numero_matricula, modelo, precio_por_dia):
        super().__init__(numero_matricula, modelo, precio_por_dia)

# Ejemplo de uso
cliente1 = Cliente("Luis Martínez", 30, "CLI001")
coche1 = Coche("MAT123", "Toyota Corolla", 50)
moto1 = Moto("MAT456", "Yamaha R3", 30)

cliente1.mostrar_info()
print()
coche1.mostrar_info()
print()
moto1.mostrar_info()
