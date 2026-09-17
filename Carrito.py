
# Simulador de carrito 

def agregar_producto(carrito, catalogo, id_prod, cantidad):
    if id_prod not in catalogo:
        print("Error: El producto no existe en el catálogo.")
        return carrito

    if cantidad <= 0:
        print("Error: La cantidad a agregar debe ser mayor a 0.")
        return carrito

    stock_disponible = catalogo[id_prod]["stock"]

    # Verificar si el producto ya está presente en el carrito
    for i in range(len(carrito)):
        item_id, item_cantidad = carrito[i]
        if item_id == id_prod:
            nueva_cantidad = item_cantidad + cantidad
            if nueva_cantidad > stock_disponible:
                print(f"Error: No hay suficiente stock. Disponibles: {stock_disponible}, en carrito: {item_cantidad}.")
                return carrito
            
            carrito[i] = (id_prod, nueva_cantidad)
            print(f"Cantidad del producto '{catalogo[id_prod]['nombre']}' actualizada a {nueva_cantidad}.")
            return carrito

    # Si el producto no estaba en el carrito
    if cantidad > stock_disponible:
        print(f"Error: No hay suficiente stock. Stock disponible: {stock_disponible}")
        return carrito

    carrito.append((id_prod, cantidad))
    print(f"Producto '{catalogo[id_prod]['nombre']}' agregado al carrito correctamente.")
    return carrito


def eliminar_producto(carrito, id_prod):

    for i in range(len(carrito)):
        if carrito[i][0] == id_prod:
            carrito.pop(i)
            print(f"Producto '{id_prod}' eliminado del carrito.")
            return carrito

    print(f"El producto '{id_prod}' no se encuentra en el carrito.")
    return carrito