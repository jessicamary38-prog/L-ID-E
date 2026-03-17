import streamlit as st
import os

# --- 1. CONFIGURAÇÕES DE PÁGINA ---
st.set_page_config(
    page_title="Maison L'Idée - Jéssica Maria", 
    page_icon="⚜️", 
    layout="centered"
)

# Estilização CSS Maison
st.markdown("""
    <style>
    .main { background-color: #fcfaf7; }
    .stButton>button {
        background-color: #D4AF37; color: white; border-radius: 10px;
        font-weight: bold; width: 100%; height: 3em; border: none; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #B8860B; transform: translateY(2px); }
    h1, h2, h3 { color: #4a3728; font-family: 'serif'; }
    .st-emotion-cache-16idsys p { font-size: 1.1rem; line-height: 1.6; color: #5D4037; }
    .quote { border-left: 5px solid #D4AF37; padding-left: 20px; font-style: italic; color: #4a3728; margin: 20px 0; }
    .highlight-name { font-size: 1.5rem; font-weight: bold; color: #4a3728; margin-top: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DEFINIÇÃO DAS PÁGINAS ---

def pagina_inicio():
    st.title("🏛️ Maison L’Idée")
    st.subheader("Onde a Alma Encontra sua Imagem")
    if os.path.exists("banner.png"): st.image("banner.png")
    st.markdown("""
    A Maison L’Idée (A Casa da Ideia) não é apenas um espaço de consultoria de imagem; é um refúgio dedicado à revelação da identidade. Acreditamos que a beleza não é algo que se cria do zero, mas algo que se descobre e se organiza.
    
    Nascemos da convicção de que cada ser humano é um projeto único, desenhado com uma geometria específica e uma essência inconfundível. Nosso papel é ser a ponte entre quem você é por dentro e o que o mundo vê por fora.
    
    ### 🌿 Nossa Filosofia: A Beleza em Ordem
    Para nós, a imagem é um testemunho silencioso. Quando há um abismo entre a sua alma e a sua aparência, o resultado é o cansaço emocional. Na Maison, trabalhamos para que haja paz no espelho. Unimos três pilares fundamentais para criar uma harmonia que gera repetição e conforto:
    
    * **O Temperamento:** A força da sua alma e o seu ritmo interno.
    * **A Geometria (Kibbe):** O respeito às linhas e formas do seu projeto original.
    * **A Essência (Kitchener):** O perfume e a mensagem que o seu rosto emana.
    """)

def pagina_jessica():
    st.title("⚜️ Jéssica Maria")
    st.subheader("A Curadora por trás da Maison")
    col1, col2 = st.columns([1, 1.5])
    with col1:
        if os.path.exists("perfil.png"): st.image("perfil.png")
        st.link_button("📸 INSTAGRAM", "https://www.instagram.com/jessicamargo.mr")
    with col2:
        st.markdown("""
        Integro corpo, face e essência através da neurociência e do comportamento humano. 
        Dessa investigação nasceu o meu método exclusivo: a **humanidade sistêmica**.
        
        Acredito que vestir-se de si mesma é um ato de autogoverno e honra ao seu projeto original. Meu papel é ser a ponte que traduz a sua essência em uma imagem coerente e cheia de paz.
        """)
        st.markdown('<p class="highlight-name">Prazer, Jéssica Maria.</p>', unsafe_allow_html=True)

def pagina_maternar():
    st.title("🕊️ Maternar Leve") # Ícone alterado para pomba (paz)
    st.markdown("""
    A maternidade é a nossa missão mais profunda. Na Maison L'Idée, acreditamos que o lar é o nosso primeiro santuário, e a forma como educamos nossos filhos é a nossa maior obra de arte. Por isso, convidamos a Raiane Camargo para trazer luz a este caminho através do @amae.pedagoga_.
    
    ### A Pedagogia do Afeto
    
    "Quando o Francisco chegou, minha casa se transformou na minha primeira sala de aula. 🏠✨
    
    Eu sou a Raiane, tenho 24 anos e, ao ver o mundo pelos olhos do meu filho, entendi que a pedagogia não está apenas nos livros, mas no dia a dia, nas brincadeiras e no afeto. Minha faculdade se tornou a ferramenta para criar momentos lúdicos, amorosos e cheios de propósito para ele.
    
    O Maternar Leve nasce desse desejo de viver a Maternidade Sagrada: entendendo que cada descoberta é um milagre e cada ensinamento é uma semente de eternidade. Decidi tirar esse conhecimento do papel para criar o @amae.pedagoga_ — um espaço onde vou te mostrar que é possível se conectar com seu filho através do ensinar, de forma simples e cheia de significado.
    
    A infância passa rápido demais para não aproveitarmos cada revelação."
    """)
    st.link_button("✨ SIGA @AMAE.PEDAGOGA_", "https://www.instagram.com/amae.pedagoga_")

def pagina_importa():
    st.title("❤️ Alguém se Importa")
    st.markdown("""
    Muitas vezes, a desistência não acontece de uma hora para outra. Ela é um caminho silencioso... 
    *(Texto completo conforme enviado anteriormente)*
    """)
    st.markdown('<div class="quote">"Porque Deus amou o mundo de tal maneira..." (João 3:16)</div>', unsafe_allow_html=True)
    st.link_button("📩 CONVERSAR COM JÉSSICA", "https://wa.me/5515996398197")

def pagina_biblioteca():
    st.title("📚 Biblioteca Maison L’Idée")
    st.markdown("""
    Entre e sinta-se em casa... *(Texto completo conforme enviado anteriormente)*
    """)
    st.link_button("☕ ACESSAR BIBLIOTECA", "https://drive.google.com/drive/folders/1i9UQn39hkamqAefA3-bsErfadjObVhSF")

def pagina_analise_360():
    st.title("📏 Triagem Sistêmica 360º")
    st.info("Etapa 1: Temperamento (Cortesia).")
    nome = st.text_input("Nome:")
    # ... (Lógica da triagem)
    if st.button("SOLICITAR DOSSIÊ"):
        st.success("Dados prontos para envio.")

def pagina_modelo():
    st.title("📔 Modelo de Consultoria")
    st.write("Conheça a estrutura do Dossiê que entregamos em nossa consultoria premium.")
    st.link_button("🔗 VER MODELO NO NOTION", "https://www.notion.so/Dossi-J-ssica-Maria-317f44f5bd8680c3b6a9e0ea0243822d")

# --- 3. NAVEGAÇÃO CORRIGIDA ---
pg = st.navigation({
    "Maison": [
        st.Page(pagina_inicio, title="A Maison L'Idée", icon="🏛️"),
        st.Page(pagina_jessica, title="Quem Sou Eu", icon="⚜️"),
        st.Page(pagina_biblioteca, title="Biblioteca", icon="📚"),
    ],
    "Consultoria": [
        st.Page(pagina_analise_360, title="Triagem 360º", icon="📏"),
        st.Page(pagina_modelo, title="Modelo Dossiê", icon="📔"), # Correção aqui
    ],
    "Acolhimento": [
        st.Page(pagina_maternar, title="Maternar Leve", icon="🕊️"),
        st.Page(pagina_importa, title="Alguém se Importa", icon="❤️"),
    ]
})
pg.run()
