import streamlit as st

# Título de la app
st.title("Mi primera app")

# Autor
st.write("Esta app fue elaborada por Santiago Vanegas.")

# Preguntar al usuario por su nombre
nombre_usuario = st.text_input("¿Cuál es tu nombre?")

# Mostrar el mensaje de bienvenida
if nombre_usuario:
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")
