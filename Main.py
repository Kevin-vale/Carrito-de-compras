# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 16:44:02 2026

@author: aguil
"""

from Productos import cargar_catalogo, mostrar_catalogo
from Carrito import agregar_producto, eliminar_producto
from Descuento import calcular_subtotal, aplicar_descuento, REGLAS_DESCUENTO
from ticket import generar_ticket
from Menu import el_menu


def ver_carrito(carrito, catalogo):
    """Muestra los elementos actuales dentro del carrito."""
    if not carrito:
        print("\nEl carrito de compras está vacío.")
        return 0.0

    print("\n========== CARRITO DE COMPRAS ==========")
    subtotal = calcular_subtotal(carrito, catalogo)
    for id_prod, cantidad in carrito:
        nombre = catalogo[id_prod]["nombre"]
        precio = catalogo[id_prod]["precio"]
        total_item = precio * cantidad
        print(f"- {nombre} ({id_prod}) | Cantidad: {cantidad} | P.Unit: ${precio:.2f} | Total: ${total_item:.2f}")
    print("----------------------------------------")
    print(f"Subtotal actual: ${subtotal:.2f}")
    print("========================================\n")
    return subtotal


def procesar_pago(carrito, catalogo, ventas_registradas):
    """Procesa el cobro, aplica descuentos si corresponden y genera el ticket."""
    if not carrito:
        print("\nEl carrito está vacío. Agregue productos antes de pagar.")
        return

    subtotal = calcular_subtotal(carrito, catalogo)
    print(f"\nSubtotal a pagar: ${subtotal:.2f}")
    
    print("\nOpciones de descuento disponibles:")
    for clave, info in REGLAS_DESCUENTO.items():
        print(f" - {clave}: {info['descripcion']}")
    
    tipo_desc = input("Ingrese el código de descuento (o presione Enter para omitir): ").strip()
    if not tipo_desc:
        tipo_desc = "NINGUNO"

    total_final = aplicar_descuento(subtotal, tipo_desc)
    
    # Generar ticket y obtener la tupla de registro de venta
    registro = generar_ticket(carrito, catalogo, total_final)
    ventas_registradas.append(registro)
    
    # Actualizar stock disponible en el catálogo
    for id_prod, cantidad in carrito:
        catalogo[id_prod]["stock"] -= cantidad

    # Limpiar carrito de compras
    carrito.clear()


def main():
    catalogo = cargar_catalogo()
    carrito = []
    ventas_registradas = []

    while True:
        # Llamada al módulo de menú
        opcion = el_menu()

        if opcion == 1:
            mostrar_catalogo(catalogo)

        elif opcion == 2:
            mostrar_catalogo(catalogo)
            id_prod = input("Ingrese el ID del producto a agregar: ").strip().upper()
            try:
                cantidad = int(input("Ingrese la cantidad deseada: "))
                carrito = agregar_producto(carrito, catalogo, id_prod, cantidad)
            except ValueError:
                print("Error: Debe ingresar una cantidad numérica entera.")

        elif opcion == 3:
            if not carrito:
                print("El carrito está vacío.")
            else:
                ver_carrito(carrito, catalogo)
                id_prod = input("Ingrese el ID del producto a eliminar: ").strip().upper()
                carrito = eliminar_producto(carrito, id_prod)

        elif opcion == 4:
            ver_carrito(carrito, catalogo)

        elif opcion == 5:
            procesar_pago(carrito, catalogo, ventas_registradas)

        elif opcion == 6:
            print("Gracias por usar el sistema de compras. ¡Hasta luego!")
            break


if __name__ == "__main__":
    main()