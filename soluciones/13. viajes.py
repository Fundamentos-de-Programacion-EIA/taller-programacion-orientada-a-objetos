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

class AgenteViajes(Persona):
    def __init__(self, nombre, edad, id_agente):
        super().__init__(nombre, edad)
        self.id_agente = id_agente
        self.viajes_gestionados = []

    def agregar_viaje(self, viaje):
        self.viajes_gestionados.append(viaje)

    def mostrar_info(self):
        super().mostrar_info()
        print(f"ID de Agente: {self.id_agente}")
        print("Viajes Gestionados:")
        for viaje in self.viajes_gestionados:
            print(f" - {viaje}")

# Ejemplo de uso
cliente1 = Cliente("Carlos Méndez", 32, "CLI123")
agente1 = AgenteViajes("Laura Jiménez", 29, "AGT456")
agente1.agregar_viaje("Viaje a París")
agente1.agregar_viaje("Viaje a Nueva York")

cliente1.mostrar_info()
print()
agente1.mostrar_info()
