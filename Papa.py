import streamlit as st

# Título de la app
st.title("Cálculo del PAPA")

# Autor
st.write("Esta app fue elaborada por 'COLOQUE AQUÍ SU NOMBRE'.")

# Instrucciones para el usuario
st.write("Ingresa las materias vistas con sus respectivas calificaciones, créditos y tipología.")

# Crear listas para almacenar la información de las materias
materias = []
calificaciones = []
creditos = []
tipologias = []

# Lista de tipologías disponibles
tipologias_disponibles = ["Básica", "Electiva", "Disciplinar", "Libre elección"]

# Formulario para ingresar datos de las materias
st.subheader("Agregar información de materias")
nombre_materia = st.text_input("Nombre de la materia:")
calificacion = st.number_input("Calificación (0.0 a 5.0):", min_value=0.0, max_value=5.0, step=0.1)
credito = st.number_input("Créditos (número entero):", min_value=1, step=1)
tipologia = st.selectbox("Tipología de la asignatura:", tipologias_disponibles)

if st.button("Agregar materia"):
    if nombre_materia:
        materias.append(nombre_materia)
        calificaciones.append(calificacion)
        creditos.append(credito)
        tipologias.append(tipologia)
        st.success(f"Materia '{nombre_materia}' agregada con éxito.")
    else:
        st.error("Por favor, ingresa el nombre de la materia antes de agregar.")

# Mostrar materias ingresadas
if materias:
    st.subheader("Materias ingresadas")
    for i in range(len(materias)):
        st.write(f"- {materias[i]}: Calificación = {calificaciones[i]}, Créditos = {creditos[i]}, Tipología = {tipologias[i]}")

# Cálculo del PAPA global
if st.button("Calcular PAPA Global"):
    if materias:
        suma_ponderada = sum(c * cal for c, cal in zip(creditos, calificaciones))
        suma_creditos = sum(creditos)
        papa_global = suma_ponderada / suma_creditos if suma_creditos > 0 else 0
        st.subheader("Resultado PAPA Global")
        st.write(f"Tu PAPA global es: **{papa_global:.2f}**")
    else:
        st.error("Por favor, ingresa materias antes de calcular el PAPA.")

# Cálculo del PAPA por tipología
if st.button("Calcular PAPA por Tipología"):
    if materias:
        tipologias_unicas = set(tipologias)
        st.subheader("Resultados por Tipología")
        for tipo in tipologias_unicas:
            indices = [i for i, t in enumerate(tipologias) if t == tipo]
            suma_ponderada_tipo = sum(creditos[i] * calificaciones[i] for i in indices)
            suma_creditos_tipo = sum(creditos[i] for i in indices)
            papa_tipo = suma_ponderada_tipo / suma_creditos_tipo if suma_creditos_tipo > 0 else 0
            st.write(f"- Tipología '{tipo}': PAPA = **{papa_tipo:.2f}**")
    else:
        st.error("Por favor, ingresa materias antes de calcular el PAPA por tipología.")
