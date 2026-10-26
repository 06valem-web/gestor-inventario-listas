productos = []
cantidades = []


def buscar_indice_producto(nombre_producto):
    nombre_limpio = nombre_producto.strip().lower()
    for i in range(len(productos)):
        if productos[i].lower() == nombre_limpio:
            return i
    return -1


def registrar_producto():
    print("Registrar producto...")
    nombre = input("Nombre del producto: ").strip()
    
    if len(nombre) == 0:
        print("El nombre del producto no puede estar vacío.")
        return

    indice = buscar_indice_producto(nombre)
    if indice != -1:
        print(f"El producto '{productos[indice]}' ya está registrado con una cantidad de {cantidades[indice]}.")
        print("Si desea actualizar la cantidad, elija la opción 4 del menú.")
        return

    try:
        cantidad = int(input("Cantidad disponible: "))
        if cantidad < 0:
            print("La cantidad no puede ser un número negativo.")
            return
    except ValueError:
        print("Error: La cantidad debe ser un número entero válido.")
        return

    productos.append(nombre)
    cantidades.append(cantidad)
    print(f"Producto '{nombre}' registrado exitosamente con cantidad {cantidad}.")


def mostrar_inventario():
    print("Inventario actual...")
    if len(productos) == 0:
        print("El inventario está vacío.")
    else:
        for i in range(len(productos)):
            print(f"{i + 1}. {productos[i]} - Cantidad: {cantidades[i]}")


def buscar_producto():
    print("Buscar producto...")
    if len(productos) == 0:
        print("El inventario está vacío.")
        return

    nombre = input("Ingrese el nombre del producto a buscar: ").strip()
    indice = buscar_indice_producto(nombre)

    if indice != -1:
        print(f"Producto encontrado: {productos[indice]} Cantidad disponible: {cantidades[indice]}")
    else:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")


def modificar_cantidad():
    print("Modificar cantidad de un producto...")
    if len(productos) == 0:
        print("El inventario está vacío.")
        return

    nombre = input("Ingrese el nombre del producto a modificar: ").strip()
    indice = buscar_indice_producto(nombre)

    if indice != -1:
        print(f"Cantidad actual de '{productos[indice]}': {cantidades[indice]}")
        try:
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            if nueva_cantidad < 0:
                print("La cantidad no puede ser negativa.")
                return
            cantidades[indice] = nueva_cantidad
            print(f"Cantidad de '{productos[indice]}' actualizada correctamente a {nueva_cantidad}.")
        except ValueError:
            print("Error: Ingrese un valor numérico entero.")
    else:
        print(f"No se puede modificar: El producto '{nombre}' no existe.")


def eliminar_producto():
    print("Eliminar un producto...")
    if len(productos) == 0:
        print("El inventario está vacío.")
        return

    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
    indice = buscar_indice_producto(nombre)

    if indice != -1:
        prod_eliminado = productos.pop(indice)
        cant_eliminada = cantidades.pop(indice)
        print(f"Se eliminó el producto '{prod_eliminado}' (Cantidad que tenía: {cant_eliminada}).")
        print("Listas sincronizadas correctamente.")
    else:
        print(f"No se puede eliminar: El producto '{nombre}' no existe.")


def mostrar_total_productos():
    print("Total de productos diferentes")
    total = len(productos)
    print(f"Actualmente hay {total} producto(s) diferente(s) registrado(s) en el inventario.")


def mostrar_producto_mayor_cantidad():
    print("Producto con mayor cantidad...")
    if len(productos) == 0:
        print("El inventario está vacío.")
        return

    max_cantidad = max(cantidades)
    indice_max = cantidades.index(max_cantidad)
    print(f"El producto con mayor cantidad es '{productos[indice_max]}' con {max_cantidad} unidades.")


def mostrar_resumen_inventario():
    print("Resumen general del inventario...")
    if len(productos) == 0:
        print("El inventario está vacío. No hay datos para resumir.")
        return

    total_diferentes = len(productos)
    total_unidades = sum(cantidades)
    max_cantidad = max(cantidades)
    indice_max = cantidades.index(max_cantidad)
    
    print(f"Total de productos diferentes: {total_diferentes}")
    print(f"Unidades totales en stock: {total_unidades}")
    print(f"Producto con mayor stock: '{productos[indice_max]}' ({max_cantidad} unidades)")


def mostrar_menu():
    print("      Menú...")
    print("1. Registrar un producto y su cantidad disponible")
    print("2. Mostrar todos los productos con su cantidad")
    print("3. Buscar un producto por su nombre")
    print("4. Modificar la cantidad disponible de un producto")
    print("5. Eliminar un producto del inventario")
    print("6. Mostrar cuántos productos diferentes hay registrados")
    print("7. Mostrar el producto con la mayor cantidad disponible")
    print("8. Mostrar el resumen del inventario")
    print("9. Salir del programa")



def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-9): ").strip().upper()

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            modificar_cantidad()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            mostrar_total_productos()
        elif opcion == "7":
            mostrar_producto_mayor_cantidad()
        elif opcion == "8":
            mostrar_resumen_inventario()
        elif opcion == "9":
            print("\n¡Gracias por utilizar el Gestor de Inventario! Hasta luego.")
            break
        else:
            print("\nOpción no válida. Por favor, ingrese un número del 1 al 9.")

main()