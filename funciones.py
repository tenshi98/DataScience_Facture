"""
Módulo para extraer texto desde archivos PDF, procesarlo mediante OpenAI
y convertir la respuesta estructurada en formato CSV a un DataFrame de pandas.

El flujo general es:
1. Cargar las variables de entorno.
2. Extraer el texto del archivo PDF.
3. Enviar el texto a OpenAI para obtener una estructura en formato CSV.
4. Convertir el CSV recibido a un DataFrame con los tipos de datos adecuados.

Dependencias:
- openai
- PyMuPDF (fitz)
- python-dotenv
- pandas
- io.StringIO
- prompt (módulo local)

Variables de entorno:
- OPENAI_API_KEY: Clave de API utilizada para autenticar las solicitudes a OpenAI.
"""

import openai
import fitz  # PyMuPDF
from dotenv import load_dotenv
import os
import pandas as pd
from io import StringIO
from prompt import prompt

# Cargar variables de entorno desde el archivo .env
load_dotenv(".env")

# Obtener la clave de API de OpenAI desde las variables de entorno
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def extraer_texto_pdf(ruta_pdf):
    """
    Extrae el contenido textual completo de un archivo PDF.

    Abre el archivo PDF especificado y concatena el texto de todas sus
    páginas en una única cadena separada por saltos de línea.

    Args:
        ruta_pdf (str): Ruta del archivo PDF a procesar.

    Returns:
        str: Texto extraído de todas las páginas del documento.

    Raises:
        fitz.FileDataError: Si el archivo PDF está dañado o es inválido.
        RuntimeError: Excepciones generadas por PyMuPDF durante la apertura
            o lectura del documento.
    """

    # Abrir el documento PDF.
    doc = fitz.open(ruta_pdf)

    # Extraer el texto de cada página y unirlo en una única cadena.
    text = "\n".join([page.get_text("text") for page in doc])

    return text


def estructurar_texto(texto):
    """
    Envía el texto extraído a OpenAI para obtener una respuesta estructurada
    en formato CSV.

    El modelo recibe instrucciones para devolver exclusivamente un CSV válido
    o la palabra 'error' cuando no sea posible extraer información útil.

    Args:
        texto (str): Contenido textual que será enviado al modelo.

    Returns:
        str: Texto en formato CSV devuelto por el modelo o la cadena 'error'.

    Raises:
        openai.OpenAIError: Excepciones relacionadas con la comunicación con la API.
    """

    # Crear el cliente de OpenAI utilizando la clave configurada.
    cliente = openai.OpenAI(api_key=OPENAI_API_KEY)

    # Enviar el texto al modelo para su procesamiento.
    respuesta = cliente.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Eres un experto en extracción de datos de facturas. Devuelve solo el CSV sin explicaciones ni mensajes adicionales. Si no puedes extraer datos, devuelve exactamente la palabra 'error' sin comillas.",
            },
            {
                "role": "user",
                "content": prompt + "\n Este es el texto a parsear:\n" + texto,
            },
        ],
    )

    # Obtener el contenido textual de la primera respuesta del modelo.
    csv_respuesta = respuesta.choices[0].message.content.strip()

    return csv_respuesta


def csv_a_dataframe(csv):
    """
    Convierte un texto en formato CSV a un DataFrame de pandas.

    Define explícitamente los tipos de datos esperados y transforma la
    columna 'importe' a un valor numérico, reemplazando las comas por
    puntos para asegurar una conversión correcta.

    Args:
        csv (str): Contenido en formato CSV separado por punto y coma.

    Returns:
        pandas.DataFrame: DataFrame con las columnas tipadas y la columna
        'importe' convertida a valores numéricos.

    Raises:
        pandas.errors.ParserError: Si el contenido CSV no tiene un formato válido.
        KeyError: Si la columna 'importe' no existe en el CSV recibido.
        ValueError: Si ocurre un problema durante la conversión de datos.
    """

    # Definir los tipos de datos para cada columna.
    dtype_cols = {
        "fecha_factura": str,
        "proveedor": str,
        "concepto": str,
        "importe": str,
        "moneda": str,
    }

    # Leer el contenido CSV y aplicar los tipos de datos definidos.
    df_temp = pd.read_csv(StringIO(csv), delimiter=";", dtype=dtype_cols)

    # Convertir la columna 'importe' a valores numéricos.
    df_temp["importe"] = pd.to_numeric(
        df_temp["importe"].str.replace(",", "."), errors="coerce"
    )

    return df_temp
