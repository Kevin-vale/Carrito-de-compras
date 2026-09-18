# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 16:44:02 2026

@author: aguil
"""

from Productos import cargar_catalogo, mostrar_catalogo
from Carrito import agregar_producto, eliminar_producto

def calcular_subtotal(carrito, catalogo):
    """Calcula la suma total de los productos en el carrito."""
    subtotal = 0.0
    for id_prod, cantidad in carrito:
        subtotal += catalogo[id_prod]["precio"] * cantidad
    return subtotal

def ver_carrito(carrito, catalogo):
    """Muestra los elementos actuales dentro del carrito."""
    if not carrito:
        print("\nEl carrito de compras está vacío.")
        return

    print("\n========== CARRITO DE COMPRAS ==========")
    subtotal = 0.0
    for id_prod, cantidad in carrito:
        nombre = catalogo[id_prod]["nombre"]
        precio = catalogo[id_prod]["precio"]
        total_item = precio * cantidad
        subtotal += total_item
        print(f"- {nombre} ({id_prod}) | Cantidad: {cantidad} | P.Unit: ${precio:.2f} | Total: ${total_item:.2f}")
    print(f"----------------------------------------")
    print(f"Subtotal actual: ${subtotal:.2f}")
    print("========================================\n")

def main():
    catalogo = cargar_catalogo()
    carrito = []

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Mostrar catálogo de productos")
        print("2. Agregar producto al carrito")
        print("3. Eliminar producto del carrito")
        print("4. Ver contenido del carrito")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_catalogo(catalogo)

        elif opcion == "2":
            mostrar_catalogo(catalogo)
            id_prod = input("Ingrese el ID del producto a agregar: ").strip()
            try:
                cantidad = int(input("Ingrese la cantidad deseada: "))
                carrito = agregar_producto(carrito, catalogo, id_prod, cantidad)
            except ValueError:
                print("Error: Debe ingresar una cantidad numérica entera.")

        elif opcion == "3":
            if not carrito:
                print("El carrito está vacío.")
            else:
                ver_carrito(carrito, catalogo)
                id_prod = input("Ingrese el ID del producto que desea eliminar: ").strip()
                carrito = eliminar_producto(carrito, id_prod)

        elif opcion == "4":
            ver_carrito(carrito, catalogo)

        elif opcion == "5":
            print("Gracias por usar el sistema de compras. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()