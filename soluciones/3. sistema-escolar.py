class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, numero_matricula):
        super().__init__(nombre, edad)
        self.numero_matricula = numero_matricula

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Matrícula: {self.numero_matricula}")

    def es_menor_de_edad(self):
        return self.edad < 18

class Profesor(Persona):
    def __init__(self, nombre, edad, numero_empleado, materia):
        super().__init__(nombre, edad)
        self.numero_empleado = numero_empleado
        self.materia = materia

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Empleado: {self.numero_empleado}, Materia: {self.materia}")

# Ejemplo de uso
estudiante1 = Estudiante("Ana Torres", 17, "MAT12345")
profesor1 = Profesor("Carlos Ruiz", 40, "EMP6789", "Matemáticas")

estudiante1.mostrar_info()
print(f"¿Es menor de edad? {estudiante1.es_menor_de_edad()}")
print()
profesor1.mostrar_info()
