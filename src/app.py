# Importación de los paquetes
import streamlit as st
import pandas as pd

# src_ima = "https://cerebriti.b-cdn.net/uploads/897d9983bb5cd413ce50cdbbdcfe75c2.jpg"

tab1, tab2, tab3 = st.tabs(["Una Entrada", "Dos Entradas", "Tres Entradas y Sesgo"])

st.image('imagen_neurona.jpg', caption=None)

st.title('!Hola neurona¡')

with tab1:
    # st.markdown('Peso w<sub>0</sub>', unsafe_allow_html=True)
    w0 = st.slider('Peso',0,0.0,5.0)
    # st.markdown('Entrada x<sub>0</sub>', unsafe_allow_html=True)
    x0 = st.number_input("Introduzca el valor de la entrada")
    y = w0*x0

    if st.button('Calcular la salida','b1'):
        st.text(f'La salida de la neurona es {y}')

with tab2:
    col1,col2 = st.columns(2)
    with col1:
        st.markdown('Peso w<sub>0</sub>', unsafe_allow_html=True)
        w01 = st.slider('s1',0.0,5.0, label_visibility='collapsed')
        st.markdown('Entrada x<sub>0</sub>', unsafe_allow_html=True)
        x01 = st.number_input('i1',step=1)
    
    with col2:
        st.markdown('Peso w<sub>1</sub>', unsafe_allow_html=True)
        w1 = st.slider('s2',0,0.0,5.0, label_visibility='collapsed')
        st.markdown('Peso x<sub>1</sub>', unsafe_allow_html=True)
        x1 = st.number_input('i2',step=1)
    
    y1 = (w01*x01)+(w1*x1)

    if st.button('Calcular la salida','b2'):
        st.text(f'La salida de la neurona es {y1}')


with tab3:
    col11,col21,col3 = st.columns(3)
    with col11:
        st.markdown('Peso w<sub>0</sub>', unsafe_allow_html=True)
        w02 = st.slider('s3',0,0.0,5.0, label_visibility='collapsed')
        st.markdown('Entrada x<sub>0</sub>', unsafe_allow_html=True)
        x02 = st.number_input('i3',step=1)
    
    with col21:
        st.markdown('Peso w<sub>1</sub>', unsafe_allow_html=True)
        w12 = st.slider('s4',0,0.0,5.0, label_visibility='collapsed')
        st.markdown('Entrada x<sub>1</sub>', unsafe_allow_html=True)
        x12 = st.number_input('i4',step=1)
    
    with col3:
        st.markdown('Peso w<sub>2</sub>', unsafe_allow_html=True)
        w2 = st.slider('s5',0,0.0,5.0, label_visibility='collapsed')
        st.markdown('Entrada x<sub>2</sub>', unsafe_allow_html=True)
        x2 = st.number_input('i5',step=1)

    b = st.number_input('Introduzca el valor del sesgo')

    y2 = (x02*w02)+(x12*w12)+(x2*w2)+b

    if st.button('Calcular la salida','b3'):
        st.text(f'La salida de la neurona es {y2}')