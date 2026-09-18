# descuento
REGLAS_DESCUENTO = {
    "NINGUNO": {"descripcion": "Sin descuento", "porcentaje": 0.0},
    "PROMO10": {"descripcion": "Descuento del 10%", "porcentaje": 0.10},
    "PROMO20": {"descripcion": "Descuento del 20%", "porcentaje": 0.20},
    "PROMO50": {"descripcion": "Descuento del 50%", "porcentaje": 0.50}
}


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

    # Normalizar la clave de descuento recibida
    clave = tipo_descuento.upper().strip()

    # Soporte si el usuario ingresa '10%', '20%', '50%'
    if clave in ["10%", "20%", "50%"]:
        clave = f"PROMO{clave.replace('%', '')}"

    if clave in REGLAS_DESCUENTO:
        porcentaje = REGLAS_DESCUENTO[clave]["porcentaje"]
        descuento = subtotal * porcentaje
        total = subtotal - descuento
    else:
        print(f"Aviso: Tipo de descuento '{tipo_descuento}' no válido. No se aplicará descuento.")
        total = subtotal

    return round(max(0.0, total), 2)