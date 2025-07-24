#  Backend Proyecto Dymanic SAS

Este es el backend del sistema de inventario y ventas desarrollado con Django.

##  Requisitos

- Python 3.11
- PostgreSQL (o SQLite en entorno local)
- Django 4.2.23

---

## instalacion local

1. Clona el repositorio:

```bash
git clone https://github.com/camilogamboa2024/dymanic-sas.git
cd dymanic-sas


Estructura del proyecto
inventario/ – Gestión de productos.

ventas/ – Gestión de ventas, facturas y resúmenes.

reportes/ – Visualización de productos más vendidos, rotación, etc.

templates/ – HTMLs básicos para probar el funcionamiento.

services.py – Lógica de negocio separada para mayor mantenibilidad.

