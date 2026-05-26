import streamlit as st
import streamlit.components.v1 as components

# Configuración de la interfaz para aprovechar todo el ancho de la pantalla
st.set_page_config(layout="wide")

# Apertura y lectura del archivo de diseño HTML con codificación universal UTF-8
with open("index.html", "r", encoding="utf-8") as archivo:
    codigo_html = archivo.read()

# Renderizado del HTML dentro de Streamlit
# Nota: Puede incrementar el valor de 'height' si su aplicación requiere más espacio vertical
components.html(codigo_html, height=900, scrolling=True)
