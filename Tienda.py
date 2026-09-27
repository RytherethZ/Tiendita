class InventarioTienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = []

    def _buscar_producto(self, nombre):
        nombre = nombre.strip().lower()

        for producto in self.productos:
            if producto["nombre"].strip().lower() == nombre:
                return producto

        return None

    def agregar_producto(self, nombre, precio, cantidad):
        if precio <= 0 or cantidad <= 0:
            return False

        nombre = nombre.strip()
        producto_existente = self._buscar_producto(nombre)

        if producto_existente:
            producto_existente["precio"] = precio
            producto_existente["cantidad"] += cantidad
        else:
            self.productos.append({
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            })

        return True

    def vender_producto(self, nombre, cantidad):
        if cantidad <= 0:
            return "La cantidad debe ser positiva."

        producto = self._buscar_producto(nombre)

        if producto is None:
            return "El producto no existe."

        if cantidad > producto["cantidad"]:
            return "No hay suficiente stock."

        producto["cantidad"] -= cantidad

        return "Venta realizada correctamente."

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
            return

        print(f"\nInventario de {self.nombre_tienda}")
        print("-" * 45)

        for producto in self.productos:
            print(
                f"Producto: {producto['nombre']} | "
                f"Precio: {producto['precio']:.2f} | "
                f"Cantidad: {producto['cantidad']}"
            )

        print("-" * 45)

    def producto_mas_caro(self):
        if not self.productos:
            return None

        producto_caro = max(
            self.productos,
            key=lambda producto: producto["precio"]
        )

        return producto_caro["nombre"], producto_caro["precio"]


def main():
    tienda = InventarioTienda("Mi Tienda")

    while True:
        print("\n===== MENÚ =====")
        print("1. Agregar producto")
        print("2. Vender producto")
        print("3. Ver inventario")
        print("4. Consultar producto más caro")
        print("5. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre del producto: ").strip()

            if not nombre:
                print("El nombre no puede estar vacío.")
                continue

            try:
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad del producto: "))
            except ValueError:
                print("Precio o cantidad inválidos. Debes escribir números.")
                continue

            if tienda.agregar_producto(nombre, precio, cantidad):
                print("Producto agregado o actualizado correctamente.")
            else:
                print("El precio y la cantidad deben ser positivos.")

        elif opcion == "2":
            nombre = input("Nombre del producto a vender: ").strip()

            if not nombre:
                print("El nombre no puede estar vacío.")
                continue

            try:
                cantidad = int(input("Cantidad a vender: "))
            except ValueError:
                print("La cantidad debe ser un número entero.")
                continue

            mensaje = tienda.vender_producto(nombre, cantidad)
            print(mensaje)

        elif opcion == "3":
            tienda.mostrar_inventario()

        elif opcion == "4":
            resultado = tienda.producto_mas_caro()

            if resultado is None:
                print("No hay productos en el inventario.")
            else:
                nombre, precio = resultado
                print(f"El producto más caro es {nombre} con precio {precio:.2f}.")

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()