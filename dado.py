import streamlit as st
import numpy as np
import pandas as pd

# Título de la aplicación
st.title('Simulación de Lanzamiento de un Dado')

# Simular el lanzamiento de un dado 20 veces
resultados = np.random.randint(1, 7, size=20)

# Mostrar los resultados de cada lanzamiento
st.subheader('Resultados de los lanzamientos')
st.write(resultados)

# Calcular estadísticas
media = np.mean(resultados)
mediana = np.median(resultados)
moda = pd.Series(resultados).mode()[0]  # Moda usando Pandas
varianza = np.var(resultados)
desviacion_estandar = np.std(resultados)

# Mostrar el análisis de las estadísticas
st.subheader('Análisis Estadístico')
st.write(f'Media: {media}')
st.write(f'Mediana: {mediana}')
st.write(f'Moda: {moda}')
st.write(f'Varianza: {varianza}')
st.write(f'Desviación estándar: {desviacion_estandar}')

# Calcular la frecuencia de cada número del dado (1 al 6)
frecuencias = pd.Series(resultados).value_counts().sort_index()

# Mostrar la tabla de frecuencias
st.subheader('Tabla de Frecuencias')
st.write(frecuencias)

# Crear un gráfico de barras para mostrar la frecuencia de cada número
st.bar_chart(frecuencias)
