# VentAPP POS


# 🧾 POS Multiplataforma - Sistema de Punto de Venta

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Version](https://img.shields.io/badge/version-0.0.1-blue)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

POS Multiplataforma es una solución de punto de venta (TPV) totalmente funcional, moderna y multiplataforma, ideal para tiendas, supermercados y pequeños negocios que buscan una herramienta intuitiva y eficiente para gestionar sus ventas, productos y clientes desde cualquier sistema operativo.

Version en fase alfa...cargando mejoras...proximamente lo lanzamos para el público general.

---

### ✨ Características destacadas

- ✅ Interfaz limpia y amigable estilo macOS / Material Design.
- 🧃 Gestión completa de productos con categorías, IVA y control de stock.
- 🧑‍🤝‍🧑 Administración de clientes con historial de compras.
- 🧾 Módulo TPV (Terminal Punto de Venta) con escaneo rápido tipo "supermercado".
- 🖨️ Preparado para impresión de tickets y facturación electrónica.
- 💾 Guardado automático en base de datos SQLite (con posibilidad de escalar a PostgreSQL).
- ☁️ Compatible con sincronización en la nube (próximamente).
- 🌐 Disponible para Windows, macOS y Linux.

---

### 🖼️ Capturas de pantalla

> *Simulaciones iniciales, no finales. Pendiente actualizar capturas con nuevas funcionalidades*

**Pantalla principal del TPV:**

![TPV Screenshot](http://imgfz.com/i/d9so1ql.png)

**Gestión de productos:**

![Productos Screenshot](http://imgfz.com/i/ryzWHib.png)

---
```bash
tpv_app/
├── app.py                        # Punto de entrada principal (arranca la app Flet)
├── config/
│   ├── __init__.py
│   ├── settings.py               # Configuraciones globales (idioma, base de datos, entorno)
│   └── constants.py              # Constantes reutilizables (estilos, colores, rutas)
├── core/
│   ├── __init__.py
│   ├── database.py               # Inicialización SQLite u otro motor
│   ├── exceptions.py             # Manejo de errores personalizados
│   └── utils.py                  # Funciones reutilizables (formato moneda, validaciones)
├── domain/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── producto.py           # DTO Producto
│   │   ├── categoria.py
│   │   ├── cliente.py
│   │   └── venta.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── producto_repo.py
│   │   ├── categoria_repo.py
│   │   └── venta_repo.py
│   └── services/
│       ├── __init__.py
│       ├── venta_service.py      # Lógica como registrar venta, totalizar, aplicar descuentos
│       └── stock_service.py
├── ui/
│   ├── __init__.py
│   ├── main_view.py              # Ventana principal con menú lateral y navegación
│   ├── views/
│   │   ├── __init__.py
│   │   ├── producto_view.py
│   │   ├── cliente_view.py
│   │   ├── venta_view.py
│   │   ├── dashboard_view.py
│   │   └── ajustes_view.py
│   └── components/
│       ├── __init__.py
│       ├── botones.py            # Botones reutilizables
│       ├── tablas.py             # Tablas reutilizables con estilos
│       └── formularios.py
├── localization/
│   ├── es.py                     # Traducciones en español
│   ├── en.py                     # Traducciones en inglés
│   └── i18n.py                   # Manejador de idiomas
├── assets/
│   ├── images/                   # Logos, íconos
│   ├── fonts/                    # Tipografías personalizadas
│   └── themes/                   # Archivos JSON o Python con estilos de UI
├── tests/
│   ├── __init__.py
│   ├── test_productos.py
│   ├── test_ventas.py
│   └── test_integration.py
├── requirements.txt              # Dependencias del proyecto
└── README.md                     # Documentación principal
```
---

### 🚀 Instalación rápida

```bash
git clone https://github.com/brianterrazas/ventapp-pos.git
cd proyecto_tienda_POS
pip install -r requirements.txt
python main.py
```
✍️  Autor:

🙋🏽‍♀️  Brian Terrazas Sullcani
💻  Desarrollador senior en java y python, enfocado en crear soluciones sencillas para problemas complejos.
📧  ---
🔗  LinkedIn (Brian Armando Terrazas Sullcani)

📄  Licencia:

Este proyecto está licenciado bajo los términos de la [Licencia Creative Commons Atribución-NoComercial 4.0 Internacional (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).
Puedes usar, modificar y compartir el código libremente, siempre que no lo utilices con fines comerciales y des atribución al autor original.

❤️  ¿Te fue útil?
Déjame una estrella en el repo y así ayudarás a más gente a conocerlo!!