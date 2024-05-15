class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, numero_matricula, promedio):
        super().__init__(nombre, edad)
        self.numero_matricula = numero_matricula
        self.promedio = promedio

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Matrícula: {self.numero_matricula}, Promedio: {self.promedio}")

    def esta_aprobado(self):
        return self.promedio >= 3.0

class Profesor(Persona):
    def __init__(self, nombre, edad, numero_empleado, materia):
        super().__init__(nombre, edad)
        self.numero_empleado = numero_empleado
        self.materia = materia

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Empleado: {self.numero_empleado}, Materia: {self.materia}")

# Ejemplo de uso
estudiante1 = Estudiante("María López", 20, "MAT2021", 3.5)
profesor1 = Profesor("Juan Pérez", 50, "EMP102", "Física")

estudiante1.mostrar_info()
print(f"¿Está aprobado? {estudiante1.esta_aprobado()}")
print()
profesor1.mostrar_info()
