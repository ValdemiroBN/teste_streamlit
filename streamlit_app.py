import streamlit as st
from PIL import Image

st.title("Upload e visualização de imagem")

uploaded_file = st.file_uploader("Escolha uma imagem", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagem carregada", use_container_width=True)
else:
    st.write("Aguardando upload...")
