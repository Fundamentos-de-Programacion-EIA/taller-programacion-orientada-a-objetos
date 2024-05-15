class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Participante(Persona):
    def __init__(self, nombre, edad, id_participante):
        super().__init__(nombre, edad)
        self.id_participante = id_participante

    def mostrar_info(self):
        super().mostrar_info()
        print(f"ID de Participante: {self.id_participante}")

class Organizador(Persona):
    def __init__(self, nombre, edad, id_organizador):
        super().__init__(nombre, edad)
        self.id_organizador = id_organizador
        self.eventos_organizados = []

    def agregar_evento(self, evento):
        self.eventos_organizados.append(evento)

    def mostrar_info(self):
        super().mostrar_info()
        print(f"ID de Organizador: {self.id_organizador}")
        print("Eventos Organizados:")
        for evento in self.eventos_organizados:
            print(f" - {evento}")

# Ejemplo de uso
participante1 = Participante("María García", 28, "PAR001")
organizador1 = Organizador("Luis Fernández", 35, "ORG002")
organizador1.agregar_evento("Conferencia de Tecnología")
organizador1.agregar_evento("Feria de Empleo")

participante1.mostrar_info()
print()
organizador1.mostrar_info()
