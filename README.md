# Análisis Automatizado de Facturas con IA y Dashboard en Power BI

## Descripción

Este proyecto es una solución analítica de extremo a extremo diseñada para automatizar la gestión y el análisis de facturas de gastos, independientemente de su formato o proveedor. El proyecto utiliza **Inteligencia Artificial** para extraer datos de documentos no estructurados y transformarlos en información accionable visualizada en un cuadro de mando profesional.

# Descripción del Proyecto
El flujo de trabajo del proyecto resuelve el problema del procesamiento manual de facturas, las cuales suelen tener estructuras muy diferentes entre proveedores. La solución realiza las siguientes tareas:

- **Carga automática** de facturas en formato PDF desde la carpeta definida.
- **Extracción de texto** bruto mediante librerías especializadas de Python.
- **Estructuración de datos con IA** (OpenAI), extrayendo campos clave como fecha, proveedor, concepto, importe y moneda.
- **Procesamiento de datos**, incluyendo la conversión de divisas (ej. de dólares a pesos) para homogeneizar la información.
- **Almacenamiento** en una base de datos estructurada para su consulta y seguimiento histórico.
- **Visualización interactiva** en un dashboard de Power BI.

# Tecnologías Utilizadas

- **Python**: Lenguaje principal para la automatización y procesamiento.
- **OpenAI (GPT-4o mini)**: Modelo de IA utilizado para el análisis y extracción de datos estructurados.
- **SQLite**: Base de datos ligera para almacenar la información procesada.
- **Power BI**: Herramienta de Business Intelligence para la creación del cuadro de mando.
- **Librerías de Python**: Pandas (gestión de datos), sql-alchemy (conexión a BD), PyMuPDF (extracción de texto de PDFs) y python-dotenv (gestión de claves de API).

# Estructura de Archivos

- **facturas/**: Carpeta donde se depositan los archivos PDF a procesar, organizada por subcarpetas (ej. por meses).
- **Power BI/**: Contiene el archivo .pbix del dashboard y recursos gráficos.
- **main.py**: Script principal que coordina el flujo de ejecución.
- **funciones.py**: Contiene la lógica auxiliar para extraer texto, llamar a la API de IA y convertir datos a formato tabular.
- **prompts.py**: Incluye las instrucciones detalladas enviadas al modelo de IA para asegurar una extracción precisa.
- **.env**: Archivo para configurar la clave de API de OpenAI de forma segura.
- **environment.yml**: Configuración para replicar el entorno de desarrollo con todas las dependencias necesarias.

# Dashboard de Power BI
El cuadro de mando ofrece una visión global de los gastos mediante:

- **KPIs principales**: Gasto total, número de facturas, gasto medio y número de proveedores.
- **Segmentadores**: Filtros por mes para análisis temporales específicos.
- **Gráfico de Tendencia**: Evolución mensual de los gastos (no afectado por filtros de mes para mantener el contexto).
- **Tabla de Gastos Críticos**: Visualización de las 7 facturas de mayor importe mediante un filtro "Top N".
- **Treemap de Partidas**: Comparativa visual del peso relativo de cada proveedor o gasto sobre el total.

# Configuración e Instalación

- **Entorno**: Permite crear el entorno virtual utilizando el archivo environment.yml.
- **API Key**: Introducir la clave de OpenAI en el archivo .env.
- **Documentos**: Colocar las facturas PDF en la carpeta correspondiente.
- **Ejecución**: Correr main.py para generar la base de datos facturas.db.
- **Visualización**: Abrir el archivo de Power BI y configurar la conexión ODBC hacia la base de datos SQLite generada.

# Posibles Mejoras

- **Modelos Locales**: Implementar LLMs locales para reducir costes y aumentar la privacidad de los datos financieros.
- **Modelos de Visión**: Integrar IA visual para procesar facturas físicas o tickets no digitalizados.
- **Fine-tuning**: Entrenar el modelo con facturas específicas de la empresa para maximizar la precisión.
- **Integración ERP**: Conectar con sistemas contables para cruzar gastos con ingresos y generar estados de resultados
