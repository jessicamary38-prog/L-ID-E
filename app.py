import streamlit as st
import os

# --- 1. CONFIGURAÇÕES DE PÁGINA E ESTILO ---
st.set_page_config(
    page_title="Maison L'Idée - Jéssica Maria", 
    page_icon="⚜️", 
    layout="centered"
)

# Estilização para o visual de Luxo/Consultoria
st.markdown("""
    <style>
    .main { background-color: #fcfaf7; }
    .stButton>button {
        background-color: #D4AF37;
        color: white;
        border-radius: 10px;
        font-weight: bold;
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #B8860B;
    }
    h1, h2, h3 { color: #4a3728; font-family: 'serif'; }
    .st-emotion-cache-16idsys p { font-size: 1.1rem; line-height: 1.6; color: #5D4037; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. FUNÇÕES DAS PÁGINAS ---

def pagina_inicio():
    st.title("⚜️ Maison L'Idée")
    st.subheader("O Olhar por trás da Maison")
    
    # Banner Principal
    st.image("https://images.unsplash.com/photo-1490481651871-ab68de25d43d?auto=format&fit=crop&q=80&w=1000")
    
    st.divider()
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Tenta carregar sua foto perfil.jpg do GitHub
        if os.path.exists("perfil.jpg"):
            st.image("perfil.jpg", caption="Jéssica Maria")
        else:
            st.warning("⚠️ Suba sua foto como 'perfil.jpg' no GitHub.")
        
        st.markdown("### Conecte-se")
        st.link_button("📸 INSTAGRAM", "https://www.instagram.com/jessicamargo.mr")
        st.link_button("📌 PINTEREST", "https://www.pinterest.com/jessicamary38")
        
    with col2:
        st.markdown("""
        Sou uma apaixonada por moda que transformou a curiosidade em uma busca incessante pelas estratégias mais profundas de imagem. 
        Minha jornada começou com os estudos dos métodos de **David Kibbe e John Kitchener**, onde me encantei pela forma como a estrutura física e as essências moldam quem somos.

        No entanto, ao unir esses métodos, percebi que ainda faltava uma peça no quebra-cabeça: **a humanidade sistêmica**.

        Há anos, mergulho nos estudos dos temperamentos, da neurociência e do comportamento humano. Dessa investigação nasceu o meu método exclusivo. Eu não olho apenas para a roupa; eu olho para a mulher como um sistema inteiro, integrando:
        
        * **Corpo:** A geometria e as linhas naturais.
        * **Face:** O visagismo que revela a identidade.
        * **Essência:** Quem você é por dentro, refletido no seu exterior.

        Para garantir a precisão dessa entrega, uni o sensível ao tecnológico. Desenvolvi tecnologias próprias através de **Engenharia de Prompts**, que utilizo para validar meu método e garantir que cada consultoria seja baseada em dados criteriosos e uma análise profunda.

        Meu objetivo na **Maison L'Idée** é oferecer a você uma imagem que não seja apenas harmônica, mas que seja o reflexo fiel da sua força e vitalidade.

        **Prazer, Jéssica Maria.**
        """)

def pagina_posts():
    st.title("📖 Journal Maison L'Idée")
    st.write("Dicas de estilo e estratégia visual.")
    st.divider()

    # --- PARA ADICIONAR NOVOS POSTS, COPIE O BLOCO ABAIXO ---
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image("https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?q=80&w=400")
    with c2:
        st.header("A Força da Linha Vertical")
        st.write("Descubra como o caimento das peças altera a percepção da sua estatura.")
        with st.expander("Ler mais"):
            st.write("No sistema Kibbe, a verticalidade define se o seu look deve ser contínuo ou se permite quebras visuais.")
    st.divider()
    # -------------------------------------------------------

def pagina_teste_kibbe():
    st.title("📏 Teste de Geometria Corporal (Kibbe)")
    st.info("Responda com base na sua estrutura natural.")

    with st.form("form_kibbe"):
        nome = st.text_input("Nome da cliente:")
        altura = st.number_input("Altura (m):", min_value=1.0, max_value=2.20, value=1.60, step=0.01)
        st.divider()
        p1 = st.radio("1. Como você parece nas fotos?", ["A) Longilínea", "B) Proporcional", "C) Petit"])
        p2 = st.radio("2. Linha Ombro vs Quadril:", ["A) Reta ou V", "B) Simétrica", "C) Curva em 8"])
        p3 = st.radio("3. Sensação da Carne/Pele:", ["A) Firme", "B) Macia"])
        
        submeter = st.form_submit_button("REVELAR RESULTADO")

    if submeter:
        if not nome:
            st.warning("Por favor, digite o nome.")
        else:
            # Lógica de Altura Jéssica Maria
            if altura >= 1.70:
                res = "DRAMATIC" if "A)" in p2 else "SOFT DRAMATIC"
            elif altura <= 1.62:
                res = "ROMANTIC" if "C)" in p2 else "SOFT GAMINE"
            else:
                res = "CLASSIC FAMILY"
            
            st.success(f"### RESULTADO: {res}")
            
            # Botão WhatsApp
            whats = "5515996398197"
            msg = f"Olá Jéssica! Fiz o teste no site e meu resultado foi {res}. Quero agendar minha análise!"
            st.link_button("💬 AGENDAR NO WHATSAPP", f"https://wa.me/{whats}?text={msg.replace(' ', '%20')}")

# --- 3. NAVEGAÇÃO ---
pg = st.navigation({
    "Maison": [st.Page(pagina_inicio, title="A Maison", icon="🏠")],
    "Conteúdo": [st.Page(pagina_posts, title="Journal", icon="📖")],
    "Análise": [st.Page(pagina_teste_kibbe, title="Teste Kibbe", icon="📏")]
})
pg.run()
