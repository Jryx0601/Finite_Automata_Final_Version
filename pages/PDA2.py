import streamlit as st
from PIL import Image

st.header('Push Down Automata Regex 2')
img = Image.open('PDA2_Regex.png')
st.image(img,width=600)

if st.button('Back to Homepage'):
    st.switch_page('main.py')