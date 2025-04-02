import streamlit as st

# Título de la aplicación
st.title('Preguntas sobre Elementos Químicos')

# Instrucciones
st.markdown("""
Bienvenido a la aplicación de preguntas sobre elementos químicos. Puedes escribir el nombre de un elemento y te proporcionaremos información relevante sobre él.
""")

# Diccionario de elementos químicos con sus detalles
elementos = {
    'Hidrógeno': {
        'símbolo': 'H',
        'número_atómico': 1,
        'grupo': 'No metales',
        'propiedades': 'Es el elemento más ligero y abundante del universo.'
    },
    'Helio': {
        'símbolo': 'He',
        'número_atómico': 2,
        'grupo': 'Gases nobles',
        'propiedades': 'Es un gas noble, incoloro, inodoro e insípido.'
    },
    'Oxígeno': {
        'símbolo': 'O',
        'número_atómico': 8,
        'grupo': 'No metales',
        'propiedades': 'Es esencial para la respiración de los seres vivos.'
    },
    'Carbono': {
        'símbolo': 'C',
        'número_atómico': 6,
        'grupo': 'No metales',
        'propiedades': 'Es la base de la vida, formando la estructura de las moléculas orgánicas.'
