import streamlit as st
import libreria_funciones as lf

st.sidebar.title("Datos")
st.sidebar.image("DMC_image.png")

st.title("Mi primera app")
st.image("Python_logo.png", width=100)
st.title("Clase 5 funciones")

p = st.number_input("Ingrese el monto principal", value= 12000)
t = st.number_input("Ingrese la tasa anual", value= 0.05)
a = st.slider("Seleccione el número de años del préstamo", min_value= 1, max_value= 5, value= 1)
pa = st.number_input("Cantidad de pagos por años", value= 12)

cuota = lf.cuota_prestamo(p, t, a, pa)
st.write(cuota)