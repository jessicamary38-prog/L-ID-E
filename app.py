import streamlit as st

# --- 1. CONFIGURAÇÕES TÉCNICAS E ESTILO ---
st.set_page_config(
    page_title="Maison L'Idée - Consultoria", 
    page_icon="⚜️", 
    layout="centered"
)

# Estilização CSS para um visual Premium
st.markdown("""
    <style>
    .main { background-color: #fcfaf7; }
    .stButton>button {
        background-color: #D4AF37;
        color: white;
        border-radius: 10px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #B8860B;
        border-color: #B8860B;
    }
    h1, h2, h3 { color: #4a3728; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. FUNÇÕES DE CADA PÁGINA ---

def pagina_inicio():
    st.title("⚜️ Bem-vinda à Maison L'Idée")
    st.subheader("Consultoria de Imagem Estratégica & Geometria Corporal")
    
    st.image("https://images.unsplash.com/photo-1490481651871-ab68de25d43d?auto=format&fit=crop&q=80&w=1000", caption="Elegância e Estratégia")
    
    st.divider()
    
    # SEÇÃO: QUEM SOU EU
    col1, col2 = st.columns([1, 2])
    with col1:
        # Sugestão: Substitua por uma foto sua hospedada online
        st.image("https://cdn-icons-png.flaticon.com/512/607/607414.png", caption="Sua Consultora") 
        
    with col2:
        st.header("Quem Sou Eu")
        st.write("""
        Olá! Eu sou a mente por trás da **Maison L'Idée**. 
        Especialista em **Sistemas Kibbe e Essências Faciais**, o meu trabalho é 
        descodificar a geometria do seu corpo para que a sua imagem externa 
        reflita a sua força interna. 
        
        Acredito que a beleza é uma harmonia matemática e visual que todas possuímos. 
        Aqui no Clube, ajudo mulheres a encontrarem o seu ID Visual com ciência e sensibilidade.
        """)
        
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("📸 INSTAGRAM", "https://instagram.com/seu_perfil") # Atualize seu link
        with c2:
            st.link_button("📌 PINTEREST", "https://pinterest.com/seu_perfil") # Atualize seu link

def pagina_posts():
    st.title("📖 Journal Maison L'Idée")
    st.write("Explore os nossos guias exclusivos para membros do Clube.")
    st.divider()

    # Post 1
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image("https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?q=80&w=400")
    with c2:
        st.header("O Segredo da Linha Vertical")
        st.write("A verticalidade no sistema Kibbe não é sobre sua altura real...")
        with st.expander("Ler Post Completo"):
            st.markdown("A linha vertical é a distância do ombro aos joelhos. Se você tem uma vertical alta, tecidos longos favorecem sua silhueta.")

    st.divider()

    # Post 2
    c3, c4 = st.columns([1, 2])
    with c3:
        st.image("https://images.unsplash.com/photo-1509631179647-0177331693ae?q=80&w=400")
    with c4:
        st.header("Essências Faciais")
        st.write("O seu rosto comunica mensagens que o seu corpo confirma...")
        with st.expander("Ler Post Completo"):
            st.markdown("As Essências Faciais cuidam dos detalhes próximos ao rosto, como golas, brincos e maquiagem.")

def pagina_teste_kibbe():
    st.title("📏 Consultoria de Imagem: Sistema Kibbe")
    st.info("Responda com base na sua geometria natural (sem roupas modeladoras).")

    with st.form("form_kibbe_final"):
        nome = st.text_input("Nome da cliente:")
        altura = st.number_input("Altura (ex: 1.52):", min_value=1.0, max_value=2.20, value=1.60, step=0.01)
        
        st.divider()
        st.subheader("--- TESTE DE GEOMETRIA CORPORAL ---")
        
        p1 = st.radio("1. Independente da altura real, como você parece nas fotos?", 
                     ["A) Longilínea (pareço mais alta)", "B) Proporcional", "C) Petit (pareço pequena)"])

        p2 = st.radio("2. Olhando a linha que vai do ombro ao quadril:", 
                     ["A) É reta ou em V (ombros mandam)", "B) É contínua e simétrica", "C) É uma curva em 8 (quadril/busto saem da linha)"])

        p3 = st.radio("3. A sensação da sua pele/músculo é:", 
                     ["A) Firme e densa", "B) Macia e suave"])

        submeter = st.form_submit_button("REVELAR VEREDITO KIBBE")

    if submeter:
        if not nome:
            st.warning("Por favor, digite o nome.")
        else:
            resultado = ""
            # LÓGICA DE PRECISÃO (SEU MÓDULO)
            if altura >= 1.70:
                if "A)" in p2 and "A)" in p3: resultado = "DRAMATIC"
                elif "C)" in p2 or "B)" in p3: resultado = "SOFT DRAMATIC"
                else: resultado = "FLAMBOYANT NATURAL"
            elif altura <= 1.62:
                if "C)" in p2 and "B)" in p3:
                    resultado = "ROMANTIC" if "C)" in p1 else "SOFT GAMINE"
                elif "A)" in p2 or "A)" in p1: resultado = "FLAMBOYANT GAMINE"
                elif "B)" in p2 and "B)" in p3: resultado = "THEATRICAL ROMANTIC"
                else: resultado = "SOFT GAMINE"
            else:
                if "B)" in p2: resultado = "SOFT CLASSIC" if "B)" in p3 else "DRAMATIC CLASSIC"
                elif "A)" in p2: resultado = "NATURAL" if "B)" in p3 else "FLAMBOYANT NATURAL"
                else: resultado = "SOFT NATURAL"

            st.success(f"### VEREDITO KIBBE PARA {nome.upper()}: {resultado}")
            
            # Botão WhatsApp
            whats = "5515996398197"
            msg = f"Olá! Sou {nome}. Meu resultado no teste Kibbe foi: {resultado}. Quero agendar minha análise!"
            st.link_button("💬 ENVIAR RESULTADO PARA A MAISON", f"https://wa.me/{whats}?text={msg.replace(' ', '%20')}")

# --- 3. NAVEGAÇÃO ---
pg = st.navigation({
    "Maison": [st.Page(pagina_inicio, title="Início", icon="🏠")],
    "Conteúdo": [st.Page(pagina_posts, title="Journal / Blog", icon="📖")],
    "Análise": [st.Page(pagina_teste_kibbe, title="Teste Kibbe Real", icon="📏")]
})

pg.run()
