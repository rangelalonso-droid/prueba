# Importamos la clase del archivo "producto"
from producto import Producto

print("---SISTEMA DE INVENTARIO---\n")

# Instanciación de objetos
producto1 = Producto(3357, "Bujia NGK cobre", 47.50, 20)
producto2 = Producto(8765, "Bujia NGK platino", 99.20, 24)
producto3 = Producto(9817, "Bujia BOSCH platino", 134.99, 16)
producto4 = Producto(6789, "Bujia BOSCH cobre", 58.00, 20)

# Diccionario para facilitar la selección del inventario
inventario = {
    "1": producto1,
    "2": producto2,
    "3": producto3,
    "4": producto4
}

# Menú interactivo usando while
while True:
    print("\n==================================")
    print("MENÚ")
    print("==================================")
    print("A. Ver cantidad en stock")
    print("B. Registrar venta")
    print("C. Surtir inventario")
    print("D. Salir del menú")
    
    opcion = input("Seleccione una opción: ").upper() # .upper() ayuda si el usuario escribe en minúscula
    
    if opcion == "A":
        print("\n---Estado actual del inventario---")
        print(producto1.obtener_detalles())
        print(producto2.obtener_detalles())
        print(producto3.obtener_detalles())
        print(producto4.obtener_detalles())
        
    elif opcion == "B":
        print("\n---Registrar Venta---")
        print(f"1. {producto1.nombre}")
        print(f"2. {producto2.nombre}")
        print(f"3. {producto3.nombre}")
        print(f"4. {producto4.nombre}")
        prod_opcion = input("Seleccione el producto a vender: ")
        
        if prod_opcion in inventario:
            try:
                cantidad = int(input("Cantidad a vender: "))
                inventario[prod_opcion].vender(cantidad)
            except ValueError:
                print("ERROR: Ingrese un valor válido.")
        else:
            print("Opción de producto no válida.")
            
    elif opcion == "C":
        print("\n---Agregar al Inventario---")
        print(f"1. {producto1.nombre}")
        print(f"2. {producto2.nombre}")
        print(f"3. {producto3.nombre}")
        print(f"4. {producto4.nombre}")
        prod_opcion = input("Seleccione producto a surtir: ")
        
        if prod_opcion in inventario:
            try:
                cantidad = int(input("Cantidad a surtir: "))
                inventario[prod_opcion].surtir(cantidad)
            except ValueError:
                print("ERROR: Por favor ingrese un valor válido.")
        else:
            print("Opción de producto no válida.")
            
    elif opcion == "D":
        print("\n--- ¡Hasta Luego! ---")
        break 
        
    else:
        print("Opción inválida: Por favor ingrese alguna letra de la A-D.")
