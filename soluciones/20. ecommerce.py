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
        self.carrito_compras = []
        self.historial_compras = []

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Cliente: {self.numero_cliente}")

    def agregar_al_carrito(self, producto):
        self.carrito_compras.append(producto)

    def finalizar_compra(self):
        self.historial_compras.extend(self.carrito_compras)
        self.carrito_compras.clear()
        print("Compra finalizada. El carrito está vacío.")

class Producto:
    def __init__(self, id_producto, nombre, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        print(f"ID de Producto: {self.id_producto}, Nombre: {self.nombre}, Precio: {self.precio}")

# Ejemplo de uso
cliente1 = Cliente("Carlos Méndez", 32, "CLI123")
producto1 = Producto("PROD001", "Laptop", 1500)
producto2 = Producto("PROD002", "Smartphone", 800)

cliente1.agregar_al_carrito(producto1)
cliente1.agregar_al_carrito(producto2)

cliente1.mostrar_info()
print("Carrito de Compras:")
for producto in cliente1.carrito_compras:
    producto.mostrar_info()

cliente1.finalizar_compra()
print("Historial de Compras:")
for producto in cliente1.historial_compras:
    producto.mostrar_info()
