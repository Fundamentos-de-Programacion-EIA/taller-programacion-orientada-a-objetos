class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Conductor(Persona):
    def __init__(self, nombre, edad, numero_licencia):
        super().__init__(nombre, edad)
        self.numero_licencia = numero_licencia

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Licencia: {self.numero_licencia}")

class Vehiculo:
    def __init__(self, numero_matricula, modelo):
        self.numero_matricula = numero_matricula
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Número de Matrícula: {self.numero_matricula}, Modelo: {self.modelo}")

# Ejemplo de uso
conductor1 = Conductor("Jorge Sánchez", 45, "LIC12345")
vehiculo1 = Vehiculo("MAT6789", "Toyota Corolla")

conductor1.mostrar_info()
print()
vehiculo1.mostrar_info()
