import streamlit as st
import os

# --- 1. CONFIGURAÇÕES DE PÁGINA ---
st.set_page_config(
    page_title="Maison L'Idée - Jéssica Maria", 
    page_icon="⚜️", 
    layout="centered"
)

# Estilização CSS Premium
st.markdown("""
    <style>
    .main { background-color: #fcfaf7; }
    .stButton>button {
        background-color: #D4AF37; color: white; border-radius: 10px;
        font-weight: bold; width: 100%; height: 3em; border: none; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #B8860B; transform: translateY(-2px); }
    h1, h2, h3 { color: #4a3728; font-family: 'serif'; }
    .st-emotion-cache-16idsys p { font-size: 1.1rem; line-height: 1.6; color: #5D4037; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DEFINIÇÃO DAS PÁGINAS ---

def pagina_inicio():
    st.title("⚜️ Maison L'Idée")
    st.subheader("O Olhar por trás da Maison")
    if os.path.exists("banner.png"): 
        st.image("banner.png")
    st.divider()
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("perfil.JPG"): 
            st.image("perfil.JPG", caption="Jéssica Maria")
        st.markdown("### Conecte-se")
        st.link_button("📸 INSTAGRAM", "https://www.instagram.com/jessicamargo.mr")
        st.link_button("📌 PINTEREST", "https://www.pinterest.com/jessicamary38")
    with col2:
        st.markdown("""
        ### Quem Sou Eu
        Integro corpo, face e essência através da neurociência e do comportamento humano. 
        Dessa investigação nasceu o meu método exclusivo: a **humanidade sistêmica**.
        
        **Prazer, Jéssica Maria.**
        """)

def pagina_journal():
    st.title("📖 O Método Maison L'Idée")
    st.subheader("Journal: Visão Sistêmica")
    if os.path.exists("banner.png"):
        st.image("banner.png")
    
    st.markdown("""
    Na Maison L'Idée, o método une a precisão técnica ao bem-estar e à **Bioestética**.
    """)
    with st.expander("👗 Geometria Corporal (Kibbe)", expanded=True):
        st.write("Estudo da estrutura óssea e muscular para que as roupas moldem sua moldura física com harmonia.")
    
    with st.expander("🎨 Essências de Estilo (Kitchener)", expanded=True):
        st.write("Análise da mensagem que seu rosto e sua presença transmitem ao mundo através da geometria facial.")
    
    with st.expander("🧠 Temperamento e Comportamento", expanded=True):
        st.write("""
        **O pilar invisível da sua imagem.** Investigamos como o seu sistema nervoso reage ao mundo. 
        O temperamento define sua energia e comportamento, garantindo que sua imagem seja uma extensão real de quem você é.
        """)

def pagina_analise_360():
    st.title("📏 Triagem Sistêmica 360º")
    st.info("A Etapa 1 é um presente da Maison. As demais compõem seu Dossiê Premium.")

    nome = st.text_input("Nome da Cliente:").strip()
    email = st.text_input("Seu melhor E-mail:")
    altura = st.number_input("Sua Altura (ex: 1.60):", min_value=1.0, value=1.60, step=0.01)

    st.divider()

    # --- ETAPA 1: TEMPERAMENTO (O NOVO BRINDE) ---
    st.markdown("### 🧠 ETAPA 1: TEMPERAMENTO (BRINDE)")
    st.write("Descubra o seu perfil comportamental predominante:")
    t1 = st.radio("1. Em lugares novos:", ["A) Sinto-me à vontade/Interajo", "B) Sou observadora/Analiso"])
    t2 = st.radio("2. Suas decisões são mais:", ["A) Racionais/Lógicas", "B) Emocionais/Sentimentais"])
    t3 = st.radio("3. Reação a imprevistos:", ["A) Rápida e Imediata", "B) Lenta e Criteriosa"])
    t4 = st.radio("4. Duração dos sentimentos:", ["A) Curta (esqueço rápido)", "B) Longa (guardo/intensifico)"])

    temp_veredito = ""
    if "A)" in t1 and "A)" in t2: temp_veredito = "COLÉRICO"
    elif "A)" in t1 and "B)" in t2: temp_veredito = "SANGUÍNEO"
    elif "B)" in t1 and "A)" in t2: temp_veredito = "MELANCÓLICO"
    elif "B)" in t1 and "B)" in t2: temp_veredito = "FLEUMÁTICO"

    if st.button("REVELAR MEU TEMPERAMENTO (CORTESIA)"):
        st.success(f"Seu temperamento predominante é: **{temp_veredito}**")

    st.divider()

    # --- ETAPA 2: KIBBE (OCULTO) ---
    st.markdown("### 👗 ETAPA 2: GEOMETRIA CORPORAL")
    c1, c2 = st.columns(2)
    with c1:
        k_osseo = st.radio("Estrutura Óssea:", ["A) Estreita", "B) Larga", "C) Simétrica"])
        k_curva = st.radio("Curvas nítidas?", ["Sim", "Não"])
    with c2:
        k_carne = st.radio("Textura da Carne:", ["A) Densa/Firme", "B) Macia/Suave"])

    st.divider()

    # --- ETAPA 3: ESSÊNCIAS (OCULTO) ---
    st.markdown("### 🎨 ETAPA 3: ANÁLISE FACIAL")
    f1 = st.selectbox("Formato do Rosto:", ["Longo", "Oval", "Quadrado", "Redondo", "Pequeno"])
    f2 = st.selectbox("Formato dos Olhos:", ["Grandes e Redondos", "Rasgados/Feline", "Amendoados", "Médios/Simétricos"])
    f3 = st.selectbox("Formato da Boca:", ["Carnuda", "Larga", "Pequena", "Fina"])

    if st.button("SOLICITAR DOSSIÊ COMPLETO"):
        if not nome or not email:
            st.error("Por favor, preencha nome e e-mail.")
        else:
            relatorio = (
                f"*SOLICITAÇÃO DE DOSSIÊ COMPLETO*%0A"
                f"------------------------------------%0A"
                f"*CLIENTE:* {nome}%0A"
                f"*ALTURA:* {altura}%0A"
                f"------------------------------------%0A"
                f"*1. TEMPERAMENTO (Revelado):* {temp_veredito}%0A"
                f"------------------------------------%0A"
                f"*2. DADOS KIBBE (Para calcular):*%0A"
                f"- Ósseo: {k_osseo}%0A"
                f"- Curvas: {k_curva}%0A"
                f"- Carne: {k_carne}%0A"
                f"------------------------------------%0A"
                f"*3. DADOS FACIAIS:*%0A"
                f"- Rosto: {f1}%0A"
                f"- Olhos: {f2}%0A"
                f"- Boca: {f3}%0A"
            )
            st.success("Tudo pronto! Clique abaixo para me enviar os dados.")
            st.link_button("👑 ENVIAR PARA JÉSSICA MARIA", f"https://wa.me/5515996398197?text={relatorio}")

def pagina_modelo():
    st.title("📔 Modelo de Consultoria")
    st.markdown("### Veja como será seu Dossiê")
    st.write("Explore um exemplo real da entrega final da Maison L'Idée.")
    st.link_button("🔗 VER MODELO DE DOSSIÊ COMPLETO", "https://www.notion.so/Dossi-J-ssica-Maria-317f44f5bd8680c3b6a9e0ea0243822d")

# --- 3. NAVEGAÇÃO ---
pg = st.navigation({
    "Maison": [st.Page(pagina_inicio, title="Quem Sou Eu", icon="🏠")],
    "Método": [st.Page(pagina_journal, title="Journal", icon="📖")],
    "Análise": [st.Page(pagina_analise_360, title="Triagem 360º", icon="📏")],
    "Exemplo": [st.Page(pagina_modelo, title="Modelo de Consultoria", icon="📔")]
})
pg.run()
