import streamlit as st
import pandas as pd

# Título de la app
st.title("Cálculo del PAPA a partir de un archivo")

# Autor
st.write("Esta app fue elaborada por 'Santiago Vanegas'.")

# Instrucciones detalladas
st.subheader("Instrucciones")
st.write("""
1. Crea un archivo en Google Sheets o Excel con la siguiente estructura:
   - **Materia**: Nombre de la asignatura (por ejemplo, Matemáticas I).
   - **Calificación**: Nota obtenida en la materia (valor entre 0.0 y 5.0).
   - **Créditos**: Número de créditos de la asignatura (número entero).
   - **Tipología**: Tipo de asignatura (por ejemplo: Básica, Electiva, Disciplinar, Libre elección).

2. Descarga un archivo de ejemplo desde el siguiente enlace para usar como referencia:
   [Formato de archivo ejemplo](https://docs.google.com/spreadsheets/d/1depMTygqb67yKFLL7FWiJic7Hx4tdBzaB5Qrs4CYeNk/edit?usp=sharing)

3. Asegúrate de que tu archivo tenga estas **exactas columnas**: `Materia`, `Calificación`, `Créditos`, y `Tipología`.

4. Guarda el archivo en formato CSV. Si estás usando Google Sheets, selecciona `Archivo > Descargar > Valores separados por comas (.csv)`.

5. Sube el archivo en el cargador de archivos a continuación para calcular tu PAPA global y por tipología.
""")

# Ejemplo del formato del archivo
st.subheader("Ejemplo del formato del archivo:")
ejemplo_df = pd.DataFrame({
    "Materia": ["Matemáticas I", "Física II", "Historia Moderna"],
    "Calificación": [4.5, 3.8, 4.0],
    "Créditos": [3, 4, 2],
    "Tipología": ["Básica", "Disciplinar", "Libre elección"]
})
st.table(ejemplo_df)

# Cargar archivo CSV
archivo_subido = st.file_uploader("Sube tu archivo CSV aquí", type=["csv"])

if archivo_subido:
    try:
        # Leer el archivo CSV
        df = pd.read_csv(archivo_subido)

        # Validar columnas requeridas
        columnas_requeridas = ["Materia", "Calificación", "Créditos", "Tipología"]
        if all(col in df.columns for col in columnas_requeridas):
            # Mostrar el archivo cargado
            st.subheader("Datos cargados:")
            st.dataframe(df)

            # Cálculo del PAPA global
            suma_ponderada = sum(df["Calificación"] * df["Créditos"])
            suma_creditos = sum(df["Créditos"])
            papa_global = suma_ponderada / suma_creditos if suma_creditos > 0 else 0
            st.subheader("PAPA Global")
            st.write(f"Tu PAPA global es: **{papa_global:.2f}**")

            # Cálculo del PAPA por tipología
            st.subheader("PAPA por Tipología")
            for tipologia, grupo in df.groupby("Tipología"):
                suma_ponderada_tipo = sum(grupo["Calificación"] * grupo["Créditos"])
                suma_creditos_tipo = sum(grupo["Créditos"])
                papa_tipo = suma_ponderada_tipo / suma_creditos_tipo if suma_creditos_tipo > 0 else 0
                st.write(f"- Tipología '{tipologia}': PAPA = **{papa_tipo:.2f}**")

        else:
            st.error("El archivo no contiene las columnas requeridas: 'Materia', 'Calificación', 'Créditos', 'Tipología'.")
    except Exception as e:
        st.error(f"Error al procesar el archivo: {e}")
