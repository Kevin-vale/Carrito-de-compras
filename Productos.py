# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:27:19 2026

@author: isra2
"""
InvProd = {
    "ID01": {"nombre": "CerealMaiz", "categoria": "Cereales", "stock": 20, "precio": 38.0},
    "ID02": {"nombre": "CafeSoluble", "categoria": "Cafe", "stock": 15, "precio": 50.0},
    "ID03": {"nombre": "PapelHigG", "categoria": "Higiene", "stock": 5, "precio": 46.0},
    "ID04": {"nombre": "PapelhigCH", "categoria": "Higiene", "stock": 10, "precio": 23.0},
    "ID05": {"nombre": "LataAtun", "categoria": "Enlatados", "stock": 8, "precio": 17.0},
    "ID06": {"nombre": "PanBlancoG", "categoria": "Pan", "stock": 2, "precio": 39.0},
    "ID07": {"nombre": "CerealChoco", "categoria": "Cereales", "stock": 6, "precio": 42.0},
    "ID09": {"nombre": "LataSalsa", "categoria": "Enlatados", "stock": 7, "precio": 40.0},
    "ID010": {"nombre": "Papas", "categoria": "Golosinas", "stock": 3, "precio": 14.0},
    "ID011": {"nombre": "Jabon", "categoria": "Higiene", "stock": 4, "precio": 24.0},
    "ID012": {"nombre": "PastaDental", "categoria": "Higiene", "stock": 15, "precio": 14.0},
    "ID013": {"nombre": "Aceite", "categoria": "Aceites", "stock": 5, "precio": 30.0},           
    "ID014": {"nombre": "VasosDes", "categoria": "Desechables", "stock": 4, "precio": 22.0},
    "ID015": {"nombre": "PlatoDes", "categoria": "Desechables", "stock": 3, "precio": 18.0},
    "ID016": {"nombre": "cartonLeche", "categoria": "Bebidas", "stock": 4, "precio": 16.0},
    "ID017": {"nombre": "LitroAgua", "categoria": "Bebidas", "stock": 7, "precio": 10.0},
    "ID018": {"nombre": "Cerillos", "categoria": "Miselaneos", "stock": 6, "precio": 12.0},
    "ID019": {"nombre": "shampo", "categoria": "Higiene", "stock": 2, "precio": 47.0},
    "ID020": {"nombre": "Jugo", "categoria": "Bebidas", "stock": 8, "precio": 24.0},
    "ID021": {"nombre": "Galonvinagre", "categoria": "Miselaneos", "stock": 1, "precio": 28.0},
    "ID022": {"nombre": "PanDulce", "categoria": "Pan", "stock": 1, "precio": 18.0},
    "ID023": {"nombre": "Cerveza", "categoria": "Bebidas", "stock": 3, "precio": 50.0},
}


def cargar_catalogo():
 
    return InvProd


def mostrar_catalogo(catalogo):

    print("\n========================= CATÁLOGO DE PRODUCTOS =========================")
    print(f"{'ID':<8} | {'Nombre':<15} | {'Categoría':<12} | {'Stock':<6} | {'Precio':<8}")
    print("-" * 65)
    for id_prod, prod in catalogo.items():
        print(f"{id_prod:<8} | {prod['nombre']:<15} | {prod['categoria']:<12} | {prod['stock']:<6} | ${prod['precio']:<.2f}")
    print("=========================================================================\n")


def agregar_producto_inventario(catalogo, id_prod, nombre, categoria, stock, precio):

    if id_prod in catalogo:
        print(f"Error: El producto con ID '{id_prod}' ya existe.")
    else:
        catalogo[id_prod] = {
            "nombre": nombre,
            "categoria": categoria,
            "stock": stock,
            "precio": float(precio)
        }
        print(f"Producto '{nombre}' agregado al catálogo correctamente.")


def eliminar_producto_inventario(catalogo, id_prod):

    if id_prod in catalogo:
        producto_borrado = catalogo.pop(id_prod)
        print(f"El producto '{producto_borrado['nombre']}' fue eliminado del catálogo.")
    else:
        print(f"Error: El producto con ID '{id_prod}' no existe en el catálogo.")