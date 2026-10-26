Nota: Capturas de las pruebas en el pdf.
1. Objetivo
El objetivo del programa es proveer una solución en consola para administrar los nombres y las cantidades disponibles de los productos de una tienda pequeña, aplicando conceptos fundamentales de programación como listas, índices, ciclos, condicionales y funciones en Python.
2. Requisitos para ejecutar el programa
Tener instalado Python en el equipo.
No se requiere el uso de bases de datos, archivos, clases, diccionarios ni librerías externas; funciona completamente con estructuras nativas básicas de Python.
3. Instrucciones de uso
   Abrir la terminal compatible con Python.
   Exportar y ejecutar el archivo principal mediante el comando: “python main.py”.
   El programa desplegará automáticamente un menú interactivo en la consola.
   Digite el número correspondiente a la opción que desea realizar (del 1 al 8) y siga las instrucciones en pantalla para ingresar, consultar, modificar o eliminar      los  datos del inventario.
4. Funciones implementadas
  registrar_producto(): Permite registrar el nombre de un producto y su cantidad disponible inicial.
  mostrar_inventario(): Muestra todos los productos registrados actualmente junto con sus respectivas cantidades.
  buscar_producto(): Permite buscar y consultar un producto específico ingresando su nombre.
  modificar_cantidad(): Actualiza la cantidad disponible de un producto existente, verificando primero que este se encuentre en el inventario.
  eliminar_producto(): Elimina un producto de las listas paralelas manteniendo la correcta sincronización de los índices.
  mostrar_total_productos(): Muestra la cantidad total de productos diferentes registrados en el sistema.
  mostrar_producto_mayor_cantidad(): Identifica y muestra el producto que cuenta con la mayor cantidad disponible en stock.
5. Explicación de la decisión para evitar duplicados en el registro
Para evitar registrar dos veces el mismo producto en las listas paralelas, el programa implementa una validación previa dentro de la función de registro. Antes de añadir un nuevo elemento, el sistema normaliza el texto ingresado (convirtiéndolo a minúsculas y eliminando espacios vacíos) y lo compara con los elementos existentes mediante una función de búsqueda; si el producto ya se encuentra registrado, el programa bloquea el nuevo ingreso, le notifica al usuario que el artículo ya existe y le sugiere utilizar la opción de modificar cantidad en lugar de duplicar la información.
