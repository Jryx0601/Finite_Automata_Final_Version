import streamlit as st
from PIL import Image

st.header('Push Down Automata Regex 1')
img = Image.open('PDA.drawio.png')
st.image(img,use_container_width=True)

if st.button('Back to Homepage'):
    st.switch_page('main.py')