"""
Procesa un conjunto de facturas almacenadas en archivos PDF y registra la
información extraída en una base de datos SQLite.

El flujo de ejecución es el siguiente:
1. Recorre todas las carpetas contenidas en el directorio "facturas".
2. Procesa cada archivo PDF encontrado.
3. Extrae el texto del documento.
4. Solicita la estructuración del contenido mediante OpenAI.
5. Convierte la respuesta obtenida a un DataFrame de pandas.
6. Consolida la información de todas las facturas procesadas.
7. Convierte los importes expresados en dólares a euros.
8. Conserva únicamente las columnas requeridas.
9. Guarda la información en la tabla "facturas" de una base de datos SQLite.

Dependencias:
- funciones
- pandas
- sqlalchemy
- os

Salida:
- Base de datos SQLite: facturas.db
- Tabla: facturas
"""

import funciones
import pandas as pd
import os
from sqlalchemy import create_engine

# Crear un DataFrame vacío que almacenará la información consolidada
# de todas las facturas procesadas.
df = pd.DataFrame()

# Recorre todas las carpetas ubicadas dentro del directorio "facturas".
for carpeta in sorted(os.listdir("./facturas")):
    ruta_carpeta = os.path.join("./facturas/", carpeta)

    # Recorre todos los archivos contenidos en la carpeta actual.
    for archivo in os.listdir(ruta_carpeta):
        ruta_pdf = os.path.join(ruta_carpeta, archivo)

        # Informa el archivo que está siendo procesado.
        print(f"📄 Procesando factura: {ruta_pdf}")

        # Extrae el contenido textual completo del archivo PDF.
        texto_no_estructurado = funciones.extraer_texto_pdf(ruta_pdf)

        # Envía el texto para obtener una representación estructurada en formato CSV.
        texto_estructurado = funciones.estructurar_texto(texto_no_estructurado)

        # Convierte el CSV recibido a un DataFrame.
        df_factura = funciones.csv_a_dataframe(texto_estructurado)

        # Agrega la información de la factura al DataFrame consolidado.
        df = pd.concat([df, df_factura], ignore_index=True)

    # Convierte los importes cuya moneda corresponde a dólares utilizando
    # el factor de conversión definido.
    df.loc[df["moneda"] == "dolares", "importe"] *= 0.9243

    # Conserva únicamente las primeras cuatro columnas del conjunto de datos.
    df = df.iloc[:, 0:4]

# Crea una conexión a la base de datos SQLite.
engine = create_engine("sqlite:///facturas.db")

# Inserta los registros procesados en la tabla "facturas",
# agregando la información existente sin reemplazarla.
df.to_sql("facturas", engine, if_exists="append", index=False)

# Libera la conexión con la base de datos.
engine.dispose()

# Informa la finalización del proceso.
print("Proceso de extracción y estructuración de facturas completado exitosamente.")
print("Datos guardados en la base de datos 'facturas.db'.")
