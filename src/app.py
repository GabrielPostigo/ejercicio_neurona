# Importación de los paquetes
import streamlit as st
import pandas as pd

src_ima = "https://cerebriti.b-cdn.net/uploads/897d9983bb5cd413ce50cdbbdcfe75c2.jpg"

tab1, tab2, tab3 = st.tabs(["Una Entrada", "Dos Entradas", "Tres Entradas y Sesgo"])

st.image(src_ima, caption='Imagen Neurona')

st.title('!Hola neurona¡')

with tab1:
   st.text('Peso w0')
   w0 = st.slider('',0,0.00,5.00)
   st.text('Entrada X0')
   x0 = st.number_input(step=1)
   y = w0*x0

   if st.button('Calcular la salida'):
      st.text(f'La salida de la neurona es {y}')

with tab2:
    col1,col2 = st.columns(2)
    with col1:
        st.text('Peso w0')
        w01 = st.slider('',0,0.00,5.00)
        st.text('Entrada X0')
        x01 = st.number_input(step=1)
    
    with col2:
        st.text('Peso w1')
        w1 = st.slider('',0,0.00,5.00)
        st.text('Entrada X1')
        x1 = st.number_input(step=1)
    
    y1 = (w01*x01)+(w1*x1)

    if st.button('Calcular la salida'):
        st.text(f'La salida de la neurona es {y1}')


with tab3:
    col11,col21,col3 = st.columns(3)
    with col11:
        st.text('Peso w0')
        w02 = st.slider('',0,0.00,5.00)
        st.text('Entrada X0')
        x02 = st.number_input(step=1)
    
    with col21:
        st.text('Peso w1')
        w12 = st.slider('',0,0.00,5.00)
        st.text('Entrada X1')
        x12 = st.number_input(step=1)
    
    with col3:
        st.text('Peso w2')
        w2 = st.slider('',0,0.00,5.00)
        st.text('Entrada X2')
        x2 = st.number_input(step=1)

    st.number_input('Introduzca el valor del sesgo', step=1)

    y2 = (x02*w02)+(x12*w12)+(x2*w2)+b

    if st.button('Calcular la salida'):
        st.text(f'La salida de la neurona es {y2}')