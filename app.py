import streamlit as st
from PIL import Image

st.title("mi primera chamba")
st.header("la proxima semana no se como hice esto")
st.write("soy diseñadora, no programadora, no sé que pretenden")
fotito=Image.open('actually.jpg')
st.image(fotito, caption= 'Sisoy')
