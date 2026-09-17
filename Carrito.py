

<<<<<<< HEAD
# Simulador de carrito 


def agregar_producto(carrito, catalogo, id_prod, cantidad):
    
    if id_prod not in catalogo:
        print("El producto no existe")
        return carrito
    
    if cantidad <= 0:
        print("La cantidad debe ser mayor a 0")
        return carrito
    
    stock = catalogo[id_prod]["stock"]
    
    if cantidad > stock:
        print("No hay suficiente stock")
        print("stock disponibles:", stock)
        return carrito 
    
    for i in range(len(carrito)):
        
        if carrito[i][0] == id_prod:
            
            cantidad_actual = carrito[i][1]
            nueva_cantidad = cantidad_actual + cantidad
            
            if nueva_cantidad > stock:
                print("No hay suficiente stock para agregar esa cantidad") 
                return carrito
            
            carrito[i] = (id_prod, nueva_cantidad)
            
            print("producto actualizado")
            return carrito

            carrito.append((id_prod, cantidad))

            print("Producto agregado correctamente")
            return carrito 
        
        def eliminar_producto(carrito, id_prod):
            
            for i in range(len(carrito)):
                
                if carrito[i][0] == id_prod:
                    
                    carrito.pop(i)
                    
                    print("Producto eliminado")
                    return carrito
=======    
  
>>>>>>> aa5553223cbccc6bfed40d05993517d12ce9fa0d
