import streamlit as st
import os

# --- 1. CONFIGURAÇÕES DE PÁGINA E ESTÉTICA ---
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
    
    if os.path.exists("banner.png"):
        st.image("banner.png")
    else:
        st.image("https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1000")
    
    st.divider()
    
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists("perfil.JPG"):
            st.image("perfil.JPG", caption="Jéssica Maria")
        else:
            st.warning("Aguardando arquivo perfil.JPG")
        
        st.markdown("### Conecte-se")
        st.link_button("📸 INSTAGRAM", "https://www.instagram.com/jessicamargo.mr")
        st.link_button("📌 PINTEREST", "https://www.pinterest.com/jessicamary38")
        
    with col2:
        st.markdown("""
        ### O Olhar por trás da Maison
        Sou uma apaixonada por moda que transformou a curiosidade em uma busca incessante pelas estratégias mais profundas de imagem. 
        Minha jornada começou com os estudos dos métodos de **David Kibbe e John Kitchener**.

        No entanto, percebi que faltava a **humanidade sistêmica**. Integro corpo, face e essência através da neurociência e do comportamento.

        Utilizo tecnologias de **Engenharia de Prompts** para validar cada consultoria com precisão.

        **Prazer, Jéssica Maria.**
        """)

def pagina_posts():
    st.title("📖 O Método Maison L'Idée")
    if os.path.exists("banner.png"):
        st.image("banner.png")
    
    st.markdown("""
    ### Uma Visão Sistêmica da Imagem
    Na Maison L'Idée, unimos precisão técnica ao bem-estar clínico.
    
    * **👗 Geometria Corporal (Kibbe):** Estudo da estrutura óssea e distribuição de carne.
    * **🎨 Essências (Kitchener):** A mensagem do rosto e presença.
    * **🧠 Neurociência:** Alinhamento da imagem ao temperamento.
    """)
    st.link_button("👑 QUERO MINHA ANÁLISE", "https://wa.me/5515996398197")

def pagina_teste_kibbe():
    st.title("📏 Teste de Geometria Corporal (Kibbe)")
    st.info("Sistema de análise baseado na sua lógica de Scores Yin/Yang.")

    with st.form("form_kibbe_final"):
        nome = st.text_input("Nome da cliente:")
        altura = st.number_input("Altura (ex: 1.52):", min_value=1.0, value=1.60, step=0.01)
        
        st.divider()
        
        p1 = st.selectbox("1. Escala Visual: Como você parece nas fotos?", 
                         ["Selecione...", "A) Longilínea (pareço mais alta)", "B) Proporcional", "C) Petit (pareço pequena)"])
        
        p2 = st.selectbox("2. Geometria Ombro vs Quadril:", 
                         ["Selecione...", "A) Reta ou em V (ombros mandam)", "B) Contínua e simétrica", "C) Curva em 8 (quadril/busto saem)"])
        
        p3 = st.selectbox("3. Sensação da Carne:", 
                         ["Selecione...", "A) Firme e densa", "B) Macia e suave"])
        
        submeter = st.form_submit_button("REVELAR VEREDITO KIBBE")

    if submeter:
        if "Selecione" in p1 or "Selecione" in p2 or "Selecione" in p3:
            st.error("Por favor, responda todas as perguntas.")
        else:
            # --- IMPLEMENTAÇÃO DA SUA LÓGICA DE PROGRAMAÇÃO ---
            resultado = ""
            
            # Extraindo apenas a letra da resposta
            resp1 = p1[0]
            resp2 = p2[0]
            resp3 = p3[0]

            # FAIXA ALTA (>= 1.70m)
            if altura >= 1.70:
                if resp2 == "A" and resp3 == "A": resultado = "DRAMATIC"
                elif resp2 == "C" or resp3 == "B": resultado = "SOFT DRAMATIC"
                else: resultado = "FLAMBOYANT NATURAL"

            # FAIXA PETIT (<= 1.62m)
            elif altura <= 1.62:
                if resp2 == "C" and resp3 == "B":
                    resultado = "ROMANTIC" if resp1 == "C" else "SOFT GAMINE"
                elif resp2 == "A" or resp1 == "A":
                    resultado = "FLAMBOYANT GAMINE"
                elif resp2 == "B" and resp3 == "B":
                    resultado = "THEATRICAL ROMANTIC"
                else:
                    resultado = "SOFT GAMINE"

            # FAIXA MÉDIA (1.63m - 1.69m)
            else:
                if resp2 == "B":
                    resultado = "SOFT CLASSIC" if resp3 == "B" else "DRAMATIC CLASSIC"
                elif resp2 == "A":
                    resultado = "NATURAL" if resp3 == "B" else "FLAMBOYANT NATURAL"
                else:
                    resultado = "SOFT NATURAL"

            st.success(f"### VEREDITO KIBBE: {resultado}")
            
            # Imagem Instrutiva dos Corpos
            

            whats = "5515996398197"
            msg = f"Olá Jéssica Maria! Fiz o teste no site. Meu nome é {nome}, tenho {altura}m e o veredito foi {resultado}. Quero agendar!"
            st.link_button("💬 VALIDAR CONSULTORIA NO WHATSAPP", f"https://wa.me/{whats}?text={msg.replace(' ', '%20')}")

# --- 3. NAVEGAÇÃO ---
pg = st.navigation({
    "Maison": [st.Page(pagina_inicio, title="Início", icon="🏠")],
    "Método": [st.Page(pagina_posts, title="Journal", icon="📖")],
    "Análise": [st.Page(pagina_teste_kibbe, title="Teste Kibbe", icon="📏")]
})
pg.run()
