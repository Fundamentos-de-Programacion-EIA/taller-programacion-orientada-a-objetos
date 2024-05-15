class Producto:
    def __init__(self, id_producto, nombre, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        print(f"ID de Producto: {self.id_producto}, Nombre: {self.nombre}, Precio: {self.precio}")

class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_info(self):
        print(f"ID de Categoría: {self.id_categoria}, Nombre: {self.nombre}")
        print("Productos:")
        for producto in self.productos:
            producto.mostrar_info()

# Ejemplo de uso
producto1 = Producto("PROD001", "Laptop", 1500)
producto2 = Producto("PROD002", "Smartphone", 800)
categoria1 = Categoria("CAT001", "Electrónica")

categoria1.agregar_producto(producto1)
categoria1.agregar_producto(producto2)
categoria1.mostrar_info()
