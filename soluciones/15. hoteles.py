class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Huesped(Persona):
    def __init__(self, nombre, edad, numero_habitacion, fecha_checkin):
        super().__init__(nombre, edad)
        self.numero_habitacion = numero_habitacion
        self.fecha_checkin = fecha_checkin

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Habitación: {self.numero_habitacion}, Fecha de Check-in: {self.fecha_checkin}")

class Empleado(Persona):
    def __init__(self, nombre, edad, id_empleado, salario):
        super().__init__(nombre, edad)
        self.id_empleado = id_empleado
        self.salario = salario

    def mostrar_info(self):
        super().mostrar_info()
        print(f"ID de Empleado: {self.id_empleado}, Salario: {self.salario}")

# Ejemplo de uso
huesped1 = Huesped("Ana Gómez", 29, "HAB123", "2024-05-01")
empleado1 = Empleado("Pedro Ramírez", 35, "EMP789", 2500)

huesped1.mostrar_info()
print()
empleado1.mostrar_info()
