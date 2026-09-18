## 🛒 Simulador de Carrito de Compras

Este proyecto es un sistema de punto de venta desarrollado en Python que se ejecuta a través de la consola. Permite gestionar un catálogo de productos, controlar un carrito de compras, aplicar descuentos y generar un ticket final con un registro inmutable de la venta.

---

## 👥 Integrantes y Roles

*   Leonel Abad Romero Vázquez — Encargado del Menú y Flujo Principal (Estructura lógica `while True` e interfaz de usuario).
*   Israel Esaú Luna Nicanor — Encargado de Catálogo (Definición y mantenimiento del diccionario de productos).
*   Kevin Valentino León Aguilar — Encargado de Carrito (Funciones para agregar y eliminar productos del carrito).
*   Francisco Javier Reyes Contreras — Encargado de Totales y Descuentos (Cálculo de subtotales, reducción por cupones y netos).
*   María Fernanda Ramírez Flores — Integración de módulos, generación de la tupla inmutable del ticket, formato visual del recibo impreso y administración del repositorio de Git.

---

## 📊 Estructuras de Datos del Proyecto

El sistema se basa en el flujo de las siguientes estructuras requeridas:

1.  **Catálogo:** Un diccionario de diccionarios donde la clave es el ID del producto y contiene la información general:
    ```python
    InvProd = {
        "id_producto": {"nombre": "Nombre", "Precio": 0.0, "stock": 0}
    }
    ```
2.  **Carrito de Compras:** Una lista dinámica de tuplas que almacena los artículos y sus cantidades:
    ```python
    carrito_compras = [("id_producto", cantidad)]
    ```
3.  **Registro de Venta:** Una tupla inmutable generada al finalizar la compra para el control de la bitácora:
    ```python
    registro_venta = ("Folio", "Fecha AAAA-MM-DD", total_final)
    ```

---

## 📁 Arquitectura Final del Repositorio (Módulos Integrados)

El proyecto quedó estructurado de forma modular y limpia con los siguientes archivos finales en la rama principal:

*   **`Main.py`** (Cerebro del programa) — Inicializa el sistema, importa todos los módulos y arranca la ejecución general con todo listo.
*   **`Menu.py`** (Leo) — Contiene la lógica del menú interactivo en consola y el control de flujos mediante el ciclo `while True`.
*   **`Productos.py`** (Isra) — Define el diccionario base con el catálogo nuevo de productos, precios y stocks disponibles.
*   **`Carrito.py`** (Kevin) — Resguarda las funciones optimizadas para añadir productos, validar stock disponible y remover elementos del carrito.
*   **`Descuento.py`** (Paco) — Realiza las operaciones matemáticas del subtotal y la aplicación de los distintos porcentajes de descuento.
*   **`ticket.py`** (Fer) — Procesa la lista de tuplas final, despliega el recibo alineado visualmente en columnas y genera el retorno inmutable.
*   **`.spyproject/config`** — Archivos de configuración locales del entorno de desarrollo Spyder del equipo.

---

## 🛠️ Bitácora de Git y Resolución de Conflictos

Durante el desarrollo colaborativo del proyecto en GitHub, se presentaron y resolvieron los siguientes eventos en el repositorio:

### 1. Resolución Manual de Conflicto de Merge (Módulo de Carrito)
*   **Problema:** Al intentar unificar las funciones de la rama del carrito de compras con la rama principal (`main`), Git generó un conflicto de marcas debido a modificaciones simultáneas en las mismas líneas, resultando en etiquetas de superposición (`<<<<<<< HEAD`, `=======`, `>>>>>>>`).
*   **Solución:** Como integrador, abrí el archivo en el editor, eliminé manualmente las etiquetas de control de Git y reestructuré las funciones `agregar_producto` y `eliminar_producto` para asegurar que operaran de forma independiente y respetaran la sangría (indentación) de 4 espacios requerida por Python (norma PEP 8).

### 2. Integración y Homologación de Variables
*   Se unificaron los módulos de los integrantes solucionando discrepancias en los nombres de las variables clave. Se adaptó el módulo de ticket para que use la clave `"Precio"` (con mayúscula inicial) tal como fue definida en las funciones de cálculo de descuentos de Paco, y `"nombre"` para empatar con la estructura del catálogo.
*   Se vinculó el menú principal con la función `generar_ticket` para que al elegir la opción **5**, se recupere la lista de tuplas del carrito, se apliquen las operaciones aritméticas y se guarde la tupla de venta en el historial global del sistema.

---
