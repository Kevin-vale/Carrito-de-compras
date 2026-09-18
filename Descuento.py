

def calcular_subtotal(carrito, catalogo):

    subtotal = 0.0
    for id_prod, cantidad in carrito:
        if id_prod in catalogo:
            precio = catalogo[id_prod]["precio"]
            subtotal += precio * cantidad
    return round(subtotal, 2)


def aplicar_descuento(subtotal, tipo_descuento):

    if subtotal <= 0:
        return 0.0

    if tipo_descuento == "10%":
        total = subtotal * 0.90 # se aplica el 10%
    elif tipo_descuento == "20%":
        total = subtotal * 0.80 # se aplica el 20 %
    elif tipo_descuento == "50%":
        total = subtotal * 0.50 # se aplica el 50%
    else:
        total = subtotal

    if total < 0:
        total = 0.0

    return round(total, 2)
