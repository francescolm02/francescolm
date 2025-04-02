import streamlit as st
import random

# Datos de elementos químicos
elementos = {
    'Hidrógeno': {'símbolo': 'H', 'número_atómico': 1, 'grupo': 1},
    'Helio': {'símbolo': 'He', 'número_atómico': 2, 'grupo': 18},
    'Litio': {'símbolo': 'Li', 'número_atómico': 3, 'grupo': 1},
    'Carbono': {'símbolo': 'C', 'número_atómico': 6, 'grupo': 14},
    'Nitrógeno': {'símbolo': 'N', 'número_atómico': 7, 'grupo': 15},
    'Oxígeno': {'símbolo': 'O', 'número_atómico': 8, 'grupo': 16},
    'Neón': {'símbolo': 'Ne', 'número_atómico': 10, 'grupo': 18},
    'Sodio': {'símbolo': 'Na', 'número_atómico': 11, 'grupo': 1},
    'Magnesio': {'símbolo': 'Mg', 'número_atómico': 12, 'grupo': 2},
    'Aluminio': {'símbolo': 'Al', 'número_atómico': 13, 'grupo': 13},
}

# Función para hacer una pregunta sobre un elemento
def hacer_pregunta():
    # Seleccionar un elemento al azar
    elemento = random.choice(list(elementos.keys()))
    pregunta = f"¿Cuál es el símbolo del elemento {elemento}?"
    respuesta_correcta = elementos[elemento]['símbolo']
    return pregunta, respuesta_correcta

# Título de la aplicación
st.title('¡Juego de Preguntas sobre Elementos Químicos!')

# Pregunta aleatoria
pregunta, respuesta_correcta = hacer_pregunta()

# Mostrar la pregunta
st.write(pregunta)

# Crear una caja de texto para que el usuario ingrese su respuesta
respuesta_usuario = st.text_input('Tu respuesta:')

# Verificar si la respuesta es correcta
if respuesta_usuario:
    if respuesta_usuario.strip().lower() == respuesta_correcta.lower():
        st.success('¡Correcto! 🎉')
    else:
        st.error(f'Incorrecto. La respuesta correcta es: {respuesta_correcta}.')

# Botón para obtener una nueva pregunta
if st.button('Nueva pregunta'):
    pregunta, respuesta_correcta = hacer_pregunta()
    st.write(pregunta)
