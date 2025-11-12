import streamlit as st
import pandas as pd
import os
from PIL import Image

# ---------- CONFIGURAÇÃO ----------
st.set_page_config(page_title="Catálogo - Pronta Entrega", layout="wide")

# ---------- LOGO ----------
BASE_DIR = os.path.dirname(__file__)
LOGO_PATH = os.path.join(BASE_DIR, "static", "imagens", "logo.png")

if os.path.exists(LOGO_PATH):
    logo = Image.open(LOGO_PATH)
    st.sidebar.image(logo, use_column_width=True)
else:
    st.sidebar.write("Logo não encontrada.")

# ---------- FUNÇÃO PARA CARREGAR IMAGENS ----------
def carregar_imagem(nome_arquivo):
    """
    Retorna o caminho completo da imagem se existir,
    caso contrário retorna a imagem padrão 'SEM IMAGEM.jpg'.
    """
    img_dir = os.path.join(BASE_DIR, "static", "imagens")
    caminho = os.path.join(img_dir, nome_arquivo)

    if os.path.exists(caminho):
        return caminho
    else:
        sem_img = os.path.join(img_dir, "SEM IMAGEM.jpg")
        return sem_img if os.path.exists(sem_img) else None

# ---------- CARREGAR DADOS ----------
arquivo_excel = os.path.join(BASE_DIR, "catalogo.xlsx")

if os.path.exists(arquivo_excel):
    df = pd.read_excel(arquivo_excel)
else:
    st.error("Arquivo de catálogo não encontrado.")
    st.stop()

# ---------- TÍTULO ----------
st.title("Catálogo - Pronta Entrega")
st.write("Explore os produtos disponíveis em nosso estoque!")

# ---------- LISTAGEM DE PRODUTOS ----------
colunas = st.columns(3)
for idx, row in df.iterrows():
    col = colunas[idx % 3]
    with col:
        imagem_path = carregar_imagem(f"{row['DESCRIÇÃO DO PRODUTO']}.jpg")

        if imagem_path:
            st.image(imagem_path, use_column_width=True)
        else:
            st.write("Sem imagem disponível")

        st.markdown(f"**{row['DESCRIÇÃO DO PRODUTO']}**")
        st.write(f"Marca: {row['MARCA']}")
        st.write(f"Preço: R$ {row['POR']}")

# ---------- RODAPÉ ----------
st.markdown("---")
st.caption("© 2025 Catálogo Digital - CLAMI")
