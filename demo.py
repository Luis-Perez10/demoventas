# prompt: Imprimir dataframe usando streamlit
import plotly.express as px
import streamlit as st
import pandas as pd

# Leer el archivo Excel
try:
    df = pd.read_excel('SalidaFinalVentas.xlsx')
    st.dataframe(df) # Use st.dataframe to display the DataFrame in Streamlit
except FileNotFoundError:
    st.error("Error: 'SalidaFinalVentas.xlsx' not found.")
except Exception as e:
    st.error(f"An error occurred: {e}")

# Leer el archivo Excel
try:
    df = pd.read_excel('SalidaFinalVentas.xlsx')

    # Verifica si la columna 'Region' existe en el Dataframe
    if 'Region' in df.columns:
        # Crea la gráfica de ventas por región
        fig = px.bar(df, x='Region', y='Sales', title='Ventas por Región') # Reemplaza 'Ventas' con el nombre de tu columna de ventas
        st.plotly_chart(fig)
    else:
        st.error("La columna 'Region' no se encuentra en el archivo.")

    st.dataframe(df) # Muestra el Dataframe en Streamlit
except FileNotFoundError:
    st.error("El archivo 'SalidaFinalVentas.xlsx' no se encontró.")
except Exception as e:
    st.error(f"Ocurrió un error al leer el archivo: {e}")
