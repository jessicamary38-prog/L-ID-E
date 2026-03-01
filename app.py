import streamlit as st
import os

# --- 1. CONFIGURAÇÕES DE PÁGINA E ESTÉTICA ---
st.set_page_config(
    page_title="Maison L'Idée - Jéssica Maria", 
    page_icon="⚜️", 
    layout="centered"
)

# Estilização CSS para o visual de Luxo e Consultoria
st.markdown("""
    <style>
    .main { background-color: #fcfaf7; }
    .stButton>button {
        background-color: #D4AF37;
        color: white;
        border-radius: 10px;
        font-weight: bold;
        transition: 0.3s;
        border: none;
        width: 100%;
        height: 3em;
    }
    .stButton>button:hover {
        background-color: #B8860B;
        transform: translateY(-2px);
    }
    h1, h2, h3 { color: #4a3728; font-family: 'serif'; }
    .st-emotion-cache-16idsys p { font-size: 1.1rem; line-height: 1.6; color: #5D4037; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. FUNÇÕES DAS PÁGINAS ---

def pagina_inicio():
    st.title("⚜️ Maison L'Idée")
    st.subheader("O Olhar por trás da Maison")
    
    # --- BANNER PRINCIPAL ---
    if os.path.exists("banner.png"):
        st.image("banner.png")
    else:
        st.image("https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1000")
    
    st.divider()
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # --- FOTO DE PERFIL (Ajustado para o nome que está no seu GitHub) ---
        if os.path.exists("perfil.JPG"):
            st.image("perfil.JPG", caption="Jéssica Maria")
        elif os.path.exists("perfil.JPG"):
            st.image("perfil.JPG", caption="Jéssica Maria")
        else:
            st.warning("Foto 'perfil.JPG' não encontrada.")
        
        st.markdown("### Conecte-se")
        st.link_button("📸 INSTAGRAM", "https://www.instagram.com/jessicamargo.mr")
        st.link_button("📌 PINTEREST", "https://www.pinterest.com/jessicamary38")
        
    with col2:
        st.markdown("""
        ### O Olhar por trás da Maison
        
        Sou uma apaixonada por moda que transformou a curiosidade em uma busca incessante pelas estratégias mais profundas de imagem. 
        Minha jornada começou com os estudos dos métodos de **David Kibbe e John Kitchener**, onde me encantei pela forma como a estrutura física e as essências moldam quem somos.

        No entanto, ao unir esses métodos, percebi que ainda faltava uma peça no quebra-cabeça: **a humanidade sistêmica**.

        Há anos, mergulho nos estudos dos temperamentos, da neurociência e do comportamento humano. Dessa investigação nasceu o meu método exclusivo. Eu não olho apenas para a roupa; eu olho para a mulher como um sistema inteiro, integrando corpo, face e essência.

        Para garantir a precisão dessa entrega, uni o sensível ao tecnológico através de **Engenharia de Prompts**, garantindo que cada consultoria seja baseada em dados criteriosos.

        **Prazer, Jéssica Maria.**
        """)

def pagina_posts():
    st.title("📖 O Método Maison L'Idée")
    st.subheader("Uma Visão Sistêmica da Image")
    
    if os.path.exists("banner.png"):
        st.image("banner.png", caption="Curadoria Maison L'Idée")
    
    st.markdown("""
    Na Maison L'Idée, não seguimos regras rígidas ou paletas genéricas. Nosso método é uma jornada profunda de autoconhecimento que une a precisão técnica ao bem-estar clínico.
    """)

    with st.expander("👗 Geometria Corporal (Kibbe)", expanded=True):
        st.write("A análise da sua estrutura óssea e composição física para identificar sua geometria natural e criar harmonia visual.")

    with st.expander("🎨 Essências de Estilo (Kitchener)", expanded=True):
        st.write("O estudo do seu rosto e presença para revelar a mensagem que sua imagem comunica ao mundo.")

    with st.expander("🧠 Temperamento e Comportamento", expanded=True):
        st.write("Alinhamento da imagem ao seu sistema nervoso e personalidade através da neurociência.")

    st.divider()
    st.header("✨ Nosso Diferencial")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Validação Tecnológica:** Uso de Engenharia de Prompts para diagnósticos precisos.")
        st.markdown("**Harmonia vs. Paletas:** Foco no Visagismo e identidade única.")
    with c2:
        st.markdown("**Foco na Vitalidade:** Beleza integrada ao bem-estar e saúde física.")
        st.markdown("**Ciência e Cuidado:** Um olhar para a mulher como um sistema indissociável.")

    st.link_button("👑 QUERO MINHA ANÁLISE SISTÊMICA", "https://wa.me/5515996398197?text=Olá%20Jéssica!%20Quero%20saber%20mais%20sobre%20o%20Método%20Maison.")

def pagina_teste_kibbe():
    st.title("📏 Teste de Geometria Corporal")
    with st.form("form_kibbe"):
        nome = st.text_input("Seu Nome:")
        altura = st.number_input("Altura (m):", min_value=1.0, value=1.60, step=0.01)
        p1 = st.radio("Percepção Visual:", ["A) Longilínea", "B) Proporcional", "C) Petit"])
        p2 = st.radio("Linha Ombro/Quadril:", ["A) Reta/V", "B) Simétrica", "C) Curva"])
        submeter = st.form_submit_button("VER RESULTADO")

    if submeter:
        if altura >= 1.70: res = "DRAMATIC FAMILY"
        elif altura <= 1.62: res = "GAMINE/ROMANTIC"
        else: res = "CLASSIC/NATURAL"
        
        st.success(f"### RESULTADO: {res}")
        st.link_button("💬 VALIDAR COM JÉSSICA MARIA", f"https://wa.me/5515996398197?text=Meu%20Kibbe%20deu%20{res}")

# --- 3. NAVEGAÇÃO ---
pg = st.navigation({
    "A Maison": [st.Page(pagina_inicio, title="Início", icon="🏠")],
    "O Método": [st.Page(pagina_posts, title="Journal", icon="📖")],
    "Análise": [st.Page(pagina_teste_kibbe, title="Teste Kibbe", icon="📏")]
})
pg.run()
