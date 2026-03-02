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
        ### O Olhar por trás da Maison
        Sou uma apaixonada por moda que transformou a curiosidade em uma busca incessante pelas estratégias mais profundas de imagem. 
        Minha jornada começou com os estudos dos métodos de **David Kibbe e John Kitchener**.

        Integro corpo, face e essência através da neurociência e do comportamento humano. Dessa investigação nasceu o meu método exclusivo: a **humanidade sistêmica**.

        Para garantir a precisão, utilizo tecnologias de **Engenharia de Prompts**, garantindo que cada consultoria seja baseada em dados criteriosos.

        **Prazer, Jéssica Maria.**
        """)

def pagina_journal():
    st.title("📖 O Método Maison L'Idée")
    st.subheader("Uma Visão Sistêmica da Imagem")
    
    if os.path.exists("banner.png"):
        st.image("banner.png", caption="Curadoria Maison L'Idée")
    
    st.markdown("""
    Na Maison L'Idée, não seguimos regras rígidas. Nosso método une a precisão técnica ao bem-estar clínico.
    """)

    with st.expander("👗 Geometria Corporal (Kibbe)", expanded=True):
        st.write("Estudo da estrutura óssea e muscular para que as roupas moldem sua moldura física com harmonia.")

    with st.expander("🎨 Essências de Estilo (Kitchener)", expanded=True):
        st.write("Análise da mensagem que seu rosto e sua presença transmitem ao mundo.")

    with st.expander("🧠 Temperamento e Comportamento", expanded=True):
        st.write("Alinhamento da imagem ao seu sistema nervoso, garantindo que sua imagem seja uma ferramenta de confiança.")

    st.divider()
    st.header("✨ Nosso Diferencial")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Validação Tecnológica:** Engenharia de Prompts para diagnósticos precisos.")
    with c2:
        st.markdown("**Foco na Vitalidade:** Beleza integrada ao bem-estar e saúde física.")

def pagina_analise_360():
    st.title("📏 Triagem Sistêmica 360º")
    st.info("Preencha as etapas abaixo. A Etapa 1 é uma cortesia; as demais compõem o seu Relatório Premium.")

    nome = st.text_input("Nome da Cliente:").strip()
    email = st.text_input("Seu melhor E-mail:")
    altura = st.number_input("Altura (ex: 1.52):", min_value=1.0, value=1.60, step=0.01)

    st.divider()

    # --- ETAPA 1: KIBBE ---
    st.markdown("### 👗 ETAPA 1: KIBBE (CORTESIA)")
    c1, c2 = st.columns(2)
    with c1:
        p1 = st.radio("1. Estrutura Óssea:", ["A) Estreita", "B) Larga", "C) Simétrica"])
        curva = st.radio("2. Presença de Curvas nítidas?", ["S", "N"])
    with c2:
        carne = st.radio("3. Textura da Carne:", ["A) Densa/Firme", "B) Macia/Suave"])

    # Lógica Kibbe Original
    kibbe_res = ""
    if altura <= 1.63:
        if curva == "S": kibbe_res = "SOFT GAMINE" if "A)" in carne else "FAMÍLIA ROMÂNTICA"
        else: kibbe_res = "FLAMBOYANT GAMINE" if "A)" in carne else "GAMINE MISTO"
    elif altura >= 1.70:
        if curva == "S": kibbe_res = "SOFT DRAMATIC"
        elif "B)" in p1: kibbe_res = "FLAMBOYANT NATURAL"
        else: kibbe_res = "DRAMATIC"
    else:
        if curva == "S": kibbe_res = "SOFT NATURAL" if "B)" in p1 else "SOFT CLASSIC"
        else: kibbe_res = "NATURAL PURE" if "B)" in p1 else "CLASSIC / DRAMATIC CLASSIC"

    if st.button("REVELAR MEU KIBBE"):
        st.success(f"Resultado Preliminar: **{kibbe_res}**")

    st.divider()

    # --- ETAPA 2: ESSÊNCIAS ---
    st.markdown("### 🎨 ETAPA 2: ESSÊNCIAS FACIAIS")
    pts = {"Dramatic": 0, "Natural": 0, "Classic": 0, "Romantic": 0, "Gamine": 0, "Ingenue": 0}
    r1 = st.selectbox("Formato do Rosto:", ["Longo", "Oval", "Quadrado", "Redondo", "Pequeno"])
    if r1 == "Longo": pts["Dramatic"] += 40
    elif r1 == "Oval": pts["Classic"] += 40
    elif r1 == "Quadrado": pts["Natural"] += 40
    elif r1 == "Redondo": pts["Ingenue"] += 20; pts["Romantic"] += 20
    elif r1 == "Pequeno": pts["Gamine"] += 40

    r2 = st.selectbox("Formato da Boca:", ["Carnuda/Arredondada", "Larga/Aberta", "Pequena", "Fina"])
    if r2 == "Carnuda/Arredondada": pts["Romantic"] += 30
    elif r2 == "Larga/Aberta": pts["Natural"] += 30
    elif r2 == "Pequena": pts["Ingenue"] += 30
    elif r2 == "Fina": pts["Dramatic"] += 15; pts["Gamine"] += 15

    st.divider()

    # --- ETAPA 3: TEMPERAMENTO ---
    st.markdown("### 🧠 ETAPA 3: TEMPERAMENTO")
    e1 = st.radio("Energia:", ["A) Extrovertida", "B) Introvertida"])
    e2 = st.radio("Julgamento:", ["A) Racional", "B) Emocional"])
    e3 = st.radio("Reação:", ["A) Rápida/Imediata", "B) Lenta/Criteriosa"])
    e4 = st.radio("Duração do Impacto:", ["A) Curta", "B) Longa"])

    if st.button("SOLICITAR DOSSIÊ PREMIUM"):
        if not nome or not email:
            st.error("Por favor, preencha nome e e-mail.")
        else:
            relatorio = f"NOVA TRIAGEM: {nome} | Email: {email} | Kibbe: {kibbe_res} | Temp: {e1[0]}{e2[0]}{e3[0]}{e4[0]} | Scores: {pts}"
            st.success("Dados prontos! Clique abaixo para falar com Jéssica.")
            st.link_button("👑 ENVIAR PARA JÉSSICA MARIA", f"https://wa.me/5515996398197?text={relatorio.replace(' ', '%20')}")

# --- 3. NAVEGAÇÃO ---
pg = st.navigation({
    "Maison": [st.Page(pagina_inicio, title="Início", icon="🏠")],
    "Método": [st.Page(pagina_journal, title="Journal", icon="📖")],
    "Análise": [st.Page(pagina_analise_360, title="Triagem 360º", icon="📏")]
})
pg.run()
