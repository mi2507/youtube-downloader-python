import streamlit as st
from yt_dlp import YoutubeDL
import os

st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: #df2c14; 
        color: white; 
        padding: 16px 36px; /* Tamanho do botão */
        border: none; /* Sem borda */
        border-radius: 5px; /* Bordas arredondadas */
        font-size: 16px; /* Tamanho da fonte */
        cursor: pointer; /* Cursor de ponteiro */
    }
    div.stButton > button:hover {
        background-color: #c61a09; /* Cor ao passar o mouse */
         color: white; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image("youTube.png", width=150)

# Título e instruções
st.title("Youtube Downloader")
st.markdown("Insira o link para fazer o download do vídeo")

# Entrada do link
url = st.text_input("Cole seu link aqui")

# Botão de download
if st.button("Download"):
    if not url:
        st.error("Por favor, insira um link válido.")
    else:
        # Exibir mensagem de progresso
        st.info("Baixando...")

        # Configurações do YoutubeDL
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join("downloads", '%(title)s.%(ext)s'),  # Pasta de saída e formato
        }

        # Criar a pasta 'downloads' se não existir
        os.makedirs("downloads", exist_ok=True)

        try:
            # Realizar o download
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])  # Usar o link inserido pelo usuário
            st.success("Download concluído com sucesso!")
        except Exception as e:
            st.error(f"Ocorreu um erro: {e}")
