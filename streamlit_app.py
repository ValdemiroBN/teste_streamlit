import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

# Carrega o modelo BLIP
@st.cache_resource
def carregar_modelo():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = carregar_modelo()

st.title("Descrição automática de imagem (IA)")

uploaded_file = st.file_uploader("Escolha uma imagem", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Imagem carregada", use_container_width=True)

    st.subheader("Descrição gerada pela IA:")

    # Geração da legenda
    inputs = processor(images=image, return_tensors="pt")
    out = model.generate(**inputs)
    descricao = processor.decode(out[0], skip_special_tokens=True)

    st.success(descricao)
else:
    st.write("Aguardando upload...")
