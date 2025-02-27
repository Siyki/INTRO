import streamlit as st
from PIL import Image

st.title("Mi primera chamba")
st.header("la proxima semana no se como hice esto")
st.write("soy diseñadora, no programadora, no sé que pretenden")
fotito=Image.open('actually.jpg')
st.image(fotito, caption= 'Sisoy')


texto=st.text_input('Holi', 'holix2')
st.write('El texto escrito es', texto)

st.subheader ("Ahora usemos 2 columnas")

col1,col2= st.columns(2)
