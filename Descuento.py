# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 21:45:39 2026

@author: reyes
"""

def calcular_subtotal(carrito, catalogo):
    subtotal = 0.0
    for id_prod, cantidad in carrito:
        precio = catalogo[id_prod]["Precio"]
        subtotal += precio * cantidad
    return subtotal


def aplicar_descuento(subtotal, tipo_descuento):
    
    if subtotal <= 0:
        return 0.0
    
    if tipo_descuento == "10%":
        total = subtotal * 0.90  # se aplica el 10%

    elif tipo_descuento == "20%":
        total = subtotal * 0.80  # se aplica el 20%

    elif tipo_descuento == "50%":
        total = subtotal * 0.50  # se aplica el 50%

    else:
        total = subtotal  

    if total < 0:
        total = 0.0

    return round(total, 2)


subtotal_calculado = calcular_subtotal(carrito, InvProd)
desc = input(" seleccione el descuento (10%, 20%, FIJO): ").strip()
print("Total a pagar:", aplicar_descuento(subtotal_calculado, desc))