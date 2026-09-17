# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:27:19 2026

@author: isra2
"""
#diccionario con los productos disponibles en la tienda
InvProd = {"ID01": {"NomProd": "CerealMaiz", "Categoria": "Cereales", "Cantidad": 20, "Precio": 38},
           "ID02": {"NomProd": "CafeSoluble", "Categoria": "Cafe", "Cantidad": 15, "Precio": 50},
           "ID03": {"NomProd": "PapelHigG", "Categoria": "Higiene", "Cantidad": 5, "Precio": 46},
           "ID04": {"NomProd": "PapelhigCH", "Categoria": "Higiene", "Cantidad": 10, "Precio": 23},
           "ID05": {"NomProd": "LataAtun", "Categoria": "Enlatados", "Cantidad": 8, "Precio": 17},
           "ID06": {"NomProd": "PanBlancoG", "Categoria": "Pan", "Cantidad": 2, "Precio": 39},
           "ID07": {"NomProd": "CerealChoco", "Categoria": "Cereales", "Cantidad": 6, "Precio": 42},
           "ID09": {"NomProd": "LataSalsa", "Categoria": "Enlatados", "Cantidad": 7, "Precio": 40},
           "ID010": {"NomProd": "Papas", "Categoria": "Golosinas", "Cantidad": 3, "Precio": 14},
           "ID011": {"NomProd": "Jabon", "Categoria": "Higiene", "Cantidad": 4, "Precio": 24},
           "ID012": {"NomProd": "PastaDental", "Categoria": "Higiene", "Cantidad": 15, "Precio": 14},
           "ID013": {"NomProd": "Aceite", "Categoria": "Aceites", "Cantidad": 5, "Precio": 30},           
           "ID014": {"NomProd": "VasosDes", "Categoria": "Desechables", "Cantidad": 4, "Precio": 22},
           "ID015": {"NomProd": "PlatoDes", "Categoria": "Desechable", "Cantidad": 3, "Precio": 18},
           "ID016": {"NomProd": "cartonLeche", "Categoria": "Bebidas", "Cantidad": 4, "Precio": 16},
           "ID017": {"NomProd": "LitroAgua", "Categoria": "Bebidas", "Cantidad": 7, "Precio": 10},
           "ID018": {"NomProd": "Cerillos", "Categoria": "Miselaneos", "Cantidad": 6, "Precio": "12"},
           "ID019": {"NomProd": "shampo", "Categoria": "Higiene", "Cantidad": 2, "Precio": 47},
           "ID020": {"NomProd": "Jugo", "Categoria": "Bebidas", "Cantidad": 8, "Precio": 24},
           "ID021": {"NomProd": "Galonvinagre", "Categoria": "Miselaneos", "Cantidad": 1, "Precio": 28},
           "ID022": {"NomProd": "PanDulce", "Categoria": "Pan", "Cantidad": 1, "Precio": 18},
           "ID023": {"NomProd": "Cerveza", "Categoria": "Bebidas", "Cantidad": 3, "Precio": 50},
           }

#para agregar un producgto
def agregar_producto(Productos, id_producto, Nombre, Categoria, Cantidad, Precio):
    "Agregar producto al inventario"
    if id_producto in Productos:
        print (f"el {id_producto} ya esta  ")
    else: Productos[id_producto] = {"NomPrdo": Nombre, "Categoria": Categoria, "Cantidad": Cantidad, "Precio": Precio}
    print (f"Producto '{Nombre}' agregado")
    
#para eliminar un producto
def eliminar_producto(Productos, id_producto):
    if id_producto in Productos:
        Producto_borrado = Productos[id_producto]["NomProd"]
        Productos.pop(id_producto)
        print (f"el {Producto_borrado} fue borrado")
    else: 
        print (f"Producto '{id_producto}' no esta")