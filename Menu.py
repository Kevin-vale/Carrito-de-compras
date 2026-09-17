# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:51:17 2026

@author: leone
"""
def el_menu():
    while True:
        print("-MENÚ PRINCIPAL-")
        print("1 ==> Ver catálogo")
        print("2 ==> Agregar producto")
        print("3 ==> Eliminar producto")
        print("4 ==> Ver carrito")
        print("5 ==> Generar ticket")
        print("6 ==> Salir")

        try:
            opcion = int(input("Selecciona una opción del 1 al 6: "))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        if 1 <= opcion <= 6:
            return opcion
        else:
            print("Opción fuera de rango, intenta de nuevo.")


if __name__ == "__main__":
    while True:
        eleccion = el_menu()
        if eleccion == 6:
            print("Proceso terminado, No regrese :)")
            break
        elif eleccion <= 5:
            print(eleccion)
            print("algo")