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
    st.markdown("O método une a precisão técnica ao bem-estar e à **Bioestética**.")
    with st.expander("👗 Geometria Corporal (Kibbe)", expanded=True):
        st.write("Estudo da estrutura óssea e muscular para harmonia física.")
    with st.expander("🎨 Essências de Estilo (Kitchener)", expanded=True):
        st.write("Análise da mensagem que o seu rosto transmite.")

def pagina_analise_360():
    st.title("📏 Triagem Sistêmica 360º")
    st.info("Preencha as etapas para o seu Relatório Premium.")

    nome = st.text_input("Nome da Cliente:").strip()
    altura = st.number_input("Altura (ex: 1.60):", min_value=1.0, value=1.60, step=0.01)

    st.divider()

    # --- ETAPA 1: KIBBE ---
    st.markdown("### 👗 ETAPA 1: GEOMETRIA CORPORAL (KIBBE)")
    c1, c2 = st.columns(2)
    with c1:
        p1 = st.radio("1. Estrutura Óssea:", ["A) Estreita", "B) Larga", "C) Simétrica"])
        curva = st.radio("2. Presença de Curvas nítidas?", ["S", "N"])
    with c2:
        carne = st.radio("3. Textura da Carne:", ["A) Densa/Firme", "B) Macia/Suave"])

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

    st.divider()

    # --- ETAPA 2: TEMPERAMENTO (LOGICA COMPLETA REINTEGRADA) ---
    st.markdown("### 🧠 ETAPA 2: TEMPERAMENTO")
    st.write("Responda com base no seu comportamento natural:")
    
    e1 = st.radio("1. Em lugares totalmente desconhecidos:", ["A) Sinto-me à vontade e interajo", "B) Sou observadora/Prefiro analisar"])
    e2 = st.radio("2. Tomada de Decisão:", ["A) Racional/Lógica", "B) Emocional/Sentimental"])
    e3 = st.radio("3. Velocidade de Reação:", ["A) Rápida e Imediata", "B) Lenta e Criteriosa"])
    e4 = st.radio("4. Duração do Sentimento:", ["A) Curta (esqueço logo)", "B) Longa (guardo por muito tempo)"])

    # Lógica de Veredito
    temp_veredito = ""
    if "A)" in e1 and "A)" in e2: temp_veredito = "COLÉRICO"
    elif "A)" in e1 and "B)" in e2: temp_veredito = "SANGUÍNEO"
    elif "B)" in e1 and "A)" in e2: temp_veredito = "MELANCÓLICO"
    elif "B)" in e1 and "B)" in e2: temp_veredito = "FLEUMÁTICO"

    if st.button("SOLICITAR DOSSIÊ PREMIUM"):
        if not nome:
            st.error("Por favor, preencha o seu nome.")
        else:
            relatorio = f"*NOVA TRIAGEM 360º*%0A*Nome:* {nome}%0A*Kibbe:* {kibbe_res}%0A*Temperamento:* {temp_veredito}"
            st.success(f"Triagem concluída! O seu temperamento predominante é: **{temp_veredito}**")
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
