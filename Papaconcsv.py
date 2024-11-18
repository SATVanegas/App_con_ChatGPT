import streamlit as st
import pandas as pd

# Título de la app
st.title("Cálculo del PAPA a partir de archivo")

# Autor
st.write("Esta app fue elaborada por 'COLOQUE AQUÍ SU NOMBRE'.")

# Instrucciones
st.write("""
Puedes cargar un archivo CSV con la siguiente estructura:
- **Materia**: Nombre de la asignatura.
- **Calificación**: Nota obtenida (0.0 a 5.0).
- **Créditos**: Número de créditos de la asignatura.
- **Tipología**: Tipo de asignatura (por ejemplo: Básica, Electiva, Disciplinar, Libre elección).
""")

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
