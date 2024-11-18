import streamlit as st
import pandas as pd
import datetime

# Título de la app
st.title("Registro de Finanzas Personales")

# Autor
st.write("Esta app fue elaborada por Santiago.")

# Crear una estructura de datos para almacenar los presupuestos, ingresos y gastos
if 'presupuestos' not in st.session_state:
    st.session_state.presupuestos = pd.DataFrame(columns=["Categoría", "Presupuesto Mensual"])
if 'registros' not in st.session_state:
    st.session_state.registros = pd.DataFrame(columns=["Fecha", "Categoría", "Tipo", "Monto"])

# Función para agregar un presupuesto
def agregar_presupuesto(categoria, monto):
    st.session_state.presupuestos = st.session_state.presupuestos.append({"Categoría": categoria, "Presupuesto Mensual": monto}, ignore_index=True)

# Función para registrar un ingreso o gasto
def registrar_transaccion(fecha, categoria, tipo, monto):
    st.session_state.registros = st.session_state.registros.append({"Fecha": fecha, "Categoría": categoria, "Tipo": tipo, "Monto": monto}, ignore_index=True)

# Sección para ingresar presupuesto
st.header("Definir Presupuesto Mensual")

# Ingresar categorías presupuestarias
categorias = st.text_area("Introduce las categorías de tu presupuesto, separadas por comas (ej. Alimentación, Transporte, Entretenimiento)").split(",")
categorias = [cat.strip() for cat in categorias if cat.strip()]

# Ingresar el presupuesto para cada categoría
presupuestos = {}
for categoria in categorias:
    monto = st.number_input(f"Ingrese el presupuesto mensual para {categoria}:", min_value=0.0, step=0.01)
    presupuestos[categoria] = monto

if st.button("Guardar Presupuesto"):
    for categoria, monto in presupuestos.items():
        agregar_presupuesto(categoria, monto)
    st.success("Presupuesto guardado exitosamente.")

# Sección para ingresar transacciones (ingresos/gastos)
st.header("Registrar Transacciones (Ingresos/Gastos)")

# Ingresar fecha, categoría, tipo de transacción (Ingreso/Gasto) y monto
fecha = st.date_input("Fecha de la transacción", min_value=datetime.date(2023, 1, 1))
categoria = st.selectbox("Selecciona la categoría de la transacción", categorias)
tipo = st.radio("Tipo de transacción", ("Ingreso", "Gasto"))
monto = st.number_input("Monto de la transacción:", min_value=0.0, step=0.01)

if st.button("Registrar Transacción"):
    registrar_transaccion(fecha, categoria, tipo, monto)
    st.success("Transacción registrada exitosamente.")

# Mostrar los presupuestos actuales
st.header("Presupuestos Actuales")
st.dataframe(st.session_state.presupuestos)

# Mostrar las transacciones registradas
st.header("Transacciones Registradas")
st.dataframe(st.session_state.registros)

# Generar reporte de diferencias (Presupuestado vs Real)
st.header("Reportes de Finanzas")

# Fecha de inicio (para el reporte semanal o mensual)
fecha_inicio = st.date_input("Selecciona la fecha de inicio para el reporte", min_value=datetime.date(2023, 1, 1))

# Filtrar las transacciones según la fecha
transacciones_filtradas = st.session_state.registros[st.session_state.registros['Fecha'] >= fecha_inicio]

# Reporte semanal o mensual
tipo_reporte = st.radio("Selecciona el tipo de reporte", ("Semanal", "Mensual"))

# Función para calcular el reporte de diferencias
def reporte_diferencias(tipo_reporte):
    # Agrupar las transacciones por categoría
    transacciones_filtradas['Semana'] = transacciones_filtradas['Fecha'].apply(lambda x: x.isocalendar()[1])  # Semana del año
    transacciones_filtradas['Mes'] = transacciones_filtradas['Fecha'].apply(lambda x: x.month)  # Mes

    # Dependiendo del tipo de reporte, filtrar por semana o mes
    if tipo_reporte == "Semanal":
        transacciones_filtradas['Semana'] = transacciones_filtradas['Fecha'].apply(lambda x: x.isocalendar()[1])
        transacciones_filtradas_grouped = transacciones_filtradas.groupby(['Semana', 'Categoría', 'Tipo'])['Monto'].sum().reset_index()
    elif tipo_reporte == "Mensual":
        transacciones_filtradas_grouped = transacciones_filtradas.groupby(['Mes', 'Categoría', 'Tipo'])['Monto'].sum().reset_index()

    # Comparar las transacciones reales con el presupuesto
    reporte = pd.merge(
        transacciones_filtradas_grouped,
        st.session_state.presupuestos,
        left_on="Categoría",
        right_on="Categoría",
        how="left"
    )

    # Calcular la diferencia (real - presupuestado)
    reporte['Diferencia'] = reporte['Monto'] - reporte['Presupuesto Mensual']
    
    return reporte

# Mostrar el reporte
if st.button("Generar Reporte"):
    reporte = reporte_diferencias(tipo_reporte)
    st.write(f"Reporte {tipo_reporte}:")
    st.dataframe(reporte)

