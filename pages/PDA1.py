import streamlit as st
from PIL import Image

st.header('Push Down Automata Regex 1')
img = Image.open('PDA.drawio.png')
st.image(img,width=600)

if st.button('Back to Homepage'):
    st.switch_page('main.py')