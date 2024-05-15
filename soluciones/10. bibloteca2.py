class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Usuario(Persona):
    def __init__(self, nombre, edad, numero_usuario):
        super().__init__(nombre, edad)
        self.numero_usuario = numero_usuario

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Usuario: {self.numero_usuario}")

class Empleado(Persona):
    def __init__(self, nombre, edad, id_empleado, salario):
        super().__init__(nombre, edad)
        self.id_empleado = id_empleado
        self.salario = salario

    def mostrar_info(self):
        super().mostrar_info()
        print(f"ID de Empleado: {self.id_empleado}, Salario: {self.salario}")

class Libro:
    def __init__(self, id_libro, titulo, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor

    def mostrar_info(self):
        print(f"ID de Libro: {self.id_libro}, Título: {self.titulo}, Autor: {self.autor}")

# Ejemplo de uso
usuario1 = Usuario("Ana Martínez", 20, "USR123")
empleado1 = Empleado("Carlos Torres", 30, "EMP456", 1800)
libro1 = Libro("LIB789", "El Quijote", "Miguel de Cervantes")

usuario1.mostrar_info()
print()
empleado1.mostrar_info()
print()
libro1.mostrar_info()
