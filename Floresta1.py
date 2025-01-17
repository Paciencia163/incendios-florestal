import streamlit as st
from PIL import Image

# Configurar a página
st.set_page_config(
    page_title="Classificação de Incêndios Florestais",
    page_icon="🔥",
    layout="centered",
)

# Cabeçalho com imagem e título
header_image = "incendio.png"  # Link para uma imagem de floresta
st.image(header_image, use_column_width=True)

st.markdown("<h1 style='text-align: center; color: #ff6f61;'>🌳 Classificação de Incêndios Florestais 🔥</h1>", unsafe_allow_html=True)

# Subtítulo
st.markdown(
    "<p style='text-align: center; color: #6d6d6d; font-size: 18px;'>"
    "Carregue uma imagem da floresta para verificar seu status. Ajude a monitorar e proteger o meio ambiente! 🌿"
    "</p>",
    unsafe_allow_html=True,
)

# Caixa de upload de arquivos
uploaded_file = st.file_uploader("📂 Faça upload de uma imagem", type=["jpg", "jpeg", "png"])

# Se o usuário carregar uma imagem
if uploaded_file is not None:
    try:
        # Abrir a imagem
        image = Image.open(uploaded_file)
        
        # Exibir a imagem carregada com bordas arredondadas
        st.markdown("<h3 style='color: #007BFF;'>🔍 Imagem carregada:</h3>", unsafe_allow_html=True)
        st.image(image, caption="Visualização da Imagem", use_column_width=True)

        # Extrair o nome do arquivo
        file_name = uploaded_file.name
        
        # Verificar status da floresta
        if "floresta" in file_name.lower():
            st.markdown(
                "<div style='background-color: #d4edda; border-radius: 10px; padding: 15px;'>"
                "<h4 style='color: #155724;'>🌲 Floresta Segura!</h4>"
                "<p style='color: #155724;'>Nenhum risco identificado. Continue preservando a natureza. 🌿</p>"
                "</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                "<div style='background-color: #f8d7da; border-radius: 10px; padding: 15px;'>"
                "<h4 style='color: #721c24;'>⚠️ Floresta em Risco!</h4>"
                "<p style='color: #721c24;'>Por favor, investigue imediatamente. 🚨</p>"
                "</div>",
                unsafe_allow_html=True,
            )
    except Exception as e:
        st.error("Erro ao processar o arquivo. Certifique-se de que é uma imagem válida.")
else:
    st.info("Por favor, faça o upload de uma imagem para começar.")

# Rodapé
st.markdown(
    """
    <hr>
    <p style='text-align: center; color: #6d6d6d; font-size: 14px;'>
    Desenvolvido com ❤️ usando Streamlit | Proteja nossas florestas 🌳
    </p>
    """,
    unsafe_allow_html=True,
)
