# Dynamic SAS
![CI](https://github.com/camilogamboa2024/dymanic-sas/actions/workflows/ci.yml/badge.svg)

Dynamic SAS es una aplicación web desarrollada en Django para facilitar la gestión integral de un pequeño o mediano negocio. Sus principales características son:

Inventario
‣ CRUD de productos y categorías
‣ Registro de movimientos de stock (entradas, salidas, ajustes)
‣ Alertas de stock bajo y gestión de niveles mínimos

Ventas
‣ Administración de clientes y facturas
‣ Líneas de venta con validación de stock
‣ Resumen y detalle de ventas

Reportes
‣ Ranking de top‐productos por volumen de ventas en un rango de fechas
‣ Cálculo de rotación de inventario (días de cobertura)
‣ Formularios de filtro por fecha y tablas exportables

Autenticación y permisos
‣ Inicio/cierre de sesión
‣ Control de acceso por grupos y permisos a vistas y acciones

Calidad y despliegue
‣ Tests automatizados con pytest y cobertura ≥ 90%
‣ CI configurada con GitHub Actions (tests, migraciones, cobertura)
‣ Preparada para incorporación de CD (Heroku, AWS, etc.)

Tecnologías clave:
Django, PostgreSQL, pytest, GitHub Actions y, opcionalmente, Tailwind o Bootstrap en el front-end.

Con esta herramienta podrás llevar un control fiable de tu stock, facturación y análisis de ventas, todo en un único panel web.
