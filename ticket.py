# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 18:13:26 2026

@author: mafer
"""


from datetime import datetime
import random

def generar_ticket(carrito, catalogo, total):
    folio = f"F{random.randint(1000, 9999)}"
    fecha_completa = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("\n==========================================")
    print(f"         TICKET DE COMPRA ({folio})       ")
    print(f" Fecha: {fecha_completa}")
    print("==========================================")
    
    print(f"{'Producto':<18} {'Cant.':<6} {'Total':<10}")
    print("----------------------------------------")
    
    # Calculamos el subtotal acumulado para saber si hubo descuento
    subtotal_base = 0.0
    for id_prod, cantidad in carrito:
        nombre = catalogo[id_prod]["nombre"]
        precio = catalogo[id_prod]["Precio"]
        subtotal_prod = precio * cantidad
        subtotal_base += subtotal_prod
        print(f"{nombre:<18} {cantidad:<6} ${subtotal_prod:<10.2f}")
        
    print("----------------------------------------")
    print(f" Subtotal:                      ${subtotal_base:.2f}")
    
    # Si el total final es menor al subtotal, calculamos la diferencia
    if total < subtotal_base:
        descuento_ahorrado = subtotal_base - total
        print(f" Descuento aplicado:           -${descuento_ahorrado:.2f}")
        
    print("=========================================")
    print(f" TOTAL A PAGAR:                 ${total:.2f}")
    print("=========================================")
    print("      Gracias por su compra.            \n")
    
    fecha_registro = datetime.now().strftime("%Y-%m-%d")
    registro_venta = (folio, fecha_registro, total)
    return registro_venta
