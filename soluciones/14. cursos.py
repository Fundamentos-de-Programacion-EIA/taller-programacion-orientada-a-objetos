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

class Instructor(Persona):
    def __init__(self, nombre, edad, id_instructor, materia):
        super().__init__(nombre, edad)
        self.id_instructor = id_instructor
        self.materia = materia

    def mostrar_info(self):
        super().mostrar_info()
        print(f"ID de Instructor: {self.id_instructor}, Materia: {self.materia}")

# Ejemplo de uso
estudiante1 = Estudiante("María López", 20, "MAT2021", 3.5)
instructor1 = Instructor("Juan Pérez", 50, "INST102", "Física")

estudiante1.mostrar_info()
print(f"¿Está aprobado? {estudiante1.esta_aprobado()}")
print()
instructor1.mostrar_info()
