import streamlit as st
import pandas as pd

# Título de la app
st.title("Cálculo del PAPA (Promedio Acumulado de Puntos Académicos)")

# Autor
st.write("Esta app fue elaborada por Santiago Vanegas.")

# Estructura para guardar las asignaturas ingresadas
if 'asignaturas' not in st.session_state:
    st.session_state.asignaturas = pd.DataFrame(columns=["Nombre", "Tipología", "Calificación", "Créditos"])

# Función para agregar asignatura
def agregar_asignatura(nombre, tipologia, calificacion, creditos):
    nueva_asignatura = pd.DataFrame({"Nombre": [nombre], "Tipología": [tipologia], 
                                     "Calificación": [calificacion], "Créditos": [créditos]})
    st.session_state.asignaturas = pd.concat([st.session_state.asignaturas, nueva_asignatura], ignore_index=True)

# Función para calcular el PAPA
def calcular_papa():
    total_creditos = st.session_state.asignaturas['Créditos'].sum()
    suma_puntos = (st.session_state.asignaturas['Calificación'] * st.session_state.asignaturas['Créditos']).sum()
    if total_creditos > 0:
        papa_global = suma_puntos / total_creditos
    else:
        papa_global = 0
    return papa_global

# Función para calcular el PAPA por tipología
def calcular_papa_por_tipologia(tipologia):
    asignaturas_tipologia = st.session_state.asignaturas[st.session_state.asignaturas['Tipología'] == tipologia]
    total_creditos = asignaturas_tipologia['Créditos'].sum()
    suma_puntos = (asignaturas_tipologia['Calificación'] * asignaturas_tipologia['Créditos']).sum()
    if total_creditos > 0:
        papa_tipologia = suma_puntos / total_creditos
    else:
        papa_tipologia = 0
    return papa_tipologia

# Sección para ingresar asignaturas
st.header("Ingreso de Asignaturas")
nombre = st.text_input("Nombre de la Asignatura")
tipologia = st.selectbox("Tipología de la Asignatura", ["Obligatoria", "Optativa", "Formación General"])
calificacion = st.slider("Calificación obtenida", 0.0, 5.0, 0.0, 0.1)
creditos = st.number_input("Créditos de la asignatura", min_value=1, step=1)

if st.button("Agregar Asignatura"):
    if nombre and tipologia and calificacion >= 0.0 and creditos > 0:
        agregar_asignatura(nombre, tipologia, calificacion, creditos)
        st.success(f"Asignatura {nombre} agregada exitosamente.")
    else:
        st.error("Por favor, completa todos los campos correctamente.")

# Mostrar las asignaturas ingresadas
st.header("Asignaturas Ingresadas")
st.dataframe(st.session_state.asignaturas)

# Calcular el PAPA global
st.header("Cálculo del PAPA Global")
papa_global = calcular_papa()
st.write(f"El PAPA global es: {papa_global:.2f}")

# Calcular el PAPA por tipología
st.header("Cálculo del PAPA por Tipología")
tipologia_seleccionada = st.selectbox("Selecciona la tipología para el cálculo del PAPA", ["Obligatoria", "Optativa", "Formación General"])
papa_tipologia = calcular_papa_por_tipologia(tipologia_seleccionada)
st.write(f"El PAPA para las asignaturas de tipología '{tipologia_seleccionada}' es: {papa_tipologia:.2f}")
