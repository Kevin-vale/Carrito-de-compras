# Práctica: 🛒 Simulador de Carrito de Compras en Python
Este proyecto es un simulador funcional de un sistema de punto de venta desarrollado en Python, diseñado para ejecutarse a través de la consola. 
El sistema permite la gestión de un catálogo de productos, el control de un carrito de compras, la aplicación de descuentos y la generación de un ticket final con un registro inmutable de la venta.

## 👥 Integrantes y Roles del Equipo

*   **Leonel Abad Romero Vázquez** — Encargado del Menú y Flujo Principal (Estructura lógica `while True` e interacción con el usuario).
*   **Israel Esaú Luna Nicanor** — Encargado de Catálogo (Definición y mantenimiento del diccionario de productos).
*   **Kevin Valentino León Aguilar** — Encargado de Carrito (Funciones para agregar y eliminar productos del carrito).
*   **Francisco Javier Reyes Contreras** — Encargado de Totales y Descuentos (Cálculo de subtotales, reducción por cupones y netos).
*   **María Fernanda Ramírez Flores** — Integración de módulos, generación de la tupla inmutable del ticket, formato visual del recibo impreso y administración del repositorio de Git.

---

## 📊 Especificación de Estructuras de Datos

Para cumplir con los requerimientos estrictos del proyecto, el sistema se basa en el flujo de las siguientes estructuras:

1.  **Catálogo (Estructura Mutable):** Un diccionario de diccionarios donde la clave es el ID del producto y el valor contiene su información general:
    ```python
    catalogo = {
        "id_producto": {"nombre": "Nombre", "precio": 0.0, "stock": 0}
    }
    ```
2.  **Carrito de Compras:** Una lista dinámica de tuplas que almacena los artículos seleccionados por el cliente y sus cantidades:
    ```python
    carrito = [("id_producto", cantidad)]
    ```
3.  **Registro de Venta (Estructura Inmutable):** Una tupla estricta generada al finalizar la compra para el control de la bitácora:
    ```python
    registro_venta = ("Folio", "Fecha AAAA-MM-DD", total_final)
    ```

---

## 🛠️ Bitácora de Administración de Git y Resolución de Conflictos

Durante el desarrollo colaborativo del proyecto en GitHub, se presentaron y resolvieron de forma manual los siguientes eventos en el control de versiones:

### 1. Resolución de Conflicto de Merge en Módulo de Carrito
*   **Problema detectado:** Al intentar unificar las funciones de la rama del carrito de compras con la estructura base de la rama principal (`main`), Git generó un conflicto de marcas debido a contribuciones simultáneas en el archivo, resultando en líneas de control de superposición:
    ```text
    <<<<<<< HEAD
    # Código en desarrollo
    =======
    # Código entrante de la rama remota
    >>>>>>> aa5553223cbccc6bfed...
    ```
*   **Solución manual aplicada:** Como integrador, se procedió a abrir el archivo afectado directamente en el entorno de desarrollo. Se eliminaron manualmente todas las etiquetas de conflicto de Git (`<<<<<<<`, `=======`, `>>>>>>>`) y se reestructuraron las funciones `agregar_producto` y `eliminar_producto` para asegurar que operaran de forma independiente y respetaran la indentación de 4 espacios requerida por Python.

### 2. Integración de Módulos
*   Se realizó la vinculación del flujo del menú principal (`Menu.py`) con la función de salida `generar_ticket` alojada en `ticket.py`.
*   Se aseguró que al seleccionar la opción **5 (Generar ticket)**, el sistema recupere el estado actual de la lista de tuplas y añada la tupla inmutable de retorno al historial global de ventas de la tienda.
