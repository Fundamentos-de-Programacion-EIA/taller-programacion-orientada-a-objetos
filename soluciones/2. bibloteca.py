class Publicacion:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_info(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}")

class Libro(Publicacion):
    def __init__(self, titulo, autor, numero_paginas):
        super().__init__(titulo, autor)
        self.numero_paginas = numero_paginas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Páginas: {self.numero_paginas}")

class Revista(Publicacion):
    def __init__(self, titulo, autor, numero_edicion):
        super().__init__(titulo, autor)
        self.numero_edicion = numero_edicion

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Edición: {self.numero_edicion}")

# Ejemplo de uso
libro1 = Libro("1984", "George Orwell", 328)
revista1 = Revista("National Geographic", "John Smith", 150)

libro1.mostrar_info()
print()
revista1.mostrar_info()
