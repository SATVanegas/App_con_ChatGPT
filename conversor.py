simport streamlit as st

# Título de la app
st.title("Conversor Universal")

# Autor
st.write("Esta app fue elaborada por Santiago Vanegas.")

# Selección de categoría
categoria = st.selectbox(
    "Selecciona una categoría de conversión:",
    [
        "Temperatura",
        "Longitud",
        "Peso/Masa",
        "Volumen",
        "Tiempo",
        "Velocidad",
        "Área",
        "Energía",
        "Presión",
        "Tamaño de Datos"
    ]
)

# Función para realizar la conversión
def convertir(valor, tipo_conversión):
    if tipo_conversión == "Celsius a Fahrenheit":
        return (valor * 9/5) + 32
    elif tipo_conversión == "Fahrenheit a Celsius":
        return (valor - 32) * 5/9
    elif tipo_conversión == "Celsius a Kelvin":
        return valor + 273.15
    elif tipo_conversión == "Kelvin a Celsius":
        return valor - 273.15
    elif tipo_conversión == "Pies a metros":
        return valor * 0.3048
    elif tipo_conversión == "Metros a pies":
        return valor / 0.3048
    elif tipo_conversión == "Pulgadas a centímetros":
        return valor * 2.54
    elif tipo_conversión == "Centímetros a pulgadas":
        return valor / 2.54
    elif tipo_conversión == "Libras a kilogramos":
        return valor * 0.453592
    elif tipo_conversión == "Kilogramos a libras":
        return valor / 0.453592
    elif tipo_conversión == "Onzas a gramos":
        return valor * 28.3495
    elif tipo_conversión == "Gramos a onzas":
        return valor / 28.3495
    elif tipo_conversión == "Galones a litros":
        return valor * 3.78541
    elif tipo_conversión == "Litros a galones":
        return valor / 3.78541
    elif tipo_conversión == "Pulgadas cúbicas a centímetros cúbicos":
        return valor * 16.387
    elif tipo_conversión == "Centímetros cúbicos a pulgadas cúbicas":
        return valor / 16.387
    elif tipo_conversión == "Horas a minutos":
        return valor * 60
    elif tipo_conversión == "Minutos a segundos":
        return valor * 60
    elif tipo_conversión == "Días a horas":
        return valor * 24
    elif tipo_conversión == "Semanas a días":
        return valor * 7
    elif tipo_conversión == "Millas por hora a kilómetros por hora":
        return valor * 1.60934
    elif tipo_conversión == "Kilómetros por hora a metros por segundo":
        return valor / 3.6
    elif tipo_conversión == "Nudos a millas por hora":
        return valor * 1.15078
    elif tipo_conversión == "Metros por segundo a pies por segundo":
        return valor * 3.28084
    elif tipo_conversión == "Metros cuadrados a pies cuadrados":
        return valor * 10.7639
    elif tipo_conversión == "Pies cuadrados a metros cuadrados":
        return valor / 10.7639
    elif tipo_conversión == "Kilómetros cuadrados a millas cuadradas":
        return valor / 2.58999
    elif tipo_conversión == "Millas cuadradas a kilómetros cuadrados":
        return valor * 2.58999
    elif tipo_conversión == "Julios a calorías":
        return valor * 0.239006
    elif tipo_conversión == "Calorías a kilojulios":
        return valor * 0.004184
    elif tipo_conversión == "Kilovatios-hora a megajulios":
        return valor * 3.6
    elif tipo_conversión == "Megajulios a kilovatios-hora":
        return valor / 3.6
    elif tipo_conversión == "Pascales a atmósferas":
        return valor / 101325
    elif tipo_conversión == "Atmósferas a pascales":
        return valor * 101325
    elif tipo_conversión == "Barras a libras por pulgada cuadrada":
        return valor * 14.5038
    elif tipo_conversión == "Libras por pulgada cuadrada a bares":
        return valor / 14.5038
    elif tipo_conversión == "Megabytes a gigabytes":
        return valor / 1024
    elif tipo_conversión == "Gigabytes a Terabytes":
        return valor / 1024
    elif tipo_conversión == "Kilobytes a megabytes":
        return valor / 1024
    elif tipo_conversión == "Terabytes a petabytes":
        return valor / 1024
    else:
        return None

# Mostrar las opciones según la categoría seleccionada
if categoria == "Temperatura":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"]
    )
elif categoria == "Longitud":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ["Pies a metros", "Metros a pies", "Pulgadas a centímetros", "Centímetros a pulgadas"]
    )
elif categoria == "Peso/Masa":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ["Libras a kilogramos", "Kilogramos a libras", "Onzas a gramos", "Gramos a onzas"]
    )
elif categoria == "Volumen":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ["Galones a litros", "Litros a galones", "Pulgadas cúbicas a centímetros cúbicos", "Centímetros cúbicos a pulgadas cúbicas"]
    )
elif categoria == "Tiempo":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ["Horas a minutos", "Minutos a segundos", "Días a horas", "Semanas a días"]
    )
elif categoria == "Velocidad":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ["Millas por hora a kilómetros por hora", "Kilómetros por hora a metros por segundo", "Nudos a millas por hora", "Metros por segundo a pies por segundo"]
    )
elif categoria == "Área":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ["Metros cuadrados a pies cuadrados", "Pies cuadrados a metros cuadrados", "Kilómetros cuadrados a millas cuadradas", "Millas cuadradas a kilómetros cuadrados"]
    )
elif categoria == "Energía":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ["Julios a calorías", "Calorías a kilojulios", "Kilovatios-hora a megajulios", "Megajulios a kilovatios-hora"]
    )
elif categoria == "Presión":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ["Pascales a atmósferas", "Atmósferas a pascales", "Barras a libras por pulgada cuadrada", "Libras por pulgada cuadrada a bares"]
    )
elif categoria == "Tamaño de Datos":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ["Megabytes a gigabytes", "Gigabytes a Terabytes", "Kilobytes a megabytes", "Terabytes a petabytes"]
    )

# Solicitar el valor para convertir
valor = st.number_input("Introduce el valor a convertir:", min_value=0.0)

# Realizar la conversión y mostrar el resultado
if valor:
    resultado = convertir(valor, conversion)
    st.write(f"{valor} {conversion.split(' a ')[0]} es igual a {resultado} {conversion.split(' a ')[1]}")
