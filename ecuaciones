import streamlit as st
import numpy as np

# Título de la app
st.title("Resolución de Ecuaciones Lineales")

# Autor
st.write("Esta app fue elaborada por 'COLOQUE AQUÍ SU NOMBRE'.")

# Instrucciones para el usuario
st.write("""
Ingresa las ecuaciones en forma de matriz. Proporciona:
- Los coeficientes en forma de matriz (cada fila representa una ecuación).
- El vector de constantes independientes.
""")

# Entrada para el número de ecuaciones y variables
st.subheader("Definir el sistema de ecuaciones")
num_ecuaciones = st.number_input("Número de ecuaciones (y variables):", min_value=1, step=1)

if num_ecuaciones > 0:
    st.subheader("Ingresar los coeficientes de la matriz")
    
    # Entrada para la matriz de coeficientes
    st.write("Proporciona los coeficientes de cada ecuación:")
    matriz_coeficientes = []
    for i in range(int(num_ecuaciones)):
        fila = st.text_input(f"Coeficientes de la ecuación {i + 1} (separados por comas):")
        if fila:
            matriz_coeficientes.append([float(x) for x in fila.split(",")])

    # Entrada para el vector de constantes
    st.subheader("Ingresar el vector de constantes independientes")
    vector_constantes = st.text_input("Proporciona las constantes independientes (separadas por comas):")
    
    # Resolver el sistema si los datos están completos
    if st.button("Resolver sistema"):
        try:
            if len(matriz_coeficientes) == num_ecuaciones and vector_constantes:
                # Convertir a arrays numpy
                matriz = np.array(matriz_coeficientes)
                constantes = np.array([float(x) for x in vector_constantes.split(",")])

                # Verificar dimensiones
                if matriz.shape[0] == matriz.shape[1] == len(constantes):
                    # Resolver el sistema
                    solucion = np.linalg.solve(matriz, constantes)
                    st.success("Solución encontrada:")
                    for i, x in enumerate(solucion):
                        st.write(f"Variable x{i + 1} = {x:.4f}")
                else:
                    st.error("La matriz de coeficientes debe ser cuadrada y coincidir con el número de constantes.")
            else:
                st.error("Por favor, completa todos los datos.")
        except Exception as e:
            st.error(f"Error al resolver el sistema: {e}")
