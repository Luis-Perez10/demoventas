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

# prompt: arma una grafica de las ventas por region del dataframe df usando streamlit

import pandas as pd
import streamlit as st
import plotly.express as px

# Install openpyxl if you haven't already
# !pip install openpyxl  # This should be removed, as it's in the original code

try:
  df = pd.read_excel('SalidaFinalVentas.xlsx', engine='openpyxl')
  #print(df.head()) # Print the first few rows to verify

  # Assuming 'Region' and 'Ventas' columns exist in your dataframe
  if 'Region' not in df.columns or 'Ventas' not in df.columns:
      st.error("Error: 'Region' or 'Ventas' columns not found in the DataFrame.")
  else:
      fig = px.bar(df, x='Region', y='Ventas', title='Ventas por Región')
      st.plotly_chart(fig)

except FileNotFoundError:
  st.error("Error: 'SalidaFinalVentas.xlsx' not found. Please upload the file to your current working directory.")
except Exception as e:
  st.error(f"An error occurred: {e}")


# st.write(df) # This line can be removed or commented out if not needed

# prompt: arma una grafica de las ventas por region del dataframe df usando streamlit

# Assuming 'Region' and 'Ventas' columns exist in your dataframe
if 'Region' not in df.columns or 'Sales' not in df.columns:
    st.error("Error: 'Region' or 'Sales' columns not found in the DataFrame.")
else:
    fig = px.bar(df, x='Region', y='Sales', title='Ventas por Región')
    st.plotly_chart(fig)
