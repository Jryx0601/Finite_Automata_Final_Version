import streamlit as st
from PIL import Image

st.header('Push Down Automata Regex 2')
img = Image.open('PDA2_Regex.png')
# st.image(img)

col1,col2,col3 = st.columns([1,10,1])
col2.image(img)

if st.button('Back to Homepage'):
    st.switch_page('main.py')