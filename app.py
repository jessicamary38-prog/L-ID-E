import streamlit as st
import os

# --- 1. CONFIGURAÇÕES DE PÁGINA E ESTILO ---
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
    }
    .stButton>button:hover {
        background-color: #B8860B;
    }
    h1, h2, h3 { color: #4a3728; font-family: 'serif'; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. FUNÇÕES DAS PÁGINAS ---

def pagina_inicio():
    st.title("⚜️ Maison L'Idée")
    st.subheader("O Olhar por trás da Maison")
    
    # --- FOTO 1: BANNER PRINCIPAL (ATUALIZADO) ---
    st.image("https://replicate.delivery/pbxt/u7MhO6iOq8LwGhLq0b3gE6Q6OQ0P7Q0Q6Q6OQ0P7Q0Q6Q0Q0P7Q0Q6/output.jpg") # Novo link do banner jpg
    
    st.divider()
    
    # SEÇÃO: MANIFESTO JÉSSICA MARIA
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # --- FOTO 2: PERFIL PROFISSIONAL ---
        if os.path.exists("perfil.jpg"):
            st.image("perfil.jpg", caption="Jéssica Maria") # Carrega perfil.jpg local
        else:
            st.warning("⚠️ Suba sua foto como 'perfil.jpg' no GitHub.")
        
        st.markdown("### Conecte-se")
        st.link_button("📸 INSTAGRAM", "https://www.instagram.com/jessicamargo.mr")
        st.link_button("📌 PINTEREST", "https://www.pinterest.com/jessicamary38")
        
    with col2:
        st.markdown("""
        ### O Olhar por trás da Maison
        
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
    st.write("Explore os nossos guias e reflexões sobre estratégia visual.")
    st.divider()

    # Post de Exemplo
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image("https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?q=80&w=400")
    with c2:
        st.header("A Força da Linha Vertical")
        st.write("Entenda como a percepção de altura define a sua silhueta.")
        with st.expander("Ler Post Completo"):
            st.write("A verticalidade dita como as peças devem ser cortadas para favorecer a sua silhueta.")
    st.divider()

def pagina_teste_kibbe():
    st.title("📏 Teste de Geometria Corporal")
    with st.form("form_kibbe"):
        nome = st.text_input("Nome da cliente:")
        altura = st.number_input("Altura (m):", min_value=1.0, max_value=2.20, value=1.60, step=0.01)
        st.divider()
        p1 = st.radio("1. Como você parece nas fotos?", ["A) Longilínea", "B) Proporcional", "C) Petit"])
        p2 = st.radio("2. Linha Ombro vs Quadril:", ["A) Reta ou V", "B) Simétrica", "C) Curva em 8"])
        p3 = st.radio("3. Sensação da Carne:", ["A) Firme", "B) Macia"])
        submeter = st.form_submit_button("REVELAR RESULTADO")

    if submeter:
        if not nome:
            st.warning("Por favor, digite o nome.")
        else:
            resultado = ""
            if altura >= 1.70:
                resultado = "DRAMATIC" if "A)" in p2 else "SOFT DRAMATIC"
            elif altura <= 1.62:
                resultado = "ROMANTIC" if "C)" in p2 else "SOFT GAMINE"
            else:
                resultado = "CLASSIC FAMILY"

            st.success(f"### RESULTADO: {resultado}")
            whats = "5515996398197"
            msg = f"Olá Jéssica Maria! Meu resultado foi {resultado}. Quero agendar!"
            st.link_button("💬 AGENDAR NO WHATSAPP", f"https://wa.me/{whats}?text={msg.replace(' ', '%20')}")

# --- 3. SISTEMA DE NAVEGAÇÃO ---
pg = st.navigation({
    "A Maison": [st.Page(pagina_inicio, title="Início", icon="🏠")],
    "Conteúdo": [st.Page(pagina_posts, title="Journal", icon="📖")],
    "Análise": [st.Page(pagina_teste_kibbe, title="Teste Kibbe", icon="📏")]
})
pg.run()
