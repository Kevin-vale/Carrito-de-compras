# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:51:17 2026

@author: leone
"""
#Mostrar opciones disponibles con el uso del while true

while True:
    print("-MENÚ PRINCIPAL-")
    print("1 ==> Ver catálogo")
    print("2 ==> Agregar producto")
    print("3 ==> Eliminar producto")
    print("4 ==> Ver carrito")
    print("5 ==> Generar ticket")
    print("6 ==> Salir")

    opcion = input("Selecciona una opción del 1 al 6: ").strip()

    if opcion == "1":
        print("mostrar catalogo")
    elif opcion == "2":
        print("agregar producto")
    elif opcion == "3":
        print("eliminar producto")
    elif opcion == "4":
        print("calcular subtotal")
    elif opcion == "5":
        print("generar ticket")
    elif opcion == "6":
        print("Gracias por su compra, No regrese")
        break  # rompe el while True y finaliza
    else:
        print("Error == Escoja un numero valido PORVAFOR >:c")