class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Empleado(Persona):
    def __init__(self, nombre, edad, id_empleado, salario):
        super().__init__(nombre, edad)
        self.id_empleado = id_empleado
        self.salario = salario

    def mostrar_info(self):
        super().mostrar_info()
        print(f"ID de Empleado: {self.id_empleado}, Salario: {self.salario}")

class Proyecto:
    def __init__(self, id_proyecto, nombre, presupuesto):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.presupuesto = presupuesto
        self.empleados_asignados = []

    def asignar_empleado(self, empleado):
        self.empleados_asignados.append(empleado)

    def mostrar_info(self):
        print(f"ID de Proyecto: {self.id_proyecto}, Nombre: {self.nombre}, Presupuesto: {self.presupuesto}")
        print("Empleados asignados:")
        for empleado in self.empleados_asignados:
            empleado.mostrar_info()

# Ejemplo de uso
empleado1 = Empleado("Laura Sánchez", 35, "EMP123", 3000)
empleado2 = Empleado("Carlos Gómez", 40, "EMP124", 3200)
proyecto1 = Proyecto("PROY001", "Desarrollo de Software", 100000)

proyecto1.asignar_empleado(empleado1)
proyecto1.asignar_empleado(empleado2)
proyecto1.mostrar_info()
