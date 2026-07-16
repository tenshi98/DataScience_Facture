# PowerBI Facturas
1. Power Query (M) — Transformación de datos
-En Power BI Desktop: Inicio → Transformar datos → Editor avanzado, pega el contenido de Power Query
-Recomendación: crea también una tabla de Calendario separada
-Luego, en el modelo de datos, relaciona Calendario[Fecha] con datos_facturas[fecha_factura] (1 a muchos).

2. Medidas DAX — KPIs del dashboard ejecutivo

3. Estructura sugerida del dashboard ejecutivo

-Fila superior (tarjetas KPI): Total Facturado, Cantidad de Facturas, Ticket Promedio, Variación % vs mes anterior
-Gráfico de líneas/área: Total Facturado por mes (usando Calendario[NombreMes])
-Gráfico de barras horizontales: Top proveedores por monto
-Gráfico de dona/pastel: Distribución por concepto de gasto
-Tabla o matriz: Detalle de facturas con filtros de fecha, proveedor y concepto
-Segmentadores (slicers): Año, Trimestre, Proveedor
