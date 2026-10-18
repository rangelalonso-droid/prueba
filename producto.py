# Molde de un Gestor de inventarios
class Producto:
    # Constructor
    def __init__(self, id_producto, nombre, precio, cantidad_stock):
        # Atributos
        self.id = id_producto
        self.nombre = nombre
        self.precio = precio
        self.cantidad_stock = cantidad_stock

    # Método para mostrar información del producto
    def obtener_detalles(self):
        return f"ID: {self.id} | Producto: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.cantidad_stock} unidades."

    # Método para vender
    def vender(self, cantidad):
        if cantidad <= self.cantidad_stock:
            self.cantidad_stock -= cantidad
            print(f"VENTA EXITOSA: Se vendieron {cantidad} unidades de '{self.nombre}'.")
        else:
            print(f"No hay suficiente stock de '{self.nombre}' para {cantidad} unidades.")

    # Método para resurtir inventario
    def surtir(self, cantidad):
        self.cantidad_stock += cantidad
        print(f"Inventario actualizado, se agregaron {cantidad} unidades a '{self.nombre}'.")
