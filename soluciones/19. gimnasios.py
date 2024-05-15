class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Socio(Persona):
    def __init__(self, nombre, edad, numero_membresia, plan_entrenamiento):
        super().__init__(nombre, edad)
        self.numero_membresia = numero_membresia
        self.plan_entrenamiento = plan_entrenamiento

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Membresía: {self.numero_membresia}, Plan de Entrenamiento: {self.plan_entrenamiento}")

class Entrenador(Persona):
    def __init__(self, nombre, edad, id_entrenador, especialidad):
        super().__init__(nombre, edad)
        self.id_entrenador = id_entrenador
        self.especialidad = especialidad

    def mostrar_info(self):
        super().mostrar_info()
        print(f"ID de Entrenador: {self.id_entrenador}, Especialidad: {self.especialidad}")

# Ejemplo de uso
socio1 = Socio("Martín Pérez", 24, "MEMB001", "Plan Avanzado")
entrenador1 = Entrenador("Laura Sánchez", 30, "ENT002", "CrossFit")

socio1.mostrar_info()
print()
entrenador1.mostrar_info()
