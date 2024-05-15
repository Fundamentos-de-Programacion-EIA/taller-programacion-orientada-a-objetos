class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Paciente(Persona):
    def __init__(self, nombre, edad, numero_historia_clinica):
        super().__init__(nombre, edad)
        self.numero_historia_clinica = numero_historia_clinica

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Historia Clínica: {self.numero_historia_clinica}")

class Medico(Persona):
    def __init__(self, nombre, edad, numero_licencia, especialidad):
        super().__init__(nombre, edad)
        self.numero_licencia = numero_licencia
        self.especialidad = especialidad

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Licencia: {self.numero_licencia}, Especialidad: {self.especialidad}")

# Ejemplo de uso
paciente1 = Paciente("Juan Pérez", 30, "HC12345")
medico1 = Medico("Dra. María García", 45, "MED6789", "Cardiología")

paciente1.mostrar_info()
print()
medico1.mostrar_info()
