# prompt: Imprimir dataframe usando streamlit

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
