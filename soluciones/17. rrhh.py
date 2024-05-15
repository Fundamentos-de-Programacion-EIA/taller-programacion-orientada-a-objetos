class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Empleado(Persona):
    def __init__(self, nombre, edad, id_empleado, salario, posicion):
        super().__init__(nombre, edad)
        self.id_empleado = id_empleado
        self.salario = salario
        self.posicion = posicion

    def mostrar_info(self):
        super().mostrar_info()
        print(f"ID de Empleado: {self.id_empleado}, Salario: {self.salario}, Posición: {self.posicion}")

class Contratista(Persona):
    def __init__(self, nombre, edad, id_contratista, tarifa_por_hora, proyecto_asignado):
        super().__init__(nombre, edad)
        self.id_contratista = id_contratista
        self.tarifa_por_hora = tarifa_por_hora
        self.proyecto_asignado = proyecto_asignado

    def mostrar_info(self):
        super().mostrar_info()
        print(f"ID de Contratista: {self.id_contratista}, Tarifa por Hora: {self.tarifa_por_hora}, Proyecto Asignado: {self.proyecto_asignado}")

# Ejemplo de uso
empleado1 = Empleado("Laura Torres", 29, "EMP123", 3000, "Gerente de Proyecto")
contratista1 = Contratista("Carlos Mendoza", 35, "CON456", 50, "Desarrollo Web")

empleado1.mostrar_info()
print()
contratista1.mostrar_info()
